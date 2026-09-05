# llm-wiki 연구 데이터베이스

Language: [English README (EN)](README.md) · **한국어 (KO)**

이 저장소는 논문을 ingest하고, 영어 연구 카드와 source, 설정된 언어의 wiki, 검색용 인덱스, 참고문헌, 정적 HTML 사이트를 생성하는 공개용 `llm-wiki` 템플릿입니다.

초기 저장소는 의도적으로 비어 있습니다. 개인 논문 카드, source, wiki 레코드, PDF는 포함하지 않습니다.

구현 사양은 [llm-wiki Custom Build PRD](docs/llm-wiki-custom-prd.md)에 있습니다.

## 설치

저장소 안에 가상환경을 만들지 말고, OneDrive 밖의 경로를 사용하세요.

### Windows PowerShell

```powershell
git clone https://github.com/seongyonglee77/LLM-Wiki-Rch-DB.git
Set-Location LLM-Wiki-Rch-DB
py -3 -m venv D:\win-python\llm-wiki-venv
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install --upgrade pip
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install pyyaml docling
```

이미 `D:\win-python\master_venv`에 Docling이 설치되어 있다면 그 Python을 사용해도 됩니다.

### WSL/Linux

```bash
git clone https://github.com/seongyonglee77/LLM-Wiki-Rch-DB.git
cd LLM-Wiki-Rch-DB
python3 -m venv /mnt/d/WSL/llm-wiki-venv
/mnt/d/WSL/llm-wiki-venv/bin/python -m pip install --upgrade pip
/mnt/d/WSL/llm-wiki-venv/bin/python -m pip install pyyaml docling
```

Windows와 WSL은 서로 다른 Python 환경을 사용해야 합니다.

## PDF ingest

승인한 PDF를 로컬 `inbox/`에 넣고 저장소 루트에서 실행합니다.

```powershell
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\ingest_batch.py
```

이 작업은 다음을 생성·갱신합니다.

- 영어 source와 summary card
- `km-config.json`에 설정한 언어의 wiki 페이지
- registry, indexes, `refs.bib`, QC report
- 정적 HTML 사이트인 `wiki-site/`

PDF는 GitHub에 올리지 않습니다. 생성된 카드와 wiki를 검토하고 QC 결과를 확인한 후 commit하세요.

## 간단한 사용법

스크립트 이름을 외울 필요 없이, 이 저장소를 작업 폴더로 연 LLM에게 자연어로 요청하면 됩니다.

1. LLM을 이 저장소에서 열어 `AGENTS.md`를 읽게 합니다.
2. 승인한 PDF를 로컬 `inbox/`에 넣습니다.
3. 다음처럼 요청합니다: `inbox의 새 PDF를 전부 ingest해 줘.`
4. `sources/`, `cards/`, `wiki/`, `refs.bib`, `qc/`를 검토합니다.
5. 필요하면 다음처럼 검증을 요청합니다: `이 카드의 주장과 직접 인용을 source와 대조하고 wiki 링크를 확인해 줘.`
6. 검토가 끝난 레코드만 commit합니다. PDF와 개인 작업 메모는 공개 저장소 밖에 둡니다.

자주 쓰는 요청:

```text
llm-wiki 안에서 내 주제와 관련된 논문을 찾아 줘.
open 카드의 metadata를 점검하되 locked 레코드는 변경하지 말고 차이만 보고해 줘.
승인한 카드 변경을 registry, indexes, refs.bib, QC에 반영해 줘.
이 논문을 기존 wiki에 연결할 후보를 제안하되 card와 source를 복제하지 마.
```

이 저장소의 운영 원칙은 한 논문을 하나의 canonical record로 유지하고, 근거가 있는 상세 요약·wiki 링크·생성 bibliography·QC를 함께 검토하는 것입니다.

## 언어 설정

논문 내용 언어와 wiki 설명 언어는 독립적으로 설정합니다.

```json
{
  "paper_language": "en",
  "wiki_language": "ko"
}
```

기본값은 논문 카드·source는 영어(`en`), wiki 설명은 한국어(`ko`)입니다. 다른 사용자는 `km-config.json`에서 자신의 언어 코드로 변경할 수 있습니다.

## 생성 파일과 검증

```powershell
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_registry.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_indexes.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\export_refs_bib.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\qc_report.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_html_site.py --output wiki-site
```

`refs.bib`, `registry/`, `indexes/`, `qc/`는 생성 결과이므로 직접 편집하지 않습니다. 원본 카드와 설정을 수정한 뒤 다시 생성하세요.

## GitHub Pages

`.github/workflows/pages.yml`이 `main`에 push될 때 `wiki-site/`를 GitHub Pages로 배포합니다. GitHub 저장소의 Pages 설정에서 source를 **GitHub Actions**로 선택하세요.

초기 사이트는 빈 공개 템플릿입니다. 검토가 끝난 카드만 공개 저장소에 추가하세요.
