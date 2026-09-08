from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, read_yaml_md, write_yaml_md
from synthesis_map import render_links

WIKI_KO = {
    "2023-09-jeon-lee-eait-chatgpt": ("생성형 AI와 ChatGPT를 영어교육에 도입할 때의 가능성과 교수·학습 설계 쟁점을 정리한 연구입니다.", "ChatGPT는 상호작용과 피드백을 지원할 수 있지만, 정확성·편향·교사 매개가 핵심 조건입니다."),
    "2024-04-lee-jeon-system": ("예비교사의 AI 활용과 교사 역할 변화를 체계적으로 검토한 연구입니다.", "AI는 교사를 대체하기보다 교사의 판단과 설계를 보완하는 방향으로 통합되어야 합니다."),
    "2024-05-jeon-lee-choi-ile": ("언어교육에서 AI 챗봇의 활용 가능성과 학습자 상호작용을 검토한 연구입니다.", "챗봇의 효과는 과업 설계, 피드백의 질, 학습자의 비판적 점검에 좌우됩니다."),
    "2024-05-jeon-lee-eait": ("영어교육에서 AI 도구를 활용하는 방식과 교육적 고려사항을 논의한 연구입니다.", "AI 활용은 학습 기회를 넓히지만 목표·평가·교사 지원과 함께 설계되어야 합니다."),
    "2024-08-jeon-lee-ets": ("영어 학습에서 생성형 AI와 챗봇의 적용을 검토하고 실천적 시사점을 제시한 연구입니다.", "개인화된 연습과 즉각적 상호작용이 장점이지만, 오류 검증과 윤리적 사용이 필요합니다."),
    "2024-09-05-jeon-lee-coronel-molina-elt": ("Global Englishes 관점에서 AI와 영어교육의 관계를 비판적으로 검토한 연구입니다.", "AI 출력은 특정 영어 규범을 재생산할 수 있으므로 다양한 영어와 화자 정체성을 반영해야 합니다."),
    "2024-11-05-lee-jeon-llt": ("언어교사교육에서 생성형 AI의 역할과 교사 전문성의 변화를 논의한 연구입니다.", "교사교육은 도구 사용법을 넘어 AI 결과를 평가하고 교육적으로 재구성하는 역량을 길러야 합니다."),
    "2025-03-lee-jeon-choe-tq": ("3D 메타버스 환경에서 AI 챗봇을 활용해 예비교사의 Global Englishes 인식을 높이는 방안을 탐색한 연구입니다.", "AI 챗봇과 몰입형 과업은 인식 확장을 지원할 수 있으나, 성찰적 안내와 맥락화가 필요합니다."),
    "2025-04-genai-and-agency-eltj": ("생성형 AI 시대의 교사 agency와 교육적 의사결정을 이론적으로 검토한 연구입니다.", "교사 agency는 AI를 수동적으로 수용하는 것이 아니라 목적에 맞게 선택·조정·거부하는 실천으로 나타납니다."),
    "2025-08-29-jeon-et-al-applied-linguistics": ("생성형 AI와 언어교육에서 비판적 문식성의 의미를 종합한 연구입니다.", "학습자는 AI의 출처·편향·대표성·소유권을 검토하고 출력을 맥락에 맞게 재구성해야 합니다."),
    "20250909-seongyong-et-al-aral": ("AI와 Global Englishes를 연결해 언어 다양성과 교육 실천의 쟁점을 검토한 연구입니다.", "AI 기반 언어활동은 표준 영어 중심성을 강화할 수 있으므로 다양한 언어 자원을 의도적으로 포함해야 합니다."),
    "20260115-jeon-et-al-literacy": ("AI 문식성 연구를 검토하고 언어학습 맥락에서 필요한 역량을 정리한 연구입니다.", "AI 문식성은 프롬프트 작성만이 아니라 평가·검증·윤리·전이까지 포함하는 복합적 역량입니다."),
    "20260131-lee-et-al-review-ile": ("언어교육 연구에서 생성형 AI의 활용과 연구 동향을 종합한 문헌고찰입니다.", "연구는 효율성과 개인화를 보고하지만, 장기 학습효과·공정성·교사 역할에 대한 검증은 더 필요합니다."),
    "20260606-lee-jeon-llt": ("언어교실에서 AI 활용과 교사·학습자 상호작용의 변화를 검토한 연구입니다.", "AI는 상호작용을 확장할 수 있지만 교사의 중재와 학습자 주도성이 교육적 성과를 결정합니다."),
    "20260905-lee-et-al-tesol-journal": ("영어교육에서 생성형 AI의 교육적 활용을 비판적으로 종합한 연구입니다.", "효과적인 통합에는 명확한 학습목표, 근거 기반 과업, 결과 검증, 윤리적·포용적 설계가 필요합니다."),
}


WIKI_KO_EXTRA = {
    "2024_Addlesee-Eshghi_You-Have-Interrupted": ("중간 멈춤을 음성비서가 더 잘 복구하도록 점진적 명료화 요청을 적용한 연구이다.", "대화형 복구 파이프라인은 완전한 질문에 가까운 질의응답 성능을 보였고, 예시를 제공할 때 대규모 LLM에서 명료화 요청 생성 능력이 나타났다."),
    "2024_June_How-Do-Ai": ("한국 고객서비스 전화 대화에서 AI 음성비서와 인간 사용자가 상호작용적 역할을 어떻게 구성하는지 분석한 연구이다.", "200개 상호작용에서 키워드 응답이 가장 많았으며, AI의 표준화된 여성 목소리와 존대 표현이 대화의 위치성을 형성했다."),
    "2024_Albert-Hall_Distributed-Agency-Smart": ("스마트 홈케어에서 agency가 사람과 Alexa 및 돌봄 기술 사이의 상호작용으로 분산되는 과정을 분석한 사례연구이다.", "사용자는 Alexa를 통해 공동 돌봄 활동에 적극 참여했고, 돌봄 노동의 분산은 서비스 사용자의 agency를 보호하는 방식으로 조직되었다."),
    "2023_Albert-Hamann-Stokoe_Conversational-User-Interfaces": ("스마트 홈케어의 실제 상호작용에서 대화형 사용자 인터페이스가 인간 돌봄을 확장하지만 대체하지는 못함을 보인 사례연구이다.", "100시간 이상의 녹화에서 180개 CUI 상호작용을 분석했으며, 돌봄 보조자는 사용자의 참여를 위해 다음 행동을 조정했다."),
    "2020_Baidya-Das-Gao_Behavior-Gap-Evaluating": ("복잡한 과업지향 대화에서 zero-shot LLM agent와 인간 전문가의 행동 격차를 평가한 연구이다.", "과업 복잡도가 높아질수록 행동 격차가 커졌고, 이러한 차이는 agent 성능 저하와 관련되었다."),
    "2011_Bangerter-Mayor-Doehler_Reported-Speech-Conversational": ("간호 교대 인계 회의의 이야기에서 직접화법이 수행하는 제도적·상호작용적 기능을 분석한 연구이다.", "직접화법은 비일상적 사건을 극화하고 전문적 판단과 책임성을 드러내며, 이야기의 맥락 제시 뒤에 나타나는 경향을 보였다."),
    "2011_Barraja-Rohan_I-Told-You": ("일본인 영어 학습자의 이야기하기 발달과 L2 상호작용 능력을 5개월 동안 종단적으로 분석한 연구이다.", "학습자의 이야기는 짧은 응답 중심 발화에서 더 길고 복잡한 이야기로 점진적으로 발달했지만 그 과정은 고르지 않았다."),
    "0000_Barthel_Alexa-You-Are": ("자연스러운 인간-음성비서 상호작용에서 응답 시간과 대화 흐름의 관계를 분석한 연구이다.", "1077개 전환에서 음성비서의 응답은 느리고 거의 변하지 않았으며, 백채널과 순차적 민감성이 부족해 대화의 자연스러움이 낮아졌다."),
    "0000_Bozb-y-k-Sert-Bacanak_Veo-Integrated-Imdat_Veo-Integrated-Imdat-Pre-Service": ("VEO 통합 IMDAT가 예비 영어교사의 질문 방식과 교실 상호작용 능력에 미친 변화를 분석한 연구이다.", "질문 유형을 다양화하고 학습자 발화를 확장하면서 학생 참여가 늘었고, 비디오 기반 성찰이 상호작용 능력 발달을 지원했다."),
    "0000_Bozb-y-k-Sert-Bacanak_Veo-Integrated-Imdat-Pre-Service": ("VEO 통합 IMDAT가 예비 영어교사의 질문 방식과 교실 상호작용 능력에 미친 변화를 분석한 연구이다.", "질문 유형을 다양화하고 학습자 발화를 확장하면서 학생 참여가 늘었고, 비디오 기반 성찰이 상호작용 능력 발달을 지원했다."),
    "2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue": ("대화 분석을 바탕으로 음성 사용자 인터페이스의 대화 설계를 개선하는 방법을 제안한 개념적 연구이다.", "스크립트의 구두점은 인간 대화에 없는 멈춤을 만들 수 있었고, SSML을 사용한 턴 설계는 실제 인간 발화에 더 가까워졌다."),
}


WIKI_KO_EXTRA["2024_Ahn-Kim-Lee_How-Do-Ai"] = WIKI_KO_EXTRA["2024_June_How-Do-Ai"]


def wiki_language(root: Path) -> str:
    try:
        config = json.loads((root / "km-config.json").read_text(encoding="utf-8"))
        return str(config.get("wiki_language", "en")).lower()
    except (OSError, ValueError):
        return "en"


def build_wiki(root: Path, card: Path) -> Path:
    data, card_body = read_yaml_md(card)
    stem = data.get("stem") or card.stem
    wiki_path = root / "wiki" / f"{stem}.md"
    wiki_data = {
        "record_id": data.get("record_id", ""),
        "stem": stem,
        "metadata_status": data.get("metadata_status", "open"),
        "citation_key": data.get("citation_key", ""),
    }
    def section(name: str) -> str:
        match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |^# |\Z)", card_body, re.MULTILINE)
        return match.group(1).strip() if match else ""

    one_sentence = section("One-sentence Summary")
    findings = section("Findings")
    labels = ("요약", "핵심 결과", "연결된 종합 페이지", "메모", "관련 종합 페이지", "상세 요약 카드", "전체 추출 원문") if wiki_language(root) == "ko" else ("Summary", "Key Findings", "Synthesis Links", "Notes", "related synthesis", "detailed summary and evidence", "full parsed text")
    if wiki_language(root) == "ko" and stem in (WIKI_KO | WIKI_KO_EXTRA):
        one_sentence, findings = (WIKI_KO | WIKI_KO_EXTRA)[stem]
    synthesis_links = render_links(root, stem, "")
    body = f"""# {data.get("title") or stem}

- Card: [[../cards/{stem}|summary card]]
- Source: [[../sources/{stem}|parsed source]]
- Bibliography key: `@{data.get("citation_key", "")}`
- Metadata status: `{data.get("metadata_status", "open")}`

## {labels[0]}

{one_sentence or "Summary pending."}

## {labels[1]}

{findings or "Findings pending."}

## {labels[2]}

- Card: [[../cards/{stem}|{labels[5]}]]
- Source: [[../sources/{stem}|{labels[6]}]]
{synthesis_links}

## {labels[3]}

{"이 문서는 탐색과 종합을 위한 위키 노드입니다. 상세한 근거와 주장은 영어 카드와 source에서 확인합니다." if wiki_language(root) == "ko" else "This node is a navigation and synthesis layer. Detailed claims belong in the card and source."}
"""
    write_yaml_md(wiki_path, wiki_data, body)
    return wiki_path


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("card")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(build_wiki(root, Path(args.card).resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
