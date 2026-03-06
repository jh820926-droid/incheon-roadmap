import streamlit as st
import pandas as pd

# 1. 앱 기본 설정
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; color: #2C3E50; font-weight: bold; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.2rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .highlight { background-color: #E8F8F5; padding: 20px; border-radius: 10px; border-left: 5px solid #1ABC9C; margin-bottom: 15px;}
    .report-box { background-color: #F8F9F9; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 인천자립 주거로드맵 플래너</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 30년 주거 안심 플랜을 설계합니다</div>', unsafe_allow_html=True)

try:
    col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
    with col_img2:
        st.image("family_illust.jpg", use_container_width=True) 
except:
    pass

st.divider()

# 2. 사용자 데이터 입력부
st.subheader("📋 Step 1. 나의 현재 상태 진단")
col1, col2 = st.columns(2) 

with col1:
    user_name = st.text_input("👤 이름을 입력하세요", "김자립")
    user_age = st.number_input("🎂 현재 나이", min_value=15, max_value=50, value=20)
    user_assets = st.number_input("💰 현재 가용 자산 (단위: 만원)", min_value=0, value=100)

with col2:
    has_subscription = st.radio("🏦 주택청약종합저축 가입 여부", ["가입 완료", "미가입"], horizontal=True)
    future_plan = st.selectbox("👨‍👩‍👧‍👦 향후 10년 내 가족 계획", ["1인 가구 유지", "결혼 및 신혼가구 구성", "다자녀 가구 구성"])
    st.write("") 
    submit_btn = st.button("🚀 30년 생애주기 리포트 생성", use_container_width=True, type="primary")

# 3. 3~5페이지 분량 종합 리포트 생성 로직
if submit_btn:
    st.divider()
    st.markdown(f"## 📑 **{user_name}** 청년을 위한 30년 주거 안심 리포트")
    st.caption("아래 탭(Tab)을 눌러 현재부터 30년 후까지의 상세 로드맵을 확인하세요.")
    
    # 5개의 페이지(Tab) 생성
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 총괄 요약", "🚨 현재 (Now)", "🌱 10년 후", "🏡 20년 후", "🌅 30년 후"])
    
    # [페이지 1] 총괄 요약
    with tab1:
        st.markdown("### 📊 생애주기 주거 로드맵 요약표")
        st.markdown('<div class="highlight">이 리포트는 인천자립지원전담기관의 실제 지원 사례와 LH 주거복지 제도를 기반으로 작성된 맞춤형 시뮬레이션입니다.</div>', unsafe_allow_html=True)
        
        progress_val = int(((user_age - 16) / (47 - 16)) * 100)
        progress_val = max(0, min(100, progress_val))
        st.progress(progress_val)
        st.caption(f"📍 현재 귀하의 생애주기 진행률: **{user_age}세** 구간 통과 중")
        
        st.write(f"▶ **최종 목표:** {future_plan}에 맞춘 안정적 주거 확보 및 청약을 통한 내 집 마련")
        if has_subscription == "미가입":
             st.error("⚠️ **진단 결과:** 주거 자립의 기초 뼈대인 '주택청약'이 누락되어 있어 긴급 보완이 필요함.")

    # [페이지 2] 현재
    with tab2:
        st.markdown(f"### 🚨 현재 ({user_age}세) : 자립 기반 조성기")
        st.markdown('<div class="report-box"><b>핵심 미션: 초기 자본 형성 및 주거 안전망 진입</b></div>', unsafe_allow_html=True)
        
        if has_subscription == "미가입":
            st.warning("1️⃣ **내일 당장 은행 방문:** 주택청약종합저축 개설 (월 2만 원 자동이체 필수 설정)")
        else:
            st.success("1️⃣ **청약 유지:** 현재 납입 중인 청약통장 절대 해지 금지. (급전 필요 시 청약 예금 담보대출 활용할 것)")
            
        if user_assets < 100:
            st.error(f"2️⃣ **긴급 자본 형성:** 현재 가용 자산({user_assets}만 원)으로는 LH 최소 보증금(100만 원) 충당 불가. 청년도약계좌 등 가입을 통해 6개월 내 100만 원 확보 요망.")
        else:
            st.info(f"2️⃣ **자본 관리:** 확보된 자산({user_assets}만 원)은 자립준비청년 매입/전세임대 보증금으로 방어할 것.")

    # [페이지 3] 10년 후
    with tab3:
        target_age_10 = user_age + 10
        st.markdown(f"### 🌱 10년 후 ({target_age_10}세) : 주거 독립 및 상향기")
        st.markdown('<div class="report-box"><b>핵심 미션: 자립준비청년 특례 할인율 종료 대비 및 맞춤형 전형 전환</b></div>', unsafe_allow_html=True)
        st.write("▶ 보호종료 5년 경과 시점부터 임대료 50% 감면 혜택이 종료됨에 유의할 것.")
        
        if future_plan == "1인 가구 유지":
            st.info("▶ **추천 전형:** 청년 매입임대 또는 전세임대 (2순위/3순위 자격 요건 사전 관리)")
            st.write("▶ **예상 필요 자산:** 임대보증금 200만 원 확보 필요.")
        else:
            st.info("▶ **추천 전형:** 신혼부부 전세임대 Ⅰ, Ⅱ 유형 탐색 시작 (혼인 신고 및 자녀 계획과 연계)")

    # [페이지 4] 20년 후
    with tab4:
        target_age_20 = user_age + 20
        st.markdown(f"### 🏡 20년 후 ({target_age_20}세) : 주거 안정 및 정착기")
        st.markdown('<div class="report-box"><b>핵심 미션: 장기 거주용 임대주택 정착 또는 공공분양 1차 시도</b></div>', unsafe_allow_html=True)
        
        if future_plan == "결혼 및 신혼가구 구성":
            st.success("▶ **추천 전형:** 신혼·신생아 가구 전형 (최장 10년 거주 가능)")
            st.write("▶ **예상 필요 자산:** 임대보증금 725만 원 이상 (자녀 수에 따른 가점 관리 필수)")
        elif future_plan == "다자녀 가구 구성":
            st.success("▶ **추천 전형:** 다자녀 가구 전형 (최장 20년 거주 가능)")
            st.write("▶ **예상 필요 자산:** 임대보증금 310만 원 이상 (다자녀 우대 금리 대출 활용)")
        else:
            st.success("▶ **추천 전형:** 통합공공임대주택 1인 가구 소형 평형 (장기 거주 목적)")

    # [페이지 5] 30년 후
    with tab5:
        target_age_30 = user_age + 30
        st.markdown(f"### 🌅 30년 후 ({target_age_30}세) : 완전한 주거 자립 완성기")
        st.markdown('<div class="report-box"><b>핵심 미션: 30년간 납입한 청약통장을 활용한 내 집 마련 (공공분양)</b></div>', unsafe_allow_html=True)
        st.write("▶ 16세부터 유지해 온 청약통장의 납입 횟수와 금액이 최고 가점에 도달하는 시점.")
        st.write("▶ LH 및 SH 공공분양(사전청약 포함)에 적극 지원하여 소유권 이전 형태의 완전한 자립 완성.")
        st.info("💡 **멘토의 조언:** 여기까지 포기하지 않고 계획대로 달려온 당신의 삶을 진심으로 응원합니다. 당신은 이미 훌륭하게 자립했습니다.")

    # 4. 리스크 관리 핫라인
    st.divider()
    st.markdown("#### 🛡️ 위기 개입 핫라인")
    st.button("📞 김정현 담당 멘토에게 즉시 연결 (070-7663-1153)", use_container_width=True)