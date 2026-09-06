# llm-wiki 연구 데이터베이스

Language: [English README (EN)](README.md) · **한국어 (KO)**

Release: **v0.2.0** · 근거 기반 논문 ingest 파이프라인

이 저장소는 논문 PDF를 로컬에서 파싱하고, 영어 source·summary card·한국어 wiki·검색 인덱스·참고문헌·정적 HTML 사이트를 생성하는 공개용 `llm-wiki` 템플릿입니다. 저장소에는 개인 논문 기록과 원본 PDF가 포함되지 않습니다.

구현 사양은 [llm-wiki Custom PRD](docs/llm-wiki-custom-prd.md)에 있습니다.

## v0.2.0 변경 사항

- 파싱 직후 provisional 파일명을 만들고, 요약에서 확정한 연도·저자·제목으로 최종 파일명을 자동 확정합니다.
- 최종 `YYYY_Author_ShortTitle` stem을 PDF, source, card, wiki, parse manifest, registry, index, bibliography, QC, HTML에 일관되게 적용합니다.
- 요약카드는 통합 YAML 스키마를 사용하며 Literature Review, Findings, Discussion에 원문 근거가 필요합니다.
- 직접 인용문을 parsed source와 대조합니다. 신뢰할 수 있는 페이지 표식이 없으면 `source_text`로 표시하고 페이지 확인은 사람의 검토 대상으로 남깁니다.
- GitHub Pages용 정적 사이트가 `wiki/`, `cards/`, `sources/`를 함께 렌더링합니다. 원본 PDF는 로컬에만 둡니다.
- 파일명 정규화, record rekey, 요약 입력 정리, 근거 기반 카드 생성을 검증하는 테스트를 포함합니다.

## 권장 Luna–Luna 요약 프로파일

저장소의 Python 스크립트는 특정 LLM을 직접 호출하지 않으며 모델에 독립적입니다. Codex에서 운용할 때는 다음처럼 Luna를 두 번 사용하는 방식을 권장합니다.

```text
Docling 파싱
  → 임시 이미지 정리 Markdown 생성
  → Luna가 상세 요약과 evidence JSON 작성
  → 두 번째 Luna가 원문 근거·인용문·주장을 검증
  → 결정적 스크립트가 직접 인용문과 필수 섹션 검증
  → 최종 파일명 변경 및 registry/index/QC/HTML 재생성
```

두 번째 Luna 검증은 실용적인 critic 단계이지 독립적인 진실성 보장을 의미하지 않습니다. 직접 인용문 검사, 페이지 표식 규칙, QC, 사람의 검토가 계속 필요합니다. 페이지 정보가 parsed Markdown에 없으면 PDF를 다시 읽어 페이지를 추정하지 않고, 정확한 인용문을 `source_text`로 남기며 페이지를 비워 둡니다.

## 설치

저장소 안에 가상환경을 만들지 말고, OneDrive 밖의 Python 환경을 사용하세요.

### Windows PowerShell

```powershell
git clone https://github.com/seongyonglee77/LLM-Wiki-Rch-DB.git
Set-Location LLM-Wiki-Rch-DB
py -3 -m venv D:\win-python\llm-wiki-venv
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install --upgrade pip
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install pyyaml docling
```

이미 `D:\win-python\master_venv`에 Docling이 설치되어 있으면 그 환경을 사용해도 됩니다.

## PDF ingest

검토할 PDF를 로컬 `inbox/`에 넣고 저장소 루트에서 실행합니다.

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\ingest_batch.py
```

또는 LLM 에이전트에게 다음처럼 요청합니다.

```text
inbox의 새 PDF를 전부 ingest해 줘. 요약은 Luna로 작성하고, 두 번째 Luna 패스로 원문 진위 여부를 검증해 줘.
```

완료 후 `sources/`, `cards/`, `wiki/`, `registry/`, `indexes/`, `refs.bib`, `qc/`, `wiki-site/`를 검토하세요. 원본 PDF와 개인 작업 메모는 GitHub에 commit하지 않습니다.

## 빈 저장소 재빌드와 검증

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\build_registry.py
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\build_indexes.py
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\export_refs_bib.py
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\qc_report.py
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\build_html_site.py --output wiki-site
```

## GitHub Pages

`.github/workflows/pages.yml`이 `main` push를 감지해 `wiki-site/`를 GitHub Pages로 배포합니다. 저장소 Settings → Pages → Source에서 **GitHub Actions**를 선택하세요.
