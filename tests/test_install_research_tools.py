import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_research_tools import InstallError, build_parser, display_path, main, plan_install  # noqa: E402


def make_templates(root: Path) -> Path:
    template_root = root / "templates" / "research-skills"
    for name in ("project-init", "project-literature", "km-search", "llm-wiki-ops"):
        folder = template_root / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(f"# {name}\nDB={{{{DB_ROOT}}}}\n", encoding="utf-8")
    return template_root


def parse_args(*items: str):
    return build_parser().parse_args(list(items))


def run_main(args: list[str]) -> int:
    with contextlib.redirect_stdout(io.StringIO()):
        return main(args)


class InstallResearchToolsTests(unittest.TestCase):
    def test_preview_does_not_write_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            skills_dir = root / "skills"
            agents_root = root / "research-agents"

            actions = plan_install(
                parse_args(
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(skills_dir),
                    "--agents-root",
                    str(agents_root),
                )
            )

            self.assertTrue(any(action.kind == "write" for action in actions))
            self.assertFalse((skills_dir / "project-init" / "SKILL.md").exists())
            self.assertFalse((agents_root / "AGENTS.md").exists())

    def test_apply_installs_rendered_skills_bindings_and_bounded_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            skills_dir = root / "skills"
            agents_root = root / "research-agents"

            exit_code = run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(skills_dir),
                    "--skills-dir",
                    str(skills_dir),
                    "--agents-root",
                    str(agents_root),
                ]
            )

            self.assertEqual(exit_code, 0)
            skill_file = skills_dir / "project-init" / "SKILL.md"
            self.assertIn(str(db_root.resolve()), skill_file.read_text(encoding="utf-8"))
            self.assertNotIn("{{DB_ROOT}}", skill_file.read_text(encoding="utf-8"))
            binding = json.loads((skills_dir / "project-init" / "binding.json").read_text(encoding="utf-8"))
            self.assertEqual(binding["schema_version"], 1)
            self.assertEqual(binding["db_root"], str(db_root.resolve()))
            self.assertIsNone(binding["km_upstream_path"])

            config = json.loads((agents_root / "rch-db" / "config.json").read_text(encoding="utf-8"))
            self.assertEqual(config["phd_root"], "Undecided")
            self.assertFalse(config["phd_reads_allowed"])
            self.assertEqual(config["allowlisted_projects"], [])
            self.assertEqual(config["read_scope"]["phd_read_policy"], "disallowed")
            self.assertEqual(config["write_scope"], ["reports", "candidates", "briefings"])
            self.assertTrue((agents_root / "rch-projects" / "briefings").is_dir())
            self.assertTrue((agents_root / "CLAUDE.md").exists())
            self.assertTrue((agents_root / "GEMINI.md").exists())

    def test_agents_have_role_specific_phd_allowlist_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            phd_root = root / "phd"
            db_root.mkdir()
            phd_root.mkdir()
            template_root = make_templates(root)
            agents_root = root / "research-agents"

            run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--phd-root",
                    str(phd_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(root / "skills"),
                    "--agents-root",
                    str(agents_root),
                ]
            )

            db_config = json.loads((agents_root / "rch-db" / "config.json").read_text(encoding="utf-8"))
            projects_config = json.loads((agents_root / "rch-projects" / "config.json").read_text(encoding="utf-8"))
            self.assertFalse(db_config["phd_reads_allowed"])
            self.assertIsNone(db_config["read_scope"]["phd_root"])
            self.assertEqual(projects_config["allowlisted_projects"], [])
            self.assertTrue(projects_config["phd_reads_allowed"])
            self.assertEqual(projects_config["read_scope"]["phd_read_policy"], "allowlisted_projects_only")
            self.assertEqual(projects_config["read_scope"]["allowed_project_files"], ["PROJECT.md", "STATUS.md"])
            self.assertFalse(projects_config["read_scope"]["auto_scan_phd"])

    def test_existing_agent_text_is_backed_up_before_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            agents_root = root / "research-agents"
            agents_root.mkdir()
            (agents_root / "AGENTS.md").write_text("human notes\n", encoding="utf-8")

            run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(root / "skills"),
                    "--agents-root",
                    str(agents_root),
                ]
            )

            backups = list(agents_root.glob("AGENTS.md.*.bak"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "human notes\n")
            self.assertIn("managed-by", (agents_root / "AGENTS.md").read_text(encoding="utf-8"))

    def test_unmanaged_agent_config_aborts_before_skill_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            skills_dir = root / "skills"
            agents_root = root / "research-agents"
            (agents_root / "rch-db").mkdir(parents=True)
            (agents_root / "rch-db" / "config.json").write_text('{"owner":"person"}\n', encoding="utf-8")

            with self.assertRaises(InstallError):
                plan_install(
                    parse_args(
                        "--apply",
                        "--db-root",
                        str(db_root),
                        "--template-root",
                        str(template_root),
                        "--skills-dir",
                        str(skills_dir),
                        "--agents-root",
                        str(agents_root),
                    )
                )
            self.assertFalse((skills_dir / "project-init" / "SKILL.md").exists())

    def test_skip_agents_allows_second_platform_skill_deployment_without_touching_agent_hub(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            agents_root = root / "research-agents"

            run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(root / "skills-native"),
                    "--agents-root",
                    str(agents_root),
                ]
            )
            original_config = (agents_root / "rch-db" / "config.json").read_text(encoding="utf-8")
            run_main(
                [
                    "--apply",
                    "--skip-agents",
                    "--path-style",
                    "windows",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(root / "skills-windows"),
                    "--agents-root",
                    str(agents_root),
                ]
            )

            self.assertEqual((agents_root / "rch-db" / "config.json").read_text(encoding="utf-8"), original_config)
            self.assertTrue((root / "skills-windows" / "project-init" / "SKILL.md").exists())

    def test_backups_existing_skill_and_preserves_km_upstream_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            skills_dir = root / "skills"
            (skills_dir / "project-init").mkdir(parents=True)
            (skills_dir / "project-init" / "SKILL.md").write_text("old project init", encoding="utf-8")
            (skills_dir / "km-search").mkdir(parents=True)
            (skills_dir / "km-search" / "SKILL.md").write_text("upstream km content", encoding="utf-8")

            run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(skills_dir),
                    "--agents-root",
                    str(root / "agents"),
                ]
            )

            backups = list((skills_dir / "project-init").glob("SKILL.md.*.bak"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "old project init")
            self.assertEqual(
                (skills_dir / "km-search" / "upstream-SKILL.md").read_text(encoding="utf-8"),
                "upstream km content",
            )
            self.assertIn("# km-search", (skills_dir / "km-search" / "SKILL.md").read_text(encoding="utf-8"))

    def test_refuses_unmanaged_binding_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            skills_dir = root / "skills"
            (skills_dir / "project-init").mkdir(parents=True)
            (skills_dir / "project-init" / "binding.json").write_text('{"owner":"person"}\n', encoding="utf-8")

            with self.assertRaises(InstallError):
                plan_install(
                    parse_args(
                        "--apply",
                        "--db-root",
                        str(db_root),
                        "--template-root",
                        str(template_root),
                        "--skills-dir",
                        str(skills_dir),
                        "--agents-root",
                        str(root / "agents"),
                    )
                )

    def test_fetch_km_requires_apply_and_disallows_db_nested_checkout(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)

            with self.assertRaises(InstallError):
                plan_install(
                    parse_args(
                        "--fetch-km",
                        "--db-root",
                        str(db_root),
                        "--template-root",
                        str(template_root),
                        "--skills-dir",
                        str(root / "skills"),
                        "--agents-root",
                        str(root / "agents"),
                    )
                )
            with self.assertRaises(InstallError):
                plan_install(
                    parse_args(
                        "--apply",
                        "--fetch-km",
                        "--db-root",
                        str(db_root),
                        "--template-root",
                        str(template_root),
                        "--skills-dir",
                        str(root / "skills"),
                        "--agents-root",
                        str(root / "agents"),
                        "--km-source",
                        str(db_root / "runtime" / "knowledge-manager"),
                    )
                )

    def test_fetch_km_reuses_valid_repo_and_records_revision_without_copying(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            km_source = root / "km"
            (km_source / ".git").mkdir(parents=True)
            (km_source / "some-skill").mkdir()
            (km_source / "some-skill" / "SKILL.md").write_text("# upstream\n", encoding="utf-8")
            (km_source / ".agent" / "skills" / "km-search").mkdir(parents=True)
            (km_source / ".agent" / "skills" / "km-search" / "SKILL.md").write_text(
                "# upstream km-search\n", encoding="utf-8"
            )

            with mock.patch("install_research_tools.run_git", return_value="abc123"):
                run_main(
                    [
                        "--apply",
                        "--fetch-km",
                        "--db-root",
                        str(db_root),
                        "--template-root",
                        str(template_root),
                        "--skills-dir",
                        str(root / "skills"),
                        "--agents-root",
                        str(root / "agents"),
                        "--km-source",
                        str(km_source),
                    ]
                )

            binding = json.loads((root / "skills" / "km-search" / "binding.json").read_text(encoding="utf-8"))
            self.assertEqual(binding["km_upstream_path"], str(km_source.resolve()))
            self.assertEqual(binding["km_git_rev"], "abc123")
            self.assertFalse((root / "skills" / "some-skill").exists())
            self.assertEqual(
                (root / "skills" / "km-search" / "upstream-SKILL.md").read_text(encoding="utf-8"),
                "# upstream km-search\n",
            )

    @unittest.skipIf(not hasattr(Path, "symlink_to"), "symlink support unavailable")
    def test_km_search_symlink_is_detached_without_touching_upstream_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_root = root / "db"
            db_root.mkdir()
            template_root = make_templates(root)
            upstream_repo = root / "plugin-cache" / "knowledge-manager"
            upstream_skill_dir = upstream_repo / "skills" / "km-search"
            upstream_skill_dir.mkdir(parents=True)
            (upstream_repo / ".git").mkdir()
            upstream_skill = upstream_skill_dir / "SKILL.md"
            upstream_skill.write_text("real upstream cache skill", encoding="utf-8")
            skills_dir = root / "skills"
            km_dir = skills_dir / "km-search"
            km_dir.mkdir(parents=True)
            linked_skill = km_dir / "SKILL.md"
            linked_skill.symlink_to(upstream_skill)

            run_main(
                [
                    "--apply",
                    "--db-root",
                    str(db_root),
                    "--template-root",
                    str(template_root),
                    "--skills-dir",
                    str(skills_dir),
                    "--agents-root",
                    str(root / "agents"),
                ]
            )

            self.assertFalse(linked_skill.is_symlink())
            self.assertEqual(upstream_skill.read_text(encoding="utf-8"), "real upstream cache skill")
            self.assertEqual((km_dir / "upstream-SKILL.md").read_text(encoding="utf-8"), "real upstream cache skill")
            self.assertEqual(len(list(km_dir.glob("SKILL.md.*.bak"))), 1)
            binding = json.loads((km_dir / "binding.json").read_text(encoding="utf-8"))
            self.assertEqual(binding["km_upstream_path"], str(upstream_repo.resolve()))

    def test_windows_path_style_renders_db_root_for_skills_and_binding(self):
        self.assertEqual(display_path(Path("/mnt/d/Example DB"), "windows"), "D:/Example DB")
        self.assertEqual(display_path(Path("/tmp/Example DB"), "windows"), "/tmp/Example DB")


if __name__ == "__main__":
    unittest.main()
