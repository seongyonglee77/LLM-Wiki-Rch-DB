# 모델 요약 성능 평가 리포트

평가일: 2026-09-06  
평가 대상: `test_paper.md` 원문과 같은 폴더의 모델별 요약 5개  
평가 목적: llm-wiki에서 재사용할 수 있는 연구 카드·소스·위키 노드로서의 품질 평가

## 1. 종합 판정

**종합 1위는 Luna**, **가장 보수적이고 안전한 서술은 Terra**, **수치와 인용 표가 가장 유용한 보조자료는 Qwen**이다. 실무적으로는 Luna의 메타데이터/구조와 Terra의 신중한 해석, Qwen의 정량 표를 결합하는 것이 가장 좋다.

다만 다섯 파일 모두 바로 canonical card로 잠글 수 있는 상태는 아니다. 특히 `record_id`가 비어 있거나 benchmark용 slug로 되어 있고, 일부 `source_path`는 현재 폴더에 존재하지 않는다. llm-wiki 규칙상 먼저 정확한 `record_id`를 registry에서 확정해야 한다.

핵심 결론 자체는 다섯 요약에서 대체로 일치한다.

- 표본은 사우디의 고급 EFL 학습자 112명이고, ChatGPT-4와 교사 피드백을 두 시나리오에서 비교했다.
- ChatGPT는 즉시성·접근성·문법/문장 수준 지원에서 유용하다고 지각되었다.
- 교사 피드백은 개인화·내용·조직·방법론·동기/자신감 측면에서 더 신뢰되었다.
- 전체 과제군 차이는 `F = 2.40, p = .072`로 .05 수준에서 유의하지 않다.
- 연구의 실제 권고는 대체가 아니라 교사 피드백을 보완하는 hybrid model이다.

중요한 공통 주의점은 **이 연구가 객관적인 글쓰기 향상이나 인과효과를 직접 측정한 연구가 아니라, 학생의 지각·선호를 혼합방법으로 조사한 연구**라는 점이다. “ChatGPT가 덜 효과적이었다”, “교사가 불안을 낮췄다”, “AI가 공감/개인화를 재현할 수 없다”와 같은 표현은 원문보다 강한 주장으로 바뀌기 쉽다.

## 2. 평가 방법

원문은 128,959자, 약 10,512단어이며, 모델 요약은 2,054–4,912단어 범위였다. 평가는 단순 압축률이 아니라 다음 여섯 축으로 했다.

| 평가축 | 배점 | 판단 기준 |
|---|---:|---|
| 원문 사실 보존 | 25 | 연구 대상·설계·결과·제한을 원문 의미대로 보존하는가 |
| Hallucination/과장 통제 | 20 | 없는 사실을 만들지 않고 지각·상관·인과·유의성을 구분하는가 |
| 방법·수치 정확성 | 15 | 표본, 시나리오, 척도, RQ, 평균, ANOVA를 정확히 다루는가 |
| 근거 추적성 | 15 | 페이지, 표, 인용, 직접 인용/패러프레이즈가 재검증 가능한가 |
| llm-wiki 적합성 | 15 | Quick Card/Structured/Deep 구조, provenance, 제한, 재사용성 |
| 범위·가독성 | 10 | 핵심을 빠짐없이 전달하면서 중복과 과잉 해석을 줄이는가 |

점수는 100점 만점의 전문가 판정이며, 모델 파일의 frontmatter에 적힌 `claim_verification_pass_rate`를 그대로 신뢰하지 않았다. 원문 `test_paper.md`의 본문·표·부록과 각 요약의 실제 문장을 대조했다.

## 3. 순위와 점수

| 순위 | 모델 파일 | 분량(원문 대비) | 사실 보존 /25 | Hallucination 안전성 /20 | 방법·수치 /15 | 추적성 /15 | llm-wiki /15 | 범위·가독성 /10 | 총점 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | [luna](./test_paper%20-%20luna-summary.md) | 4,912 (46.7%) | 23 | 17 | 14 | 14 | 14 | 9 | **91** |
| 2 | [terra.medium](./test_paper%20-%20terra.medium-summary.md) | 4,846 (46.1%) | 23 | 18 | 14 | 13 | 11 | 9 | **88** |
| 3 | [qwen3.7plus](./test_paper%20-%20qwen3.7plus-summary.md) | 2,892 (27.5%) | 22 | 16 | 14 | 14 | 11 | 9 | **86** |
| 4 | [gemini 3.8 flash](./test_paper%20-%20gemini%203.8%20flash-summary.md) | 3,816 (36.3%) | 21 | 13 | 13 | 14 | 11 | 9 | **81** |
| 5 | [kimi-2.6](./test_paper%20-%20kimi-2.6-summary.md) | 2,054 (19.5%) | 20 | 15 | 12 | 8 | 10 | 8 | **73** |

분량은 품질 점수가 아니다. Kimi는 가장 짧지만 증거 추적성과 wiki 재사용성이 약하고, Luna/Terra는 길지만 연구문제·방법·결과·제한을 재사용할 수 있는 형태로 더 잘 보존한다.

## 4. 모델별 평가

### 4.1 Luna — 종합 1위, canonical card의 가장 가까운 초안

강점:

- `Quick Card → Structured Summary → Deep Summary`가 llm-wiki 카드 구조와 가장 잘 맞는다.
- DOI, URL, 출판일, 권·페이지, source hash, provenance, 페이지 기준을 갖추고 있어 metadata와 evidence가 분리되어 있다.
- `F = 2.40, p = .072`를 “전체 과제군 차이는 유의하지 않음”으로 해석하고, item-level/질적 결과와 구분한다.
- hidden AI-assisted feedback과 explicit student consultation을 구별하고, 같은 교사·서로 다른 과제라는 비교의 confounding도 제한으로 언급한다.
- “writing improvement를 직접 측정하지 않고 perception을 측정했다”는 한계를 명시해 llm-wiki의 재인용 안전성이 높다.

Hallucination/과장 위험:

- DOI·출판일·권·페이지는 원문 Markdown 본문에서 나온 정보가 아니라 Springer/외부 메타데이터 보강이다. 파일이 provenance에 이를 밝히고 있으므로 허위라기보다 **외부 출처 보강**이지만, 원문 대조 리포트에서는 별도 표시해야 한다.
- `feedback ecology`, `affective support`, `teacher agency` 같은 표현은 유용한 synthesis이지만 원문의 직접 표현이 아니라 해석이다.
- “AI가 relational reassurance를 제공하지 않는다”는 결론은 학생 지각에 대한 해석으로 써야 하며, 모든 AI 시스템에 대한 보편 명제로 쓰면 안 된다.

판정: **기본 서술 후보**. 단, 외부 메타데이터에는 출처를 유지하고, 해석 문장에는 `원문 결과의 해석` 표지를 붙인다.

### 4.2 Terra.medium — hallucination 통제가 가장 좋음

강점:

- 전체 ANOVA가 유의하지 않다는 점을 명확히 한 뒤, item-level 패턴과 질적 설명을 별도로 다룬다.
- “학생이 교사 피드백을 더 신뢰했다”와 “교사 피드백이 객관적으로 더 효과적이었다”를 대체로 구분한다.
- qualitative coding detail 부족, same-instructor confound, 일반화 한계를 언급한다.
- 연구를 replacement가 아니라 complementary model로 읽고, “usefulness와 preference는 다르다”는 중요한 해석을 보존한다.

Hallucination/과장 위험:

- `feedback ecology`, `academic-rhetorical depth`, `teacher effects are inseparable`는 대부분 타당한 해석이지만 원문의 직접 결과와 구분하면 더 안전하다.
- `pypdf로 PDF를 spot-check했다`는 provenance 서술은 이 benchmark 파일만으로는 독립 검증되지 않는다. 실제 검증 로그가 없으면 QC evidence로 간주해서는 안 된다.
- frontmatter의 `record_id`가 비어 있고, `source_path`가 현재 존재하지 않는 `inbox/test_paper - terra.medium.md`를 가리킨다.

판정: **서술·해석의 안전성 기준으로는 1위**. Luna의 metadata와 Qwen의 수치 표를 보완해 canonical card를 만들 때 가장 좋은 문장 기반이다.

### 4.3 Qwen3.7plus — 정량·증거 구조가 가장 실용적

강점:

- Table 2의 네 평균, 표준편차, 95% CI와 ANOVA 결과를 한눈에 재사용할 수 있다.
- `Directly Citable Evidence` 표가 많고, 연구질문별 Findings 분리가 명확하다.
- hidden/explicit 시나리오, 4점 Likert, six-phase thematic analysis를 빠짐없이 보존한다.
- 핵심 수치의 의미를 대체로 정확히 읽었다.

Hallucination/과장 위험:

- “one of the first studies”, “novel methodological separation”, “isolating awareness effects”는 원문이 입증하지 않는다. 두 시나리오는 인식 차이를 **탐색할 수 있는 설계**이지, awareness effect를 분리·식별한 실험은 아니다.
- `effect size`라는 원문 문구를 인용하지만 숫자나 산출 방법은 제시되지 않는다. 이를 통계적 효과크기 결과처럼 재사용하면 안 된다.
- `Scite`를 전문 도구 예로 추가한 부분은 원문에 나온 Grammarly, Writefull, Elicit보다 근거가 약하다.
- 본문에 `??`, `慣` 등 인코딩 손상이 있어 직접 카드로 옮기기 어렵다.
- `record_id`와 `source_hash`가 비어 있다.

판정: **수치·인용 appendix 후보**. “significant”, “isolating”, “first”를 삭제하고 인코딩을 복구하면 매우 유용하다.

### 4.4 Gemini 3.8 Flash — 범위는 가장 풍부하지만 과장 위험이 큼

강점:

- 이론, 방법, RQ별 결과, 직접 인용, 제한, 후속 연구까지 가장 폭넓게 커버한다.
- 원문의 표본·시나리오·평균·ANOVA·부록 문항을 잘 찾아냈다.
- 직접 인용과 페이지를 붙여 문헌고찰 재사용성이 높다.

Hallucination/과장 위험:

- “instructor feedback was rated **significantly** more effective”와 “instructor feedback exerted a **substantially greater positive effect**”는 원문의 지각 결과와 ‘effect size가 더 컸다’는 서술을 통계적 유의성·인과효과로 강화한다.
- `AI could not replicate`, `essential reassurance`, `24/7 availability`, `one of the earliest studies`, `isolating awareness effects`는 원문보다 강하거나 원문에 없는 주장이다.
- `major public university`, `near-native`도 원문의 “public university”, “C2-level”보다 강한 표현이다.
- `feedback literacy`를 핵심 이론으로 전면화했지만, 원문에서는 관련 참고문헌과 개념이 존재하더라도 본 연구의 명시적 분석틀로 제시된 것은 아니다.
- `record_id`, `source_hash`가 비어 있다.

판정: **풍부한 research note**로는 좋지만, 원문 충실성이 필요한 카드에는 직접 사용하지 않는다. 모든 “effect/significant/cannot”를 학생의 지각 또는 연구자의 논의 수준으로 낮춰야 한다.

### 4.5 Kimi-2.6 — 빠른 개요로는 좋지만 증거 카드로는 부족

강점:

- 가장 짧은 분량으로 핵심 결론, 시나리오, 주요 장단점을 전달한다.
- DOI와 저널명을 원문에서 확인하지 못했다고 명시한 점은 무리한 metadata 생성을 피한 좋은 태도다.
- 핵심적인 수치 `F = 2.40, p = .072`는 보존했다.

Hallucination/과장·운영 위험:

- `one of the first studies`, `isolate awareness effects`는 원문 근거가 없다.
- 페이지가 거의 없고, Directly Citable Evidence가 모두 `N/A`라서 인용 재검증이 어렵다.
- `Quick Card`, `Structured Summary`, `Deep Summary`, `Relevance to My Study` 중 상위 섹션이 비어 있거나 실질 내용이 적다.
- frontmatter는 `record_id`가 일반 slug이고 `source_path`/`pdf_path`가 존재하지 않는 benchmark 입력을 가리킨다. `quote_verification_pass_rate: 0.0`도 실제 검증 근거가 없어 canonical evidence로 쓸 수 없다.
- “표본 크기가 descriptive research에 충분하다”는 원문이 인용한 기준을 요약한 것이지만, 일반적인 표본 적정성 판정으로 확대하면 안 된다.

판정: **Quick Card 초안**으로만 활용. 근거 표와 페이지, 제한·재사용 섹션을 보강하지 않으면 canonical card 후보가 아니다.

## 5. Hallucination 판정표

### 원문으로 직접 확인되는 안전한 주장

`112명`, `Saudi EFL`, `C2`, `ChatGPT-4`, `네 개 과제`, `두 시나리오`, `4점 Likert`, `F = 2.40`, `p = .072`, `즉시성·접근성`, `문법·문장 조직`, `교사의 조직·내용·방법론 관련 선호`, `AI 피드백 과부하`, `hybrid recommendation`은 원문에서 확인된다. 단, “선호”와 “효과”는 원문이 주로 **학생의 지각**을 보고한다는 조건을 붙여야 한다.

### 반복적으로 발견되는 과장 패턴

| 위험한 표현 | 안전한 표현 |
|---|---|
| ChatGPT가 글쓰기 향상을 가져왔다 | 학생들이 ChatGPT 피드백이 글쓰기 향상에 유용하다고 지각했다 |
| 교사 피드백이 유의하게 더 효과적이었다 | 학생들은 교사 피드백을 더 유용/개인화된 것으로 평가했다; 전체 ANOVA는 유의하지 않았다 |
| 두 시나리오가 awareness effect를 분리했다 | AI 사용이 비공개인 조건과 학생이 직접 사용하는 조건을 비교했다 |
| AI는 공감/개인화를 재현할 수 없다 | 이 표본의 학생들은 AI 피드백을 교사만큼 개인화·정서적으로 지지적이라고 평가하지 않았다 |
| 가장 이른/최초 연구다 | 이 연구는 Saudi 고급 EFL 과정에서 해당 비교를 제시한다 |
| C2는 near-native다 | 원문은 참여자를 CEFR C2-level로 기술한다 |

이번 대조에서 핵심 수치가 완전히 날조된 사례는 확인되지 않았다. 위험의 중심은 숫자 hallucination보다 **통계적 유의성, 인과성, 일반화 범위를 한 단계씩 강화하는 semantic hallucination**이다.

## 6. llm-wiki 관점의 최종 사용 권고

가장 안전한 제작 조합은 다음과 같다.

1. **본문 서술:** Terra.medium을 기반으로 사용한다.
2. **Quick Card 및 provenance/metadata:** Luna에서 가져오되 외부 메타데이터 출처를 명시한다.
3. **정량 결과 표:** Qwen의 Table 2를 사용하되 인코딩을 복구하고, 원문 표와 다시 대조한다.
4. **Gemini:** 이론·문헌고찰 보충용으로만 사용하고 `significant/effect/cannot/first` 표현을 전부 재검토한다.
5. **Kimi:** 짧은 초기 개요 또는 누락 점검용으로 사용하고, 최종 카드의 근거로는 사용하지 않는다.

canonical ingest 전에 공통으로 해야 할 일:

- registry에서 정확한 `record_id`를 먼저 확정한다. 모델이 임의로 만든 slug를 그대로 쓰지 않는다.
- `test_paper.md`의 원문 source와 실제 PDF 경로를 provenance에 연결한다. 현재 모델 frontmatter의 `inbox/test_paper - <model>.md` 경로는 이 workspace에서 확인되지 않는다.
- `record_id`, `source_path`, `source_hash`, `summary_verified`, `quote_verification_status`를 실제 QC 결과로 채운다. 모델이 자기 자신에게 부여한 verification rate는 증거가 아니다.
- 카드에는 `원문 직접근거`, `원문에 기반한 해석`, `외부 메타데이터`를 구분해 적는다.
- 본문 핵심 문장은 “학생들이 지각했다/보고했다”를 기본 동사로 사용하고, 유의성은 실제 검정이 보고된 경우에만 사용한다.
- 최종 카드의 위키 링크·bibliography key·registry entry는 formal ingest/rebuild 후 QC로 확인한다.

## 7. 평가 범위와 잔여 위험

이번 평가는 현재 제공된 Markdown 원문과 benchmark 산출물의 내용 대조다. PDF 이미지 표의 원본 시각 레이아웃, 외부 DOI 페이지의 독립 확인, 실제 quote verification 로그 생성까지 수행한 것은 아니다. 따라서 이 리포트의 점수는 **모델 선택을 위한 비교 결과**이지, 어느 요약도 자동으로 `summary_verified: true`로 바꾸는 승인 기록이 아니다.

