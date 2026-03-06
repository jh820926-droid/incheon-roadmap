import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (공문서 및 전문 보고서 스타일 극대화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #1C2833; font-weight: 900; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #566573; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 4px solid #154360; padding-bottom: 10px; margin-top: 40px; margin-bottom: 20px;}
    .section-title { font-size: 1.4rem; color: #1A5276; font-weight: 700; background-color: #EBF5FB; padding: 10px; border-left: 6px solid #2980B9; margin-top: 30px; margin-bottom: 15px;}
    .info-box { background-color: #F8F9F9; padding: 18px; border-radius: 5px; border: 1px solid #BDC3C7; margin-bottom: 15px;}
    .warning-box { background-color: #FDEDEC; padding: 18px; border-radius: 5px; border-left: 5px solid #C0392B; margin-bottom: 15px;}
    .tip-box { background-color: #FCF3CF; padding: 18px; border-radius: 5px; border-left: 5px solid #F1C40F; margin-bottom: 15px;}
    .link-box { background-color: #EAECEE; padding: 15px; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2025 인천자립 주거로드맵 시스템</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">데이터 기반 30년 생애주기 맞춤형 주거 안심 플랜</div>', unsafe_allow_html=True)

try:
    col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
    with col_img2:
        st.image("family_illust.jpg", use_container_width=True) 
except:
    pass

st.divider()

# 2. 초정밀 맞춤형 입력 폼
st.subheader("📋 Step 1. 생애주기 목표 설정")

with st.form("lifecycle_form"):
    st.info("💡 각 연령대별로 내가 꿈꾸는 미래의 가족과 집을 선택해 주세요.")
    
    with st.expander("📌 [현재] 기본 정보 (필수)", expanded=True):
        user_name = st.text_input("👤 성명", "김자립")
        col1, col2 = st.columns(2)
        with col1:
            current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
            assets = st.number_input("💰 가용 자산 (단위: 만원)", min_value=0, value=100)
        with col2:
            is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 여부", value=True)
            has_subscription = st.radio("🏦 청약저축 가입 여부", ["가입 유지 중", "미가입"])

    with st.expander("🌱 [10년 후] 주거 목표"):
        fam_10 = st.selectbox("가족 구성", ["1인 가구 (미혼)", "결혼 (신혼부부)", "자녀 1명 이상"])
        house_10 = st.selectbox("희망 주거 전형", ["청년 전세/매입임대 (저렴한 월세)", "신혼부부 전세/매입임대", "행복주택 (직주근접)"])

    with st.expander("🏡 [20년 후] 주거 목표"):
        fam_20 = st.selectbox("가족 구성", ["1인 가구 유지", "부부 가구 (자녀 없음)", "다자녀 가구 (자녀 2명 이상)"])
        house_20 = st.selectbox("희망 주거 전형", ["통합공공임대 (장기 거주)", "다자녀 전세/매입임대", "공공분양 (내 집 마련 첫 시도)"])

    with st.expander("🌅 [30년 후] 주거 목표"):
        fam_30 = st.selectbox("가족 구성", ["1인 가구", "부부 가구", "성인 자녀와 동거"])
        house_30 = st.selectbox("최종 주거 목표", ["공공분양 (뉴홈 - 완전한 내 집 마련)", "국민임대/통합공공임대 (안정적 노후)"])

    submit_btn = st.form_submit_button("🚀 30년 심층 주거 리포트 추출", type="primary")

# 3. 2025 LH 주거복지 기반 결과 산출 (초정밀 원페이지 롱스크롤)
if submit_btn:
    st.markdown(f'<div class="report-header">📑 [종합 진단서] {user_name} 청년 30년 생애주기 주거 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**발급기관:** 인천자립지원전담기관 | **산출근거:** 2025년 국토교통부·LH 주거복지 매뉴얼")

    # [섹션 0] 총괄
    st.markdown('<div class="section-title">0. 총괄 요약 및 재무 지시</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-box"><b>[진단 개요]</b> 본 보고서는 {current_age}세 자립준비청년이 향후 30년간 {fam_30}를 구성하고 {house_30}에 도달하기 위한 재무적/행정적 최적 경로를 산출한 결과임.<br><b>[핵심 과업]</b> 각 구간별 LH 임대주택 보증금 최소액을 선제 방어하고, 주택청약종합저축 납입 횟수를 무조건적으로 보존하여 최종 공공분양 자격을 획득할 것.</div>', unsafe_allow_html=True)

    # [섹션 1] 현재
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 자립 기반 및 안전망 구축기</div>', unsafe_allow_html=True)
    
    if has_subscription == "미가입":
        st.markdown('<div class="warning-box"><b>🚨 [긴급 행정명령] 청년주택드림청약통장 즉시 개설</b><br>현재 미가입 상태로 방치할 경우 30년 후 내 집 마련(공공분양) 경로가 원천 차단됨. 명일 즉시 수탁은행에 방문하여 월 2만 원~10만 원 구간 자동이체 설정 필수. (2025년 기준 최대 4.5% 우대금리 적용)</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box"><b>✅ [상태 점검] 청약저축 납입 유지 양호</b><br>공공분양 타겟 시 가입 기간과 납입 횟수가 절대적 기준임. 급전 필요 시 해지가 아닌 \'청약예금 담보대출\'을 활용하여 계좌 생명력을 유지할 것.</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="info-box"><b>📌 [필수 확인] 2025 자립준비청년 주거 특례</b><br>▶ <b>전세임대:</b> 수도권 기준 1억 2,000만 원 한도. 만 20세 이하 무이자, 22세 이후 임대료 발생 구간 대비.<br>▶ <b>매입임대:</b> 1순위 타겟. 임대보증금 100만 원(자부담). 보호종료 후 5년 이내 임대료 50% 감면 혜택.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="tip-box"><b>💡 [전략 꿀팁] 초기 자산 형성 극대화</b><br>- <b>자립정착금 및 수당 방어:</b> 지급받은 자립정착금은 절대 소비성 지출로 낭비하지 말고 임대주택 보증금(최소 100만 원~200만 원)으로 묶어둘 것.<br>- <b>청년도약계좌 가입:</b> 매월 일정 금액을 강제 저축하여 정부 기여금을 확보하고, 10년 후 상향 이동을 위한 목돈(최소 2,000만 원 이상)으로 양생할 것.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="link-box"><b>🔗 [공식 참고 사이트]</b><br>1. 자립정보ON (자립준비청년 통합 정보): https://jaripon.ncrc.or.kr/<br>2. 마이홈포털 (전국 임대주택 공고 확인): https://www.myhome.go.kr/<br>3. 복지로 (맞춤형 급여 안내): https://www.bokjiro.go.kr/</div>', unsafe_allow_html=True)

    # [섹션 2] 10년 후
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) : 자립 특례 종료 및 주거 상향기</div>', unsafe_allow_html=True)
    st.write(f"▶ **10년 후 목표 지표:** {fam_10} 구성 / {house_10} 진입")
    
    if "신혼" in fam_10 or "신혼부부" in house_10:
         st.markdown('<div class="info-box"><b>📌 [필수 확인] 2025 신혼·신생아 주거지원 전형</b><br>▶ 혼인 7년 이내 또는 예비 신혼부부 자격 획득 필수.<br>▶ <b>전세임대 Ⅰ유형:</b> 지원한도 1억 4,500만 원 (보증금 5% 자부담 = 최소 725만 원 확보 필수).<br>▶ <b>전세임대 Ⅱ유형:</b> 지원한도 최대 2억 4,000만 원 (보증금 20% 자부담). 월 임대료는 지원금액의 1~2% 수준 부과.</div>', unsafe_allow_html=True)
         st.markdown('<div class="tip-box"><b>💡 [전략 꿀팁] 혼인 신고 타이밍 설계</b><br>- LH 신혼부부 공고일과 혼인 신고일, 임신/출산 예정일을 역산하여 가장 가점이 높은 시점에 청약을 시도할 것.<br>- <b>버팀목 전세자금대출:</b> 임대주택 낙첨 시, HUG(주택도시보증공사) 신혼부부 전용 전세자금대출(최저 금리 연 1%대)로 민간 전세시장 진입 우회 전략 수립.</div>', unsafe_allow_html=True)
    else:
         st.markdown('<div class="info-box"><b>📌 [필수 확인] 2025 일반 청년 주거지원 전형</b><br>▶ 자립준비청년 5년 특례 감면 종료. 일반 청년(19~39세) 1순위(수급자) 또는 2~3순위 자격으로 전환됨.<br>▶ <b>행복주택:</b> 1~2인용 전용면적(21~36㎡) 타겟. 보증금을 최대치로 전환하여 월 임대료를 6~10만 원대까지 낮추는 전환보증금 제도 적극 활용 요망.</div>', unsafe_allow_html=True)
         st.markdown('<div class="tip-box"><b>💡 [전략 꿀팁] 소득 요건 및 주거비 통제</b><br>- 근로 소득 발생 시 전년도 도시근로자 가구당 월평균 소득의 100% 이하 요건 충족 여부 상시 모니터링.<br>- <b>중소기업취업청년 전월세보증금대출:</b> 중소기업 재직 시 1.2% 고정금리로 최대 1억 원 대출 가능. 월 이자 10만 원 수준으로 주거비 방어 가능.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="link-box"><b>🔗 [공식 참고 사이트]</b><br>1. LH 청약플러스 (사전청약 및 임대 공고 신청): https://apply.lh.or.kr/<br>2. 주택도시기금 (청년/신혼 전월세 대출 상품 안내): https://nhuf.molit.go.kr/</div>', unsafe_allow_html=True)

    # [섹션 3] 20년 후
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) : 주거 안정 정착 및 자가 전환 대비기</div>', unsafe_allow_html=True)
    st.write(f"▶ **20년 후 목표 지표:** {fam_20} 구성 / {house_20} 진입")
    
    if "다자녀" in fam_20 or "다자녀" in house_20:
        st.markdown('<div class="info-box"><b>📌 [필수 확인] 2025 다자녀 가구 주거지원</b><br>▶ 미성년 자녀 2명 이상 양육 시 최장 20년 거주 보장 전형 진입 가능.<br>▶ <b>다자녀 매입임대:</b> 시중 전세가 대비 30~40% 수준으로 전용면적 85㎡ 이하 넓은 평형 공급.<br>▶ <b>다자녀 전세임대:</b> 수도권 기준 1억 5,500만 원 한도. 자녀 수에 따른 우대 금리(마이너스 금리) 적용 확인 필수.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box"><b>📌 [필수 확인] 통합공공임대 및 뉴홈(사전청약) 진입</b><br>▶ <b>통합공공임대:</b> 기존 국민/영구 임대주택이 통합된 형태. 가구원 수에 따른 적정 면적 배정 및 소득 연계형 임대료 부과. 중산층 진입 시에도 최장 30년 거주 가능.</div>', unsafe_allow_html=True)

    st.markdown('<div class="tip-box"><b>💡 [전략 꿀팁] 무주택 세대구성원 유지 및 DSR 관리</b><br>- <b>분양권 주의:</b> 섣부른 오피스텔 분양이나 지분 소유는 무주택 요건을 파괴하므로 절대 금물.<br>- <b>신용 점수 및 대출 한도:</b> 향후 자가 마련을 위한 LTV 80% 모기지 대출을 받기 위해, 신용카드 할부 및 현금서비스 사용을 엄격히 통제하고 1등급 신용 유지할 것.</div>', unsafe_allow_html=True)

    # [섹션 4] 30년 후
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) : 영구 자립 및 내 집 마련 완성기</div>', unsafe_allow_html=True)
    st.write(f"▶ **최종 로드맵 목표:** {fam_30} 구성 / {house_30} 달성")
    
    st.markdown('<div class="info-box"><b>📌 [최종 점검] 공공분양 (뉴홈) 자격 획득 및 소유권 이전</b><br>▶ 10대 후반부터 30년간 단 한 번의 해지 없이 납입한 주택청약종합저축 통장을 발동할 시점임.<br>▶ <b>나눔형/선택형 공공분양:</b> 시세의 70% 이하 분양가 및 초저리 장기 모기지 결합 상품 집중 공략.<br>▶ <b>생애최초 특별공급:</b> 혼인 및 자녀 요건(또는 1인 가구 특례)을 활용하여 추첨제 물량 적극 지원할 것.</div>', unsafe_allow_html=True)

    st.markdown('<div class="warning-box"><b>🎯 [사례관리자 종합 소견]</b><br>본 로드맵은 인천자립지원전담기관의 행정 데이터와 국가 주거복지 체계를 결합한 최상위 수준의 자립 시나리오임. 단기적 소비 충동을 통제하고 본 시나리오에 명시된 자산 형성(청약, 도약계좌 등)을 기계적으로 이행할 경우, 빈곤의 대물림을 끊어내고 완벽한 자가 소유 및 경제적 독립을 달성할 확률이 매우 높음. <b>흔들림 없이 이 길을 걸어가기를 강력히 권고함.</b></div>', unsafe_allow_html=True)

    st.markdown('<div class="link-box"><b>🔗 [공식 참고 사이트]</b><br>1. 뉴홈 (공공분양 50만 호 공식 안내): https://뉴홈.kr/<br>2. 한국부동산원 청약Home (민간/공공 청약 통합): https://www.applyhome.co.kr/</div>', unsafe_allow_html=True)

    # 하단 마무리
    st.divider()
    st.caption("본 리포트는 개인의 재무/행정 상황을 시뮬레이션 한 것으로, 실제 정책 변경에 따라 변동될 수 있습니다. 위기 발생 시 사례관리 기관과 긴밀히 협조하십시오.")