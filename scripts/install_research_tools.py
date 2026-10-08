#!/usr/bin/env python3
"""Install llm-wiki research helper skills and bounded agent roots.

The default mode is preview-only. Use --apply to write files, and combine
--apply --fetch-km to clone/reuse the upstream knowledge-manager checkout.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


MANAGED_BY = "llm-wiki-install_research_tools"
SCHEMA_VERSION = 1
SKILL_NAMES = ("project-init", "project-literature", "km-search", "llm-wiki-ops")
DEFAULT_KM_URL = "https://github.com/treylom/knowledge-manager"
WRITABLE_AGENT_OUTPUTS = ("reports", "candidates", "briefings")
AGENT_ROLES = ("rch-db", "rch-projects")
FORWARD_FILES = ("CLAUDE.md", "GEMINI.md")
MANAGED_TEXT = "<!-- managed-by: llm-wiki-install_research_tools -->"


class InstallError(RuntimeError):
    """Raised when an install request would violate the bounded write contract."""


@dataclass(frozen=True)
class Action:
    kind: str
    path: Path
    detail: str

    def as_dict(self) -> dict[str, str]:
        return {"kind": self.kind, "path": str(self.path), "detail": self.detail}


def script_default_db_root() -> Path:
    return Path(__file__).resolve().parent.parent


def expand_path(value: str | Path) -> Path:
    return Path(value).expanduser()


def resolve_existing_safe(path: Path) -> Path:
    """Resolve a path without allowing existing symlink components."""
    expanded = expand_path(path)
    current = expanded.anchor and Path(expanded.anchor) or Path(".")
    parts = expanded.parts[1:] if expanded.anchor else expanded.parts
    for part in parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise InstallError(f"Refusing symlink path component: {current}")
    return expanded.resolve(strict=False)


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        resolved = resolve_existing_safe(path)
        if resolved not in seen:
            seen.add(resolved)
            result.append(resolved)
    return result


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str, apply: bool, actions: list[Action]) -> None:
    if path.exists() and read_text(path) == content:
        actions.append(Action("unchanged", path, "content already current"))
        return
    actions.append(Action("write", path, "create or replace managed file"))
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def backup_path(path: Path, suffix: str = ".bak") -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return path.with_name(f"{path.name}.{stamp}{suffix}")


def backup_file(path: Path, apply: bool, actions: list[Action], destination: Path | None = None) -> Path:
    target = destination or backup_path(path)
    actions.append(Action("backup", target, f"backup existing {path.name}"))
    if apply:
        if target.exists() and read_text(target) != read_text(path):
            target = backup_path(path)
        shutil.copy2(path, target)
    return target


def write_text_with_backup(path: Path, content: str, apply: bool, actions: list[Action]) -> None:
    if path.exists() and read_text(path) == content:
        actions.append(Action("unchanged", path, "content already current"))
        return
    if path.exists():
        backup_file(path, apply, actions)
    write_text(path, content, apply, actions)


def managed_json(path: Path) -> bool:
    if not path.exists():
        return True
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return data.get("managed_by") == MANAGED_BY


def write_managed_json(path: Path, data: dict[str, object], apply: bool, actions: list[Action]) -> None:
    content = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if path.exists() and not managed_json(path):
        if read_text(path) == content:
            actions.append(Action("unchanged", path, "existing config matches requested content"))
            return
        raise InstallError(f"Refusing to clobber unmanaged config: {path}")
    if path.is_symlink():
        backup = backup_path(path)
        actions.append(Action("backup-symlink", backup, f"rename symlink {path.name} without touching target"))
        if apply:
            path.rename(backup)
    write_text(path, content, apply, actions)


def render_skill_template(template_root: Path, skill_name: str, db_root: Path) -> str:
    template = template_root / skill_name / "SKILL.md"
    if not template.is_file():
        raise InstallError(f"Missing skill template: {template}")
    return read_text(template).replace("{{DB_ROOT}}", str(db_root))


def display_path(path: Path, path_style: str) -> str:
    resolved = str(path)
    if path_style == "windows":
        parts = path.parts
        if len(parts) >= 3 and parts[0] == "/" and parts[1] == "mnt" and len(parts[2]) == 1:
            drive = parts[2].upper()
            rest = "/".join(parts[3:])
            return f"{drive}:/{rest}" if rest else f"{drive}:/"
    return resolved


def find_git_root(path: Path) -> Path | None:
    current = path if path.is_dir() else path.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def skill_binding(
    db_root_value: str,
    km_upstream_path: Path | None,
    km_git_rev: str | None,
    path_style: str,
) -> dict[str, object]:
    data: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "managed_by": MANAGED_BY,
        "db_root": db_root_value,
        "km_upstream_path": display_path(km_upstream_path, path_style) if km_upstream_path else None,
    }
    if km_git_rev:
        data["km_git_rev"] = km_git_rev
    return data


def detach_symlink_target(
    skill_dir: Path,
    skill_file: Path,
    apply: bool,
    actions: list[Action],
) -> tuple[str | None, Path | None]:
    """Detach a symlinked skill dir/file without writing through to its target."""
    symlink_path: Path | None = None
    original_skill: Path | None = None
    if skill_dir.is_symlink():
        symlink_path = skill_dir
        original_skill = (skill_dir / "SKILL.md").resolve(strict=True)
    elif skill_file.is_symlink():
        symlink_path = skill_file
        original_skill = skill_file.resolve(strict=True)
    if not symlink_path or not original_skill:
        return None, None

    upstream_content = original_skill.read_text(encoding="utf-8")
    upstream_root = find_git_root(original_skill) or original_skill.parent
    backup = backup_path(symlink_path)
    actions.append(Action("backup-symlink", backup, f"rename symlink {symlink_path.name} without touching target"))
    if apply:
        symlink_path.rename(backup)
        skill_dir.mkdir(parents=True, exist_ok=True)
    return upstream_content, upstream_root


def replace_skill_file(
    target: Path,
    content: str,
    apply: bool,
    actions: list[Action],
    *,
    km_overlay: bool = False,
    upstream_seed_content: str | None = None,
) -> Path | None:
    skill_dir = target.parent
    upstream_content, upstream_root = detach_symlink_target(skill_dir, target, apply, actions)
    preserved_upstream = upstream_content if upstream_content is not None else upstream_seed_content
    if preserved_upstream is not None and km_overlay:
        upstream_file = skill_dir / "upstream-SKILL.md"
        if upstream_file.exists() and read_text(upstream_file) == preserved_upstream:
            actions.append(Action("unchanged", upstream_file, "upstream km-search SKILL.md already preserved"))
        else:
            actions.append(Action("write", upstream_file, "preserve upstream km-search SKILL.md for local fallback"))
            if apply:
                upstream_file.parent.mkdir(parents=True, exist_ok=True)
                upstream_file.write_text(preserved_upstream, encoding="utf-8")

    if target.exists() and not target.is_symlink() and read_text(target) == content:
        actions.append(Action("unchanged", target, "skill already current"))
        return upstream_root
    if target.exists() and not target.is_symlink():
        if km_overlay:
            upstream = target.with_name("upstream-SKILL.md")
            if not upstream.exists() or read_text(upstream) != read_text(target):
                backup_file(target, apply, actions, destination=upstream)
        else:
            backup_file(target, apply, actions)
    write_text(target, content, apply, actions)
    return upstream_root


def validate_template_root(template_root: Path) -> None:
    for skill_name in SKILL_NAMES:
        template = template_root / skill_name / "SKILL.md"
        if not template.is_file():
            raise InstallError(f"Missing required template for {skill_name}: {template}")


def locate_km_skill(km_upstream_path: Path | None) -> Path | None:
    if not km_upstream_path:
        return None
    candidates = [
        km_upstream_path / ".agent" / "skills" / "km-search" / "SKILL.md",
        km_upstream_path / "skills" / "km-search" / "SKILL.md",
        km_upstream_path / "km-search" / "SKILL.md",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    for candidate in km_upstream_path.rglob("SKILL.md"):
        if candidate.parent.name == "km-search":
            return candidate
    return None


def run_git(args: list[str], cwd: Path | None = None) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def fetch_km_repo(km_source: Path, db_root: Path, apply: bool, actions: list[Action]) -> tuple[Path | None, str | None]:
    km_source = resolve_existing_safe(km_source)
    if is_relative_to(km_source, db_root):
        raise InstallError(f"Refusing to place knowledge-manager checkout inside DB root: {km_source}")
    if not apply:
        raise InstallError("--fetch-km requires --apply so dependency fetches are never accidental")

    if (km_source / ".git").is_dir():
        actions.append(Action("reuse", km_source, "existing knowledge-manager git checkout"))
    elif km_source.exists() and any(km_source.iterdir()):
        raise InstallError(f"Refusing non-empty non-git km source: {km_source}")
    else:
        actions.append(Action("clone", km_source, DEFAULT_KM_URL))
        km_source.parent.mkdir(parents=True, exist_ok=True)
        run_git(["clone", DEFAULT_KM_URL, str(km_source)])

    skill_files = list(km_source.rglob("SKILL.md"))
    if not skill_files:
        raise InstallError(f"Fetched/reused KM repo has no SKILL.md resources: {km_source}")
    rev = run_git(["rev-parse", "HEAD"], cwd=km_source)
    actions.append(Action("record", km_source, f"knowledge-manager revision {rev}"))
    return km_source, rev


def install_skills(
    *,
    db_root: Path,
    template_root: Path,
    skills_dirs: list[Path],
    km_upstream_path: Path | None,
    km_git_rev: str | None,
    path_style: str,
    apply: bool,
    actions: list[Action],
) -> None:
    validate_template_root(template_root)
    db_root_value = display_path(db_root, path_style)
    upstream_km_skill = locate_km_skill(km_upstream_path)
    upstream_km_content = read_text(upstream_km_skill) if upstream_km_skill else None
    for skills_dir in skills_dirs:
        for skill_name in SKILL_NAMES:
            binding_file = skills_dir / skill_name / "binding.json"
            if binding_file.exists() and not managed_json(binding_file):
                raise InstallError(f"Refusing to clobber unmanaged config: {binding_file}")

    for skills_dir in skills_dirs:
        for skill_name in SKILL_NAMES:
            skill_dir = skills_dir / skill_name
            skill_file = skill_dir / "SKILL.md"
            binding_file = skill_dir / "binding.json"
            content = render_skill_template(template_root, skill_name, Path(db_root_value))
            detected_upstream = replace_skill_file(
                skill_file,
                content,
                apply,
                actions,
                km_overlay=(skill_name == "km-search"),
                upstream_seed_content=upstream_km_content if skill_name == "km-search" else None,
            )
            skill_km_upstream = km_upstream_path or (detected_upstream if skill_name == "km-search" else None)
            write_managed_json(
                binding_file,
                skill_binding(db_root_value, skill_km_upstream, km_git_rev, path_style),
                apply,
                actions,
            )


def agent_config(db_root_value: str, phd_root_value: str | None, role: str) -> dict[str, object]:
    if role == "rch-db":
        read_scope: dict[str, object] = {
            "db_root": db_root_value,
            "phd_root": None,
            "phd_read_policy": "disallowed",
            "auto_scan_phd": False,
        }
        phd_reads_allowed = False
    else:
        read_scope = {
            "db_root": db_root_value,
            "phd_root": phd_root_value,
            "phd_read_policy": "allowlisted_projects_only",
            "allowed_project_files": ["PROJECT.md", "STATUS.md"],
            "auto_scan_phd": False,
        }
        phd_reads_allowed = bool(phd_root_value)
    return {
        "schema_version": SCHEMA_VERSION,
        "managed_by": MANAGED_BY,
        "role": role,
        "db_root": db_root_value,
        "phd_root": phd_root_value if phd_root_value else "Undecided",
        "phd_reads_allowed": phd_reads_allowed,
        "allowlisted_projects": [],
        "read_scope": read_scope,
        "write_scope": list(WRITABLE_AGENT_OUTPUTS),
        "startup": {
            "no_bots": True,
            "no_credentials": True,
            "no_auto_phd_scan": True,
        },
    }


def agent_readme(db_root_value: str, phd_root_value: str | None, role: str) -> str:
    if role == "rch-db":
        phd_line = "- PhD root: not in scope for this role\n- PhD reads are disallowed.\n"
        role_line = "- Role: DB-only literature/wiki operations against the bound llm-wiki root.\n"
    elif phd_root_value:
        phd_line = (
            f"- PhD root: {phd_root_value}\n"
            "- PhD reads require explicit allowlisted_projects entries and are limited to PROJECT.md/STATUS.md.\n"
        )
        role_line = "- Role: project status/context reader plus bounded report/candidate/briefing outputs.\n"
    else:
        phd_line = "- PhD root: Undecided\n- PhD reads are disallowed until --phd-root and allowlisted_projects are configured.\n"
        role_line = "- Role: project-facing outputs with no PhD project reads yet.\n"
    return (
        f"{MANAGED_TEXT}\n"
        f"# {role}\n\n"
        "This agent root is managed by llm-wiki research tooling.\n\n"
        f"- DB root: {db_root_value}\n"
        f"{role_line}"
        f"{phd_line}"
        "- Startup must not launch bots, access credentials, or scan PhD folders automatically.\n"
        "- Write outputs only under reports/, candidates/, and briefings/.\n"
    )


def root_agents_md(db_root_value: str, phd_root_value: str | None) -> str:
    phd_status = phd_root_value if phd_root_value else "Undecided; PhD reads disallowed"
    return (
        f"{MANAGED_TEXT}\n"
        "# Research Agents\n\n"
        "Minimal bounded research-agent root generated by install_research_tools.py.\n\n"
        f"- DB root: {db_root_value}\n"
        f"- PhD root: {phd_status}\n"
        "- rch-db: DB-only role. It must not read the PhD root.\n"
        "- rch-projects: PhD reads require explicit allowlisted_projects and are limited to PROJECT.md/STATUS.md.\n"
        "- Do not start bots, load credentials, or scan PhD folders at startup.\n"
        "- Agents may write only reports/, candidates/, and briefings/ beneath their own role folder.\n"
    )


def forward_file(role_hint: str = "") -> str:
    hint = f" for {role_hint}" if role_hint else ""
    return (
        f"{MANAGED_TEXT}\n"
        f"# Forward{hint}\n\n"
        "Read AGENTS.md in this directory first. It is the generated operating contract for GJC/AGY-compatible agents.\n"
    )


def preflight_agent_targets(agents_root: Path) -> None:
    for role in AGENT_ROLES:
        config_file = agents_root / role / "config.json"
        if config_file.exists() and not managed_json(config_file):
            raise InstallError(f"Refusing to clobber unmanaged config: {config_file}")


def install_agents(
    *,
    db_root: Path,
    agents_root: Path,
    phd_root: Path | None,
    path_style: str,
    apply: bool,
    actions: list[Action],
) -> None:
    preflight_agent_targets(agents_root)
    db_root_value = display_path(db_root, path_style)
    phd_root_value = display_path(phd_root, path_style) if phd_root else None

    write_text_with_backup(agents_root / "AGENTS.md", root_agents_md(db_root_value, phd_root_value), apply, actions)
    for name in FORWARD_FILES:
        write_text_with_backup(agents_root / name, forward_file(), apply, actions)

    for role in AGENT_ROLES:
        role_root = agents_root / role
        write_text_with_backup(role_root / "AGENTS.md", agent_readme(db_root_value, phd_root_value, role), apply, actions)
        for name in FORWARD_FILES:
            write_text_with_backup(role_root / name, forward_file(role), apply, actions)
        write_managed_json(role_root / "config.json", agent_config(db_root_value, phd_root_value, role), apply, actions)
        for folder in WRITABLE_AGENT_OUTPUTS:
            path = role_root / folder
            actions.append(Action("mkdir", path, "bounded agent output directory"))
            if apply:
                path.mkdir(parents=True, exist_ok=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-root", type=Path, default=script_default_db_root(), help="llm-wiki DB root")
    parser.add_argument(
        "--template-root",
        type=Path,
        default=None,
        help="skill template root; defaults to DB templates/research-skills",
    )
    parser.add_argument(
        "--skills-dir",
        action="append",
        type=Path,
        default=None,
        help="skill destination directory; repeatable; default ~/.codex/skills",
    )
    parser.add_argument(
        "--agents-root",
        type=Path,
        default=None,
        help="research agents root; defaults to sibling research-agents next to DB root",
    )
    parser.add_argument("--phd-root", type=Path, default=None, help="optional PhD root; omitted keeps PhD reads disabled")
    parser.add_argument("--apply", action="store_true", help="write changes; default previews only")
    parser.add_argument("--skip-agents", action="store_true", help="install skills only; useful for second platform deployments")
    parser.add_argument(
        "--path-style",
        choices=("native", "windows"),
        default="native",
        help="rendered path style for SKILL.md and binding.json; filesystem access remains native",
    )
    parser.add_argument("--fetch-km", action="store_true", help="clone or reuse upstream knowledge-manager checkout")
    parser.add_argument(
        "--km-source",
        type=Path,
        default=Path("~/.local/share/llm-wiki/knowledge-manager"),
        help="non-cloud knowledge-manager checkout location",
    )
    return parser


def plan_install(args: argparse.Namespace) -> list[Action]:
    db_root = resolve_existing_safe(args.db_root)
    if not db_root.exists():
        raise InstallError(f"DB root does not exist: {db_root}")
    template_root = resolve_existing_safe(args.template_root or (db_root / "templates" / "research-skills"))
    skills_dirs = unique_paths(args.skills_dir or [Path("~/.codex/skills")])
    agents_root = resolve_existing_safe(args.agents_root or (db_root.parent / "research-agents"))
    phd_root = resolve_existing_safe(args.phd_root) if args.phd_root else None

    actions: list[Action] = []
    km_upstream_path: Path | None = None
    km_git_rev: str | None = None
    if args.fetch_km:
        km_upstream_path, km_git_rev = fetch_km_repo(args.km_source, db_root, args.apply, actions)

    if not args.skip_agents:
        preflight_agent_targets(agents_root)

    install_skills(
        db_root=db_root,
        template_root=template_root,
        skills_dirs=skills_dirs,
        km_upstream_path=km_upstream_path,
        km_git_rev=km_git_rev,
        path_style=args.path_style,
        apply=args.apply,
        actions=actions,
    )
    if not args.skip_agents:
        install_agents(
            db_root=db_root,
            agents_root=agents_root,
            phd_root=phd_root,
            path_style=args.path_style,
            apply=args.apply,
            actions=actions,
        )
    return actions


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        actions = plan_install(args)
    except (InstallError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"error: {exc}\n")
    mode = "apply" if args.apply else "preview"
    print(json.dumps({"mode": mode, "actions": [action.as_dict() for action in actions]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
