from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "정보융합학부 테크트리 가이드 API 🗡️"}

class PlayerStats(BaseModel):
    level: str
    weapon: str
    target_class: str

@app.post("/quest")
def get_quest(stats: PlayerStats):
    is_beginner = "초보자" in stats.level
    w = stats.weapon

    if stats.target_class == "AI 마법사":
        if is_beginner:
            quest_name = "[전공선택] AI수학"
            if "C/C++" in w:
                skill_acquired = "수치 계산 & 행렬 연산 구현 능력"
                description = "C/C++의 빠른 연산 능력을 활용해 AI의 뼈대가 되는 수학 마법을 수련합니다. 행렬 곱셈을 직접 구현하며 실력을 쌓아보세요!"
            elif "Java" in w:
                skill_acquired = "객체 기반 수학 라이브러리 활용 능력"
                description = "Java의 객체지향 설계로 수학 연산 구조를 체계적으로 이해합니다. 라이브러리를 직접 설계하며 AI 마법사의 기초를 다져보세요!"
            else:
                skill_acquired = "수식 문서화 & 개념 정리 능력"
                description = "Markdown으로 수식과 개념을 정리하는 습관이 AI 마법사의 첫걸음입니다. 문서화 능력은 나중에 큰 무기가 됩니다!"
        else:
            quest_name = "[전공선택] 머신러닝"
            if "C/C++" in w:
                skill_acquired = "고성능 모델 최적화 & 추론 속도 강화"
                description = "C/C++로 모델의 성능을 극한까지 끌어올립니다. 실무에서 가장 빠른 AI 마법사가 될 수 있습니다!"
            elif "Java" in w:
                skill_acquired = "엔터프라이즈 ML 파이프라인 설계 능력"
                description = "Java 기반 시스템에 머신러닝을 통합하는 능력을 키웁니다. 대규모 서비스에서 빛나는 AI 마법사로 성장하세요!"
            else:
                skill_acquired = "ML 실험 문서화 & 재현성 확보 능력"
                description = "실험 결과를 체계적으로 기록하는 능력은 머신러닝의 핵심입니다. 문서화 마법사에서 AI 마법사로 전직 완료!"

    elif stats.target_class == "백엔드 기사":
        if is_beginner:
            quest_name = "[전공필수] 객체지향프로그래밍"
            if "C/C++" in w:
                skill_acquired = "포인터 & 메모리 관리 기반 설계 능력"
                description = "C/C++의 메모리 개념을 바탕으로 객체지향 설계를 배웁니다. 낮은 레벨부터 이해하는 튼튼한 백엔드 기사가 됩니다!"
            elif "Java" in w:
                skill_acquired = "클래스 설계 & 캡슐화 방어력 증대"
                description = "Java는 객체지향의 정석입니다. 클래스와 인터페이스를 자유자재로 다루는 백엔드 기사로 성장하세요!"
            else:
                skill_acquired = "요구사항 분석 & 설계 문서화 능력"
                description = "Markdown으로 시스템 설계를 문서화하는 능력을 키웁니다. 코드보다 설계가 먼저인 백엔드 기사의 첫걸음!"
        else:
            quest_name = "[전공선택] 데이터베이스"
            if "C/C++" in w:
                skill_acquired = "DB 엔진 내부 구조 & 쿼리 최적화 능력"
                description = "C/C++ 수준의 깊은 이해로 데이터베이스 내부까지 파고듭니다. 쿼리 최적화의 달인 백엔드 기사가 되세요!"
            elif "Java" in w:
                skill_acquired = "JPA & ORM 기반 데이터 모델링 능력"
                description = "Java와 JPA를 활용해 객체와 DB를 자연스럽게 연결합니다. 실무 백엔드 기사의 핵심 스킬입니다!"
            else:
                skill_acquired = "ERD 설계 & 데이터 구조 문서화 능력"
                description = "Markdown으로 ERD와 테이블 구조를 정리하는 능력을 키웁니다. 설계 능력이 뛰어난 백엔드 기사로 성장하세요!"

    else:  # 오픈소스 탐험가
        if is_beginner:
            quest_name = "[전공필수] 오픈소스소프트웨어실습"
            if "C/C++" in w:
                skill_acquired = "C 기반 오픈소스 프로젝트 기여 능력"
                description = "C/C++ 실력으로 Linux 커널급 오픈소스에 도전합니다. 거친 IT 생태계를 정면 돌파하는 탐험가가 되세요!"
            elif "Java" in w:
                skill_acquired = "Java 오픈소스 생태계 기여 & 빌드 자동화"
                description = "Java 기반 오픈소스 프로젝트는 무궁무진합니다. Maven/Gradle로 빌드 자동화까지 마스터하는 탐험가가 되세요!"
            else:
                skill_acquired = "Git & README 문서화 & 커뮤니티 기여 능력"
                description = "Markdown 실력을 살려 오픈소스 문서화에 기여합니다. 좋은 README 하나가 프로젝트를 살립니다!"
        else:
            quest_name = "[전공선택] 컴퓨터네트워크"
            if "C/C++" in w:
                skill_acquired = "소켓 프로그래밍 & 저수준 네트워크 구현"
                description = "C/C++로 소켓을 직접 구현하며 네트워크의 깊은 곳까지 탐험합니다. 진정한 오픈소스 탐험가의 무기입니다!"
            elif "Java" in w:
                skill_acquired = "Java 네트워크 프로그래밍 & 서버 구현"
                description = "Java로 서버와 클라이언트를 직접 구현하며 네트워크를 정복합니다. 백엔드와 네트워크를 동시에 잡는 탐험가가 되세요!"
            else:
                skill_acquired = "네트워크 프로토콜 분석 & 문서화 능력"
                description = "Markdown으로 네트워크 구조와 프로토콜을 정리합니다. 개념을 꿰뚫는 오픈소스 탐험가로 전직 완료!"

    return {
        "quest_name": quest_name,
        "skill_acquired": skill_acquired,
        "description": description
    }