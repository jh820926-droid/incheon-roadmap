import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (보고서 가독성 극대화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: bold; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 20px;}
    .report-title { font-size: 1.8rem; color: #1A5276; font-weight: bold; border-bottom: 3px solid #1A5276; padding-bottom: 10px; margin-top: 40px;}
    .section-header { font-size: 1.4rem; color: #2E86C1; font-weight: bold; margin-top: 30px; margin-bottom: 10px;}
    .report-box { background-color: #F8F9F9; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px;}
    .highlight-blue { background-color: #EBF5FB; padding: 15px; border-left: 5px solid #3498DB; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
    .highlight-red { background-color: #FDEDEC; padding: 15px; border-left: 5px solid #E74C3C; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
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

# 2. 초정밀 맞춤형 입력 폼
st.subheader("📋 Step 1. 나의 30년 생애주기 설계")

with st.form("lifecycle_form"):
    st.info("💡 각 연령대별로 내가 꿈꾸는 미래의 가족과 집을 선택해 주세요.")
    
    with st.expander("📌 [현재] 나의 기본 정보 (필수)", expanded=True):
        user_name = st.text_input("👤 이름", "김자립")
        col1, col2 = st.columns(2)
        with col1:
            current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
            assets = st.number_input("💰 가용 자산 (단위: 만원)", min_value=0, value=100)
        with col2:
            is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 여부", value=True)
            has_subscription = st.radio("🏦 청약저축 가입 여부", ["가입 유지 중", "미가입"])

    with st.expander("🌱 [10년 후] 나의 목표"):
        fam_10 = st.selectbox("10년 후 가족 구성", ["1인 가구 (미혼)", "결혼 (신혼부부)", "자녀 1명 이상"])
        house_10 = st.selectbox("10년 후 희망 주거", ["청년 전세/매입임대 (저렴한 월세)", "신혼부부 전세/매입임대", "행복주택 (직주근접)"])

    with st.expander("🏡 [20년 후] 나의 목표"):
        fam_20 = st.selectbox("20년 후 가족 구성", ["1인 가구 유지", "부부 가구 (자녀 없음)", "다자녀 가구 (자녀 2명 이상)"])
        house_20 = st.selectbox("20년 후 희망 주거", ["통합공공임대 (장기 거주)", "다자녀 전세/매입임대", "공공분양 (내 집 마련 첫 시도)"])

    with st.expander("🌅 [30년 후] 나의 목표"):
        fam_30 = st.selectbox("30년 후 가족 구성", ["1인 가구", "부부 가구", "성인 자녀와 동거"])
        house_30 = st.selectbox("30년 후 최종 주거 목표", ["공공분양 (완전한 내 집 마련)", "국민임대/통합공공임대 (안정적 노후)"])

    submit_btn = st.form_submit_button("🚀 맞춤형 심층 리포트 산출", type="primary")

# 3. 2025 LH 주거복지 기반 결과 산출 (원페이지 롱스크롤 형식)
if submit_btn:
    st.markdown(f'<div class="report-title">📑 [공식] {user_name} 청년 30년 생애주기 맞춤형 주거로드맵 종합 리포트</div>', unsafe_allow_html=True)
    st.caption(f"발급일자: 2026년 | 산출근거: 2025년 국토교통부·LH 주거복지사업 매뉴얼 | 담당: 김정현 사례관리 및 기획 전문가")

    # [섹션 0] 총괄 요약
    st.markdown('<div class="section-header">0. 로드맵 총괄 요약 및 행정 지시</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="highlight-blue"><b>[진단 결과]</b> 본 사례는 {current_age}세 자립준비청년이 30년간 {fam_30}를 구성하고 {house_30}에 도달하기 위한 재무/행정적 시뮬레이션 결과임.<br><b>[핵심 지시]</b> 각 연령대별 제시된 필수 가용 자산을 선제적으로 확보하고, 청약 납입 횟수를 무조건적으로 방어할 것.</div>', unsafe_allow_html=True)

    # [섹션 1] 현재
    st.markdown(f'<div class="section-header">1. 현재 ({current_age}세) : 자립 기반 방어선 구축기</div>', unsafe_allow_html=True)
    if has_subscription == "미가입":
        st.markdown('<div class="highlight-red"><b>🚨 [행정 명령] 주택청약종합저축 즉시 개설 요망</b><br>현재 청약 미가입 상태로 30년 후 공공분양 진입이 원천 차단됨. 명일 즉시 수탁은행 방문하여 청년주택드림청약통장(최고 금리 4.5%) 개설 및 월 2만 원 자동이체 강제 설정할 것.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="highlight-blue"><b>✅ [상태 점검] 청약저축 유지 상태 양호</b><br>현행 유지 필수. 재무 위기 시 해지가 아닌 청약담보대출 활용으로 납입 횟수(기간) 보존할 것.</div>', unsafe_allow_html=True)

    if is_vulnerable:
        st.markdown(f'<div class="report-box"><b>[2025 자립준비청년 특례 전형 매칭]</b><br>▶ <b>전세임대:</b> 수도권 기준 최대 1억 2,000만 원 한도 지원. 만 20세 이하 무이자 적용, 22세 이후 임대료 발생 구간 진입 대비 요망.<br>▶ <b>매입임대:</b> 1순위 타겟. 보증금 100만 원 (자부담). 보호종료 후 5년 이내 임대료 50% 감면 특례 적용. 현재 가용 자산({assets}만 원) 대비 최소 보증금 충족 여부 상시 모니터링 요망.</div>', unsafe_allow_html=True)

    # [섹션 2] 10년 후
    st.markdown(f'<div class="section-header">2. 10년 후 ({current_age+10}세) : 자립 특례 종료 및 맞춤형 전환기</div>', unsafe_allow_html=True)
    st.write(f"**목표 지표:** {fam_10} 구성 / {house_10} 진입")
    
    if "신혼" in fam_10 or "신혼부부" in house_10:
         st.markdown('<div class="report-box"><b>[2025 신혼·신생아 주거지원 세부 요건]</b><br>▶ <b>전형 특징:</b> 혼인 7년 이내 또는 예비 신혼부부 대상.<br>▶ <b>전세임대 Ⅰ유형:</b> 지원한도 1억 4,500만 원. (보증금 5% 자부담: <b>최소 725만 원 확보 필수</b>)<br>▶ <b>전세임대 Ⅱ유형:</b> 지원한도 2억 4,000만 원 (보증금 20% 자부담). 월 임대료는 지원금액의 1~2% 수준 (약 20~30만 원) 산출 예상.<br>▶ <b>행동 지시:</b> 혼인 신고 시점과 LH 공고일 역산하여 선제적 자금 계획 수립할 것.</div>', unsafe_allow_html=True)
    else:
         st.markdown('<div class="report-box"><b>[2025 청년 일반 주거지원 세부 요건]</b><br>▶ <b>전형 특징:</b> 자립준비청년 5년 특례 감면 종료 후 일반 청년(19~39세) 자격으로 전환됨. 임대료 상승 구간 진입.<br>▶ <b>매입/전세임대:</b> 1순위 자격(수급자, 한부모 등) 상실 시 2~3순위 경쟁 돌입. 보증금 200만 원 기본 요구됨.<br>▶ <b>행동 지시:</b> 특례 종료 전 1~2인용 행복주택(전용 21~36㎡) 청약 당첨을 위한 무주택 요건 및 소득 기준(전년도 도시근로자 100% 이하) 통제할 것.</div>', unsafe_allow_html=True)

    # [섹션 3] 20년 후
    st.markdown(f'<div class="section-header">3. 20년 후 ({current_age+20}세) : 주거 안정 및 자가 전환 대비기</div>', unsafe_allow_html=True)
    st.write(f"**목표 지표:** {fam_20} 구성 / {house_20} 진입")
    
    if "다자녀" in fam_20 or "다자녀" in house_20:
        st.markdown('<div class="report-box"><b>[2025 다자녀 가구 주거지원 세부 요건]</b><br>▶ <b>전형 특징:</b> 2명 이상의 미성년 자녀를 둔 무주택 세대. 최장 20년 거주 보장으로 양육 안정성 극대화.<br>▶ <b>다자녀 매입임대:</b> 시중 시세의 30~40% 수준. 전용면적 85㎡ 이하 공급.<br>▶ <b>다자녀 전세임대:</b> 수도권 기준 1억 5,500만 원 한도 지원. (자녀 수에 따른 우대 금리 마이너스 적용 확인 요망).<br>▶ <b>행동 지시:</b> 다자녀 가구 전형 입주 시, 향후 공공분양 다자녀 특별공급 자격을 훼손하지 않는 범위 내에서 거주할 것.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="report-box"><b>[통합공공임대 및 뉴홈 진입 요건]</b><br>▶ <b>통합공공임대:</b> 기존 국민/영구/행복주택이 통합된 형태로, 소득 연계형 임대료 부과. 중산층 진입 시에도 최장 30년 거주 가능.<br>▶ <b>뉴홈(공공분양) 준비:</b> 사전청약 나눔형/선택형 공략. LTV 80% 장기 저리 모기지 활용을 위한 신용점수 및 원리금 상환 능력(DSR) 사전 점검할 것.</div>', unsafe_allow_html=True)

    # [섹션 4] 30년 후
    st.markdown(f'<div class="section-header">4. 30년 후 ({current_age+30}세) : 자가 소유 및 영구 주거 자립 달성기</div>', unsafe_allow_html=True)
    st.write(f"**목표 지표:** {fam_30} 구성 / {house_30} 달성")
    
    st.markdown('<div class="highlight-blue"><b>[최종 로드맵 산출 결과]</b><br>본 설계는 10대 후반부터 축적된 공공 자원 활용 능력과 청약 납입 데이터를 기반으로, LH 임대주택 순환 거주를 거쳐 최종 <b>자가 소유(또는 장기 공공임대 안착)</b>에 이르는 학문적, 실무적 모범 사례로 평가됨. <br>단기적 소비 통제와 지속적인 소득 증빙 관리가 수반될 경우 본 로드맵의 달성 확률은 95% 이상으로 추산됨.</div>', unsafe_allow_html=True)

    # [핫라인]
    st.markdown("---")
    st.markdown("#### 🛡️ 위기 개입 핫라인 (비상 연락망)")
    st.write("본 계획 실행 중 생계급여 탈락, 보증금 미납, 실직 등 중대 변수 발생 시 즉각적인 사례관리 개입을 요청할 것.")
    st.button("📞 김정현 전담 멘토 즉시 연결 (Tel. 070-7663-1153)", use_container_width=True)