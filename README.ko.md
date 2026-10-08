# llm-wiki 연구 데이터베이스

Language: [English README (EN)](README.md) · **한국어 (KO)**

Release: **v0.2.2** · portable 설치·연구 프로젝트·에이전트 워크플로

이 저장소는 논문 PDF를 로컬에서 파싱하고, 영어 source·summary card·영어 기본 wiki·검색 인덱스·참고문헌·정적 HTML 사이트를 생성하는 공개용 `llm-wiki` 템플릿입니다. 저장소에는 개인 논문 기록과 원본 PDF가 포함되지 않습니다. 논문 기록 언어와 wiki 종합 언어는 별도로 설정합니다.

구현 사양은 [llm-wiki Custom PRD](docs/llm-wiki-custom-prd.md)에 있습니다.

## 제공 기능

- 개인 논문·PDF·프로젝트 기록을 포함하지 않는 빈 공개용 llm-wiki 템플릿
- 근거 기반 ingest, citation metadata, wiki synthesis, 색인, bibliography, QC, 정적 사이트 생성
- 프로젝트 초기화·문헌 원장 도구와 DB 바인딩 Knowledge Manager 검색 및 DB 전용 운영 스킬
- 설치 저장소 위치에서 DB 경로를 자동 감지하고, 연구 프로젝트·agent 경로는 사용자 선택으로 설정

## 권장 2단계 요약 프로파일

저장소의 Python 스크립트는 특정 LLM을 직접 호출하지 않으며 모델에 독립적입니다. 선택한 모델로 요약을 작성하고, 두 번째 패스에서 원문 근거를 확인할 수 있습니다.

```text
Docling 파싱
  → 임시 이미지 정리 Markdown 생성
  → 선택한 모델이 상세 요약과 evidence JSON 작성
  → 두 번째 패스에서 원문 근거·인용문·주장을 검증
  → 결정적 스크립트가 직접 인용문과 필수 섹션 검증
  → 최종 파일명 변경 및 registry/index/QC/HTML 재생성
```

두 번째 검증 패스는 실용적인 critic 단계이지 독립적인 진실성 보장을 의미하지 않습니다. 직접 인용문 검사, 페이지 표식 규칙, QC, 사람의 검토가 계속 필요합니다. 페이지 정보가 parsed Markdown에 없으면 PDF를 다시 읽어 페이지를 추정하지 않고, 정확한 인용문을 `source_text`로 남기며 페이지를 비워 둡니다.

## 설치

저장소가 클라우드 동기화 폴더 안에 있을 수 있으므로, 저장소 안에 가상환경·캐시를 만들지 말고 동기화 폴더 밖의 OS 전용 Python 환경을 사용하세요.

### Windows PowerShell

실행 전에 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY`를 설치할 저장소(예: 본인의 fork)의 HTTPS 주소로 바꾸고, `DB_FOLDER`와 `PYTHON_ENV` 위치를 직접 정하세요. 명령이 상위 폴더와 마지막 DB 폴더를 만듭니다. 설치 스크립트는 그 폴더 안의 자기 위치를 기준으로 DB 경로를 자동 감지하므로 개인 PC 경로를 코드에 넣지 않습니다. `PYTHON_ENV`는 저장소나 클라우드 동기화 폴더 바깥에 둡니다.

```powershell
$REPOSITORY_URL = 'https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git'
$DB_FOLDER = 'C:\Research\llm-wiki-db' # 사용할 위치로 변경
$PYTHON_ENV = 'C:\ResearchTools\llm-wiki-venv' # 동기화되지 않는 위치를 선택
New-Item -ItemType Directory -Force -Path (Split-Path $DB_FOLDER) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path $PYTHON_ENV) | Out-Null
git clone $REPOSITORY_URL $DB_FOLDER
Set-Location $DB_FOLDER
py -3 -m venv $PYTHON_ENV
& "$PYTHON_ENV\Scripts\python.exe" -m pip install --upgrade pip
& "$PYTHON_ENV\Scripts\python.exe" -m pip install pyyaml docling
```

`<...>` 부분은 각 사용자의 실제 로컬 경로로 바꿉니다. 가상환경은 OneDrive 등 동기화 폴더 밖에 둡니다.

### WSL2/Linux

`REPOSITORY_URL`을 설치할 저장소 또는 fork 주소로, `DB_FOLDER`와 `PYTHON_ENV`를 원하는 경로로 바꾸세요. 명령이 상위 폴더를 만들고 `git clone`이 마지막 DB 폴더를 만듭니다. 설치기는 자신의 위치에서 DB 경로를 자동 감지합니다.

```bash
REPOSITORY_URL="https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git"
DB_FOLDER="$HOME/research/llm-wiki-db" # 사용할 위치로 변경
PYTHON_ENV="$HOME/.local/venvs/llm-wiki" # OS 전용, 클라우드 동기화 밖
mkdir -p "$(dirname "$DB_FOLDER")"
mkdir -p "$(dirname "$PYTHON_ENV")"
git clone "$REPOSITORY_URL" "$DB_FOLDER"
cd "$DB_FOLDER"
python3 -m venv "$PYTHON_ENV"
"$PYTHON_ENV/bin/python" -m pip install --upgrade pip pyyaml docling
```

Windows Python과 WSL Python은 서로 다른 환경을 사용해야 합니다.

### macOS

`REPOSITORY_URL`을 설치할 저장소 또는 fork 주소로, `DB_FOLDER`와 `PYTHON_ENV`를 원하는 경로로 바꾸세요. 명령이 상위 폴더를 만들고 `git clone`이 마지막 DB 폴더를 만듭니다. 설치기는 자신의 위치에서 DB 경로를 자동 감지합니다.

```bash
REPOSITORY_URL="https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git"
DB_FOLDER="$HOME/research/llm-wiki-db" # 사용할 위치로 변경
PYTHON_ENV="$HOME/.local/venvs/llm-wiki" # macOS 전용, 클라우드 동기화 밖
mkdir -p "$(dirname "$DB_FOLDER")"
mkdir -p "$(dirname "$PYTHON_ENV")"
git clone "$REPOSITORY_URL" "$DB_FOLDER"
cd "$DB_FOLDER"
python3 -m venv "$PYTHON_ENV"
"$PYTHON_ENV/bin/python" -m pip install --upgrade pip pyyaml docling
```

macOS 전용 Python을 사용하고 iCloud Drive 및 다른 동기화 폴더 바깥에 환경을 둡니다.

### 연구 워크플로 설치와 경로 설정

DB 폴더에서 먼저 preview한 뒤 적용합니다. `--fetch-km`은 upstream Knowledge Manager checkout을 클라우드 동기화 폴더 바깥에 선택적으로 받습니다. 기본 에이전트 루트는 DB 폴더와 나란한 `research-agents/`이며, 연구 프로젝트 root는 프로젝트 접근을 허용하려는 경우 직접 지정합니다.

```powershell
py -3 scripts\install_research_tools.py
py -3 scripts\install_research_tools.py --apply --fetch-km --path-style windows
```

```bash
python3 scripts/install_research_tools.py
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native
```

프로젝트는 DB 폴더 밖에 두며 `project-config.json`이 현재 호스트에서 유효한 DB 경로와 고정 검색 범위를 연결합니다. 기존 문서는 덮어쓰지 않습니다. Codex/GJC/AGY에 설치할 추가 위치는 `--skills-dir`를 반복 지정합니다.

설치기는 내려받은 저장소 위치를 DB root로 자동 인식합니다. 반면 연구 프로젝트 위치는 자동 추측하지 않습니다. `--phd-root`를 생략하면 프로젝트 읽기는 비활성화되고, 허용할 연구 프로젝트 루트를 직접 지정해야 합니다. 기존 CLI 옵션 이름은 `--phd-root`지만, 이 옵션이 지정하는 대상은 연구 프로젝트 root입니다. `research-agents` 폴더는 기본적으로 DB 폴더의 형제 위치에 생성되며, 원하면 `--agents-root`로 사용자가 정한 위치를 지정할 수 있습니다. 이 값들은 설치 시 호스트별 설정이며 저장소에 개인 절대경로로 기록되지 않습니다.

연구 프로젝트 접근을 허용하려면 아래처럼 두 경로를 직접 지정하세요. 설치를 실행하는 OS에서 유효한 경로를 사용합니다.

```powershell
py -3 scripts\install_research_tools.py --apply --fetch-km --path-style windows --phd-root '<사용자가_정한_연구_프로젝트_루트>' --agents-root '<사용자가_정한_에이전트_루트>'
```

```bash
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native --phd-root '<사용자가_정한_연구_프로젝트_루트>' --agents-root '<사용자가_정한_에이전트_루트>'
```

처음에는 `--apply` 없이 preview를 실행하고 생성 예정 경로를 확인한 뒤, 같은 명령에 `--apply`를 추가해 적용하세요. Windows와 WSL 클라이언트가 동기화 DB를 함께 쓰면 각 OS에서 유효한 `--skills-dir`와 `--path-style`로 각각 설치하며, 두 번째 설치에서 공용 agent hub를 다시 쓰지 않도록 `--skip-agents`를 사용합니다. Windows·WSL/Linux·macOS의 Python 환경은 서로 공유하지 않습니다.

### 권장 폴더 구조

문헌 DB, 활성 연구 프로젝트, 에이전트 작업 공간을 서로 복사하거나 중첩하지 말고 병렬로 둡니다. 아래 이름과 상위 경로는 예시이므로 사용자가 자신의 저장 위치에 맞게 정합니다.

```text
<사용자가_선택한_작업공간>/
├── research-db/                 내려받은 llm-wiki 저장소; DB root 자동 감지
├── research-projects/           연구 프로젝트; DB 안에 복제하지 않음
│   └── <project>/               원고/연구별 독립 작업 폴더
│       ├── AGENTS.md             프로젝트 규칙과 DB 연결 경계
│       ├── PROJECT.md / STATUS.md
│       ├── literature-evidence.json + literature-evidence.md
│       ├── citation-gaps.md / references.bib
│       ├── citation-packets/ / drafts/ / outlines/
│       └── methods/ / resources/ / submission/ (필요에 따라)
├── research-agents/             DB corpus 밖의 역할별 작업 공간
│   ├── rch-db/                   DB 검색; reports/candidates/briefings에만 기록
│   └── rch-projects/             명시적으로 허용한 프로젝트 상태만 읽음
└── research-ops/                선택 사항: CFP·아이디어·일정·통합 보고
```

`project-init`은 누락 파일만 만들고 연구 내용을 임의로 채우지 않습니다. 설치기는 내려받은 저장소 위치에서 DB root를 자동 감지하지만 연구 프로젝트 root는 추측하지 않으며, `--phd-root`가 없으면 프로젝트 읽기가 비활성화됩니다. 이 기존 CLI 옵션은 연구 프로젝트 root를 지정합니다. `--agents-root`로 병렬 에이전트 폴더의 위치를 직접 지정할 수 있습니다.

### 프로젝트 초기화 및 자연어 사용

프로젝트 폴더를 코딩 에이전트에서 열고 **“이 프로젝트 표준 초기화해 줘”**라고 요청합니다. `project-init`은 preview 후 필요한 파일만 생성하고, `project-config.json`에 현재 DB 경로와 `indexes`, `wiki`, `cards`, `sources` 검색 범위를 연결합니다. CLI로는 다음처럼 실행할 수 있습니다.

```bash
python3 "<DB_ROOT>/scripts/project_init.py" --project "<PROJECT_ROOT>"
python3 "<DB_ROOT>/scripts/project_init.py" --project "<PROJECT_ROOT>" --apply
```

```text
KM으로 내 DB에서 teacher agency 관련 문헌을 찾아 후보 표에 정리해 줘.
후보 2와 4의 원문 근거를 확인하고 citation packet을 만들어 줘.
선택 문헌으로 문헌고찰 아웃라인을 작성해 줘.
이 초안의 인용을 검증하고 STATUS.md에 다음 작업을 기록해 줘.
최신 논문을 웹/학술검색으로 찾아 줘.   # 요청한 경우에만 외부 검색
```

KM 검색은 연결된 DB를 대상으로 하는 읽기 전용 검색입니다. 후보 선택, 근거 원장 기록, citation packet, 프로젝트 Bib 생성은 별도의 `project-literature` 작업입니다. 검색 결과 자체가 인용 승인으로 취급되지는 않습니다.

## PDF ingest

검토할 PDF를 로컬 `inbox/`에 넣고 저장소 루트에서 실행합니다.

```powershell
py -3 scripts\ingest_batch.py
```

또는 LLM 에이전트에게 다음처럼 요청합니다.

```text
inbox의 새 PDF를 전부 ingest해 줘. 근거가 포함된 상세 요약을 작성하고 원문 인용을 검증해 줘.
```

완료 후 `sources/`, `cards/`, `wiki/`, `registry/`, `indexes/`, `refs.bib`, `qc/`, `wiki-site/`를 검토하세요. 원본 PDF와 개인 작업 메모는 GitHub에 commit하지 않습니다.

## 빈 저장소 재빌드와 검증

```powershell
py -3 scripts\build_registry.py
py -3 scripts\build_indexes.py
py -3 scripts\export_refs_bib.py
py -3 scripts\qc_report.py
py -3 scripts\build_html_site.py --output wiki-site
```

## GitHub Pages

`.github/workflows/pages.yml`이 `main` push를 감지해 `wiki-site/`를 GitHub Pages로 배포합니다. 저장소 Settings → Pages → Source에서 **GitHub Actions**를 선택하세요.

## 정적 위키 사이트 보기와 공개

`wiki-site/`는 wiki·cards·parsed sources를 보여 주는 생성형 읽기 전용 사이트입니다. ingest/rebuild 후 `wiki-site/index.html`을 브라우저에서 열어 Obsidian 없이 확인할 수 있습니다. GitHub Pages 공개는 선택 사항이며, 공개 전에 생성된 모든 문서에 비공개 연구자료·저작권 문제가 없는지 검토하세요. 원본 PDF나 미검토 프로젝트 노트는 공개하지 않습니다.

## 릴리스 기록

### v0.2.2

- 설치할 저장소 URL, DB 위치, Python 환경, 선택적 연구 프로젝트 루트와 agent 작업 공간을 사용자가 정하는 범용 설치 안내를 추가했습니다.
- 내려받은 저장소에서 DB root를 자동 감지하고, 연구 프로젝트 접근은 명시적 설정 전까지 비활성화하는 경계를 문서화했습니다.
- DB·연구 프로젝트·research-agents 병렬 폴더 구조, project-init/project-literature 자연어 사용 예, wiki-site 로컬 보기·선택적 공개 안내를 추가했습니다.
- maintainer 개인 GitHub 주소와 로컬 절대경로를 사용자 설정 자리표시자로 교체했습니다.

### v0.2.1

- 개인 연구자료를 포함하지 않는 빈 공개용 템플릿으로 정리했습니다.
- ingest workflow, template, script, navigation, test와 정적 HTML shell을 포함합니다.

### v0.2.0

- 논문 ingest에 잠정 파일명을 사용하고, 요약 메타데이터 확정 후 최종 파일명을 적용합니다.
- PDF, source, card, wiki, manifest, registry, index, bibliography, QC, HTML에서 `YYYY_Author_ShortTitle`을 일관되게 사용합니다.
- Literature Review, Findings, Discussion에 원문 근거를 요구하는 통합 summary-card YAML 구조를 적용했습니다.
- 직접 인용을 parsed source와 검증합니다. 믿을 만한 page marker가 없으면 `source_text`로 남기고 페이지 검토를 요청합니다.
- 정적 사이트가 `wiki/`, `cards/`, `sources/`를 렌더링하며 원본 PDF는 공개 저장소에서 제외됩니다.
- 파일명 정규화, record 재키잉, 요약 입력 정리, 근거 기반 카드 생성 테스트를 포함합니다.
