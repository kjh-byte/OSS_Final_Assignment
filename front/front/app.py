import streamlit as st
import requests

API_URL = "http://back:8000/quest"

st.set_page_config(page_title="SW 테크 트리 길라잡이", page_icon="⚔️")

st.title("⚔️ SW 모험가 길드: 전직 퀘스트 안내소")
st.write("환영합니다, 모험가님! 현재 상태와 목표를 알려주시면 다음 수강 퀘스트를 추천해 드립니다.")
st.markdown("---")

st.subheader("🛡️ 모험가의 현재 스탯 설정")
level = st.radio("현재 레벨 (학년)", ["초보자 (1~2학년)", "숙련자 (3~4학년)"])
weapon = st.selectbox("가장 자신 있는 주력 무기", ["C/C++ (전사의 도끼)", "Java (성기사의 방패)", "Markdown (기록자의 깃펜)"])
target_class = st.selectbox("희망 전직 클래스", ["AI 마법사", "백엔드 기사", "오픈소스 탐험가"])

st.markdown("---")

if st.button("📜 전직 퀘스트 발급받기"):
    payload = {
        "level": level,
        "weapon": weapon,
        "target_class": target_class
    }
    
    with st.spinner("길드장이 모험가님에게 맞는 퀘스트를 탐색 중입니다..."):
        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status() 
            
            data = response.json()
            
            st.success("새로운 퀘스트가 도착했습니다!")
            st.markdown(f"> ### 🎯 추천 퀘스트: **{data['quest_name']}**")
            st.markdown(f"**✨ 획득 예정 스킬:** {data['skill_acquired']}")
            st.markdown(f"**📖 길드장의 코멘트:** {data['description']}")
            
            st.balloons()
            
        except requests.exceptions.RequestException:
            st.error("길드 서버와 통신이 끊어졌습니다. 백엔드가 실행 중인지 확인해주세요.")