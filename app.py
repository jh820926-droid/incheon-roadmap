import streamlit as st

# 1. 앱 기본 설정 (모바일 친화적 중앙 정렬)
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: bold; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 20px;}
    .report-box { background-color: #F8F9F9; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px;}
    .highlight-blue { background-color: #EBF5FB; padding: 15px; border-left: 5px solid #3498DB; border-radius: 5px; margin-bottom: 15px;}
    .highlight-green { background-color: #E9F7EF; padding: 15px; border-left: 5px solid #27AE60; border-radius: 5px; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2025 인천자립 주거로드맵 플래너</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 선택으로 그리는 30년 맞춤형 주거 안심 플랜</div>', unsafe_allow_html=True)

try:
    col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
    with col_img2:
        st.image("family_illust.jpg", use_container_width=True) 
except:
    pass

st.divider()

# 2. 초정밀 맞춤형 입력 폼 (이탈률 방지를 위한 Form 및 Expander 적용)
st.subheader("📋 Step 1. 나의 30년 생애주기 설계하기")

with st.form("lifecycle_form"):
    st.info("💡 각 연령대별로 내가 꿈꾸는 미래의 가족과 집을 선택해 주세요.")
    
    # [현재]
    with st.expander("📌 [현재] 나의 기본 정보 (필수)", expanded=True):
        user_name = st.text_input("👤 이름", "김자립")
        col1, col2 = st.columns(2)
        with col1:
            current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
            assets = st.number_input("💰 가용 자산 (단위: 만원)", min_value=0, value=100)
        with col2:
            is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 여부", value=True)
            has_subscription = st.radio("🏦 청약저축 가입 여부", ["가입 유지 중", "미가입"])

    # [10년 후]
    with st.expander("🌱 [10년 후] 나의 목표 (20대 후반 ~ 30대)"):
        st.write(f"**{current_age + 10}세의 나는...**")
        fam_10 = st.selectbox("10년 후 가족 구성", ["1인 가구 (미혼)", "결혼 (신혼부부)", "자녀 1명 이상"])
        house_10 = st.selectbox("10년 후 희망 주거 지원", ["청년 전세/매입임대 (저렴한 월세)", "신혼부부 전세/매입임대", "행복주택 (직주근접)"])

    # [20년 후]
    with st.expander("🏡 [20년 후] 나의 목표 (30대 후반 ~ 40대)"):
        st.write(f"**{current_age + 20}세의 나는...**")
        fam_20 = st.selectbox("20년 후 가족 구성", ["1인 가구 유지", "부부 가구 (자녀 없음)", "다자녀 가구 (자녀 2명 이상)"])
        house_20 = st.selectbox("20년 후 희망 주거 지원", ["통합공공임대 (장기 거주)", "다자녀 전세/매입임대", "공공분양 (내 집 마련 첫 시도)"])

    # [30년 후]
    with st.expander("🌅 [30년 후] 나의 목표 (40대 후반 ~ 50대)"):
        st.write(f"**{current_age + 30}세의 나는...**")
        fam_30 = st.selectbox("30년 후 가족 구성", ["1인 가구", "부부 가구", "성인 자녀와 동거"])
        house_30 = st.selectbox("30년 후 최종 주거 목표", ["공공분양 (뉴홈 - 완전한 내 집)", "국민임대/통합공공임대 (안정적 노후 준비)"])

    submit_btn = st.form_submit_button("🚀 초정밀 맞춤형 리포트 추출하기", type="primary")

# 3. 2025 LH 주거복지 기반 결과 산출 로직
if submit_btn:
    st.divider()
    st.markdown(f"## 📑 **{user_name}** 청년을 위한 2025 LH 맞춤형 주거 리포트")
    st.caption("※ 본 리포트는 『2025 한눈에 보는 주거복지사업 안내』 기준을 반영하여 추출되었습니다.")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 총괄 요약", "🚨 현재 (Now)", "🌱 10년 후", "🏡 20년 후", "🌅 30년 후"])
    
    # [Tab 1] 총괄
    with tab1:
        st.markdown("### 📊 30년 생애주기 로드맵 요약")
        st.markdown('<div class="highlight-blue">사용자가 직접 입력한 10년 단위의 가족 구성 및 희망 주거 형태를 LH 2025년 최신 전형과 교차 분석한 결과입니다.</div>', unsafe_allow_html=True)
        st.write(f"- **현재 (자립기반):** 자산 {assets}만 원 / 청약 {has_subscription}")
        st.write(f"- **10년 후 ({current_age+10}세):** {fam_10} / {house_10}")
        st.write(f"- **20년 후 ({current_age+20}세):** {fam_20} / {house_20}")
        st.write(f"- **30년 후 ({current_age+30}세):** {fam_30} / {house_30} 달성")

    # [Tab 2] 현재
    with tab2:
        st.markdown(f"### 🚨 현재 ({current_age}세) : 자립 기반 조성기")
        st.markdown('<div class="report-box"><b>[핵심 미션] 2025년 자립준비청년 주거지원 방어선 구축</b></div>', unsafe_allow_html=True)
        
        if has_subscription == "미가입":
            st.error("⚠️ **[경고] 주택청약종합저축(청년주택드림청약통장) 미가입 상태입니다.**\n\n내일 즉시 은행에 방문하여 가입하세요. 2025년 기준 청년주택드림청약통장은 최대 4.5% 이자율을 제공하며, 향후 30년 후 '공공분양'을 위한 필수 무기입니다.")
        else:
            st.success("✅ **[우수] 청약저축 가입 유지 중입니다.**\n\n현재 상태를 반드시 유지하며, 납입 횟수를 늘리는 것에 집중하세요.")

        if is_vulnerable:
            st.markdown('<div class="highlight-green"><b>💡 2025 자립준비청년 특례 전형 안내</b><br>- <b>자립준비청년 전세임대:</b> 만 20세 이하 무이자, 22세 이후 임대료 발생 (보증금 지원한도: 수도권 1억 2천만 원)<br>- <b>자립준비청년 매입임대:</b> 임대보증금 100만 원 (자부담)으로 입주 가능. 보호종료 후 5년 이내 임대료 50% 감면 혜택 적용.</div>', unsafe_allow_html=True)
            if assets < 100:
                st.warning(f"🚨 현재 가용 자산({assets}만 원)이 매입임대 최소 보증금(100만 원)에 미달합니다. 1순위 타겟으로 단기 자금 확보가 시급합니다.")

    # [Tab 3] 10년 후
    with tab3:
        st.markdown(f"### 🌱 10년 후 ({current_age+10}세) : 주거 독립 및 상향기")
        st.markdown(f'<div class="report-box"><b>[목표] {fam_10} 구성 및 {house_10} 진입</b></div>', unsafe_allow_html=True)
        
        if "신혼" in fam_10 or "신혼부부" in house_10:
            st.markdown('<div class="highlight-blue"><b>💍 2025 신혼·신생아 주거지원 로드맵</b><br>- <b>신혼부부 전세임대 Ⅰ, Ⅱ:</b> 혼인 7년 이내 또는 예비 신혼부부 대상. 지원한도 최대 2억 4천만 원(Ⅱ유형, 수도권 기준).<br>- <b>필요 자금:</b> 전세지원금의 5~20%가 임대보증금(자부담)으로 요구됨. (약 700만 원 ~ 4,000만 원 수준 자산 형성 필요)</div>', unsafe_allow_html=True)
        elif "1인" in fam_10:
            st.markdown('<div class="highlight-blue"><b>🏃‍♂️ 2025 청년 주거지원 로드맵</b><br>- <b>청년 전세/매입임대:</b> 자립준비청년 특례 기간(5년) 종료 후 일반 청년 1~2순위로 전환. <br>- <b>행복주택:</b> 1인 가구 전용 면적(약 21~36㎡) 타겟. 보증금 비율 상향을 통해 월 임대료를 6~10만 원대까지 낮추는 전략 필요.</div>', unsafe_allow_html=True)

    # [Tab 4] 20년 후
    with tab4:
        st.markdown(f"### 🏡 20년 후 ({current_age+20}세) : 주거 안정 및 정착기")
        st.markdown(f'<div class="report-box"><b>[목표] {fam_20} 구성 및 {house_20} 진입</b></div>', unsafe_allow_html=True)
        
        if "다자녀" in fam_20 or "다자녀" in house_20:
            st.markdown('<div class="highlight-green"><b>👶 2025 다자녀 가구 주거지원 로드맵</b><br>- <b>다자녀 전세/매입임대:</b> 미성년 자녀 2명 이상 가구 대상. 최장 20년 거주 보장.<br>- <b>통합공공임대 (다자녀 우선공급):</b> 소득 및 자산 요건(2025년 기준 총자산 약 3억 4,500만 원 이하) 충족 시 넓은 평형(전용 84㎡ 이하) 장기 거주 가능.</div>', unsafe_allow_html=True)
        elif "공공분양" in house_20:
            st.markdown('<div class="highlight-blue"><b>🏗️ 내 집 마련 첫 시도 (공공분양 사전 청약)</b><br>- 현재부터 20년간 납입한 청약통장 활용. 무주택 세대구성원 자격 반드시 유지.<br>- <b>뉴홈(나눔형/선택형):</b> 초기 자본 부담을 줄이고 장기 모기지(대출)를 결합한 전형 집중 공략.</div>', unsafe_allow_html=True)
        else:
            st.info("▶ 1~2인 가구를 위한 통합공공임대 중형 평형에 정착하여 주거비 지출을 소득의 20% 이내로 통제하는 재무 전략 유지.")

    # [Tab 5] 30년 후
    with tab5:
        st.markdown(f"### 🌅 30년 후 ({current_age+30}세) : 주거 자립 완성기")
        st.markdown(f'<div class="report-box"><b>[최종 목표] {fam_30} 구성 및 {house_30} 달성</b></div>', unsafe_allow_html=True)
        
        if "공공분양" in house_30:
            st.success("🎉 **[로드맵 완성] 완전한 내 집 마련 (소유권 확보)**\n\n자립준비청년에서 시작하여, 30년간의 치밀한 청약 납입과 자산 관리를 통해 LH 공공분양 당첨 및 자가 소유를 이뤄내는 완벽한 자립 시나리오입니다.")
        else:
            st.success("🎉 **[로드맵 완성] 완벽한 주거 안전망 정착**\n\n무리한 영끌 대출을 지양하고, 통합공공임대 등을 통해 주거비 부담을 최소화하여 은퇴 후 여유로운 현금흐름을 창출하는 스마트한 자립 시나리오입니다.")

        st.markdown("---")
        st.markdown("#### 🛡️ 위기 개입 및 멘토링 핫라인")
        st.write("본 로드맵을 달성하는 과정에서 예기치 못한 재무적 위기(수급비 탈락, 실직 등)가 발생할 경우, 주저하지 말고 기관으로 연락하여 주거지원 유예 및 대안을 모색하십시오.")
        st.button("📞 김정현 담당 멘토에게 즉시 연결 (070-7663-1153)", use_container_width=True)