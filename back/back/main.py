from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PlayerStats(BaseModel):
    level: str
    weapon: str
    target_class: str

@app.post("/quest")
def get_quest(stats: PlayerStats):
    quest_name = ""
    skill_acquired = ""
    description = ""

    if stats.target_class == "AI 마법사":
        quest_name = "[전공선택] 인공지능수학"
        skill_acquired = "선형 변환과 정방 행렬 마스터"
        description = f"장착하신 [{stats.weapon}]을(를) 활용해 AI의 뼈대가 되는 수학적 마법을 수련합니다. 훌륭한 AI 마법사가 되기 위한 필수 코스입니다!"
        
    elif stats.target_class == "백엔드 기사":
        quest_name = "[전공필수] 객체지향프로그래밍"
        skill_acquired = "실시간 예약 시스템 구축 방어력 증대"
        description = f"[{stats.weapon}] 스킬을 활용하여 복잡한 시스템을 안전하게 설계하는 훈련을 합니다. 튼튼한 백엔드 기사로 성장할 수 있습니다."
        
    else: 
        quest_name = "[전공필수] 오픈소스소프트웨어실습"
        skill_acquired = "AWS EC2 배포 및 Docker 소환술"
        description = f"[{stats.weapon}]만으로는 거친 IT 생태계를 살아남기 힘듭니다! 클라우드라는 새로운 대륙을 개척하는 방법을 배웁니다."

    return {
        "quest_name": quest_name,
        "skill_acquired": skill_acquired,
        "description": description
    }