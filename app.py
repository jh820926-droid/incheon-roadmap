import streamlit as st
import pandas as pd

# 1. 앱 기본 설정 (스마트폰 앱처럼 화면을 가운데로 모아줌!)
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# --- CSS 스타일링 (앱에 예쁜 옷을 입히는 코드) ---
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; color: #2C3E50; font-weight: bold; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.2rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .highlight { background-color: #E8F8F5; padding: 20px; border-radius: 10px; border-left: 5px solid #1ABC9C; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)

# 2. 메인 배너 및 제목
st.markdown('<div class="main-title">🏠 인천자립 주거로드맵 플래너</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 30년 주거 안심 플랜을 설계합니다</div>', unsafe_allow_html=True)

# [디자인 핵심] 이미지가 늘어나지 않도록 투명한 여백으로 감싸서 가운데 정렬!
try:
    col_img1, col_img2, col_img3 = st.columns([1, 8, 1]) # 양옆에 1만큼의 여백을 줌
    with col_img2:
        st.image("family_illust.jpg", use_container_width=True) 
except:
    st.info("💡 바탕화면에 'family_illust.jpg' 사진을 저장해보세요!")

st.divider()

# 3. 사용자 데이터 입력부
st.subheader("📋 Step 1. 나의 현재 상태 진단")
col1, col2 = st.columns(2) 

with col1:
    user_name = st.text_input("👤 이름을 입력하세요", "김자립")
    user_age = st.number_input("🎂 현재 나이", min_value=15, max_value=50, value=20)
    user_assets = st.number_input("💰 현재 가용 자산 (단위: 만원)", min_value=0, value=100)

with col2:
    has_subscription = st.radio("🏦 주택청약종합저축 가입 여부", ["가입 완료", "미가입"], horizontal=True)
    future_plan = st.selectbox("👨‍👩‍👧‍👦 향후 10년 내 가족 계획", ["1인 가구 유지", "결혼 및 신혼가구 구성", "다자녀 가구 구성"])
    st.write("") # 버튼 위치 맞추기
    submit_btn = st.button("🚀 나의 주거 로드맵 분석 시작", use_container_width=True, type="primary")

# 4. 로드맵 산출 알고리즘 및 결과 표출부
if submit_btn:
    st.divider()
    st.markdown(f"### ✨ **{user_name}** 청년을 위한 맞춤형 주거 로드맵 결과")
    
    # 생애주기 시각화
    progress_val = int(((user_age - 16) / (47 - 16)) * 100)
    progress_val = max(0, min(100, progress_val))
    st.progress(progress_val)
    st.caption(f"📍 현재 생애주기 진행률: **{user_age}세** 구간 통과 중")

    # 핵심 미션 도출
    if has_subscription == "미가입":
        st.error("🚨 **[긴급 미션]** 주택청약종합저축이 없습니다! 내일 당장 은행에 방문하여 월 2만 원 자동이체를 설정하세요.")
    else:
        st.success("✅ 주택청약종합저축 유지 중! 아주 훌륭한 주거 자립의 첫걸음입니다.")

    # 추천 전형
    st.markdown("#### 🎯 추천 주거 전형 및 필요 자금")
    
    if user_age <= 20:
        st.markdown('<div class="highlight"><b>[소년소녀가정 전형]</b><br>20세까지 LH임대료 이자 없음. 재계약 횟수 제한 없음 (지원한도 1억 3,000만 원)<br>▶ <b>현재 미션:</b> 22세 이후 임대료 지출 시작에 대비하여 기초 자산 형성 시작.</div>', unsafe_allow_html=True)
        
    elif 20 < user_age <= 28 and future_plan == "1인 가구 유지":
        st.markdown('<div class="highlight"><b>[자립준비청년 전형]</b><br>보호종료 후 5년까지 임대료 50% 할인 적용 구간.<br>▶ <b>필요 자금:</b> 임대보증금 100만 원 (자부담)<br>▶ <b>지원 한도:</b> 1억 2,000만 원 / 임대료 약 22만 원 예상</div>', unsafe_allow_html=True)
        if user_assets < 100:
            st.warning(f"⚠️ 현재 가용 자산({user_assets}만 원) 부족. 보증금 100만 원 확보를 위한 단기 적금 즉시 가입 요망.")
            
    elif future_plan == "결혼 및 신혼가구 구성":
        st.markdown('<div class="highlight"><b>[신혼·신생아 가구 전형]</b><br>6세 이하 자녀를 둔 혼인가구 대상. 총 10년 거주 가능.<br>▶ <b>필요 자금:</b> 임대보증금 725만 원 (자부담)<br>▶ <b>지원 한도:</b> 1억 4,500만 원 / 임대료 약 26만 원 예상</div>', unsafe_allow_html=True)
        
    elif future_plan == "다자녀 가구 구성":
        st.markdown('<div class="highlight"><b>[다자녀 가구 전형]</b><br>자녀 2명 이상의 혼인가구. 총 20년 거주 가능.<br>▶ <b>필요 자금:</b> 임대보증금 310만 원 (자부담)<br>▶ <b>지원 한도:</b> 1억 5,500만 원 / 임대료 약 28만 원 예상</div>', unsafe_allow_html=True)

    # 리스크 관리 및 핫라인
    st.divider()
    st.markdown("#### 🛡️ 든든한 지지체계")
    st.info("**위기 발생 시 (수급자 탈락, 임대료 연체 등) 절대 혼자 고민하지 말 것.**")
    st.button("📞 김정현 담당 멘토에게 즉시 연결 (070-7663-1153)", use_container_width=True)