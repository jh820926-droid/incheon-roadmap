import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 4px solid #154360; padding-bottom: 10px; margin-top: 40px; margin-bottom: 20px;}
    .section-title { font-size: 1.5rem; color: #2980B9; font-weight: 700; background-color: #EBF5FB; padding: 12px; border-radius: 8px; margin-top: 35px; margin-bottom: 15px;}
    .info-box { background-color: #FDFEFE; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px; line-height: 1.6;}
    .warning-box { background-color: #FDEDEC; padding: 20px; border-radius: 8px; border-left: 6px solid #E74C3C; margin-bottom: 15px; line-height: 1.6;}
    .lh-secret { background-color: #F5EEF8; padding: 20px; border-radius: 8px; border-left: 6px solid #9B59B6; margin-bottom: 15px; line-height: 1.6;}
    .gasan-box { background-color: #E8F8F5; padding: 20px; border-radius: 8px; border-left: 6px solid #1ABC9C; margin-bottom: 15px; line-height: 1.6;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵 시스템</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">LH 실무 데이터 기반 30년 초정밀 주거 안심 플랜</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass

st.divider()

# 2. 고도화된 30년 생애주기 입력 폼
st.subheader("📋 Step 1. 나의 30년 생애주기 및 주거 설계")

fam_options = ["1인 가구 (단독)", "2인 가구 (부부/형제)", "3인 가구 (부부+자녀1)", "4인 이상 가구 (다자녀)"]
house_options = [
    "전세임대 (내가 원하는 민간주택 탐색)", 
    "매입임대 (LH가 매입한 다세대/오피스텔)", 
    "건설임대 (영구/국민/행복 아파트)", 
    "통합공공임대 (소득연계형 장기거주 아파트)", 
    "공공분양 (내 집 마련/자가 소유)"
]

with st.form("lifecycle_form"):
    st.info("💡 시작점인 '현재'부터 30년 후까지, 청약 통장 유지 여부와 희망 주거를 꼼꼼히 설계해 보아요!")
    
    with st.expander("📌 [현재] 기본 정보 및 출발선 설계", expanded=True):
        user_name = st.text_input("👤 성명", "김자립")
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 현재 가용 자산 (단위: 만원)", min_value=0, value=100)
        is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 (우선공급 대상)", value=True)
        
        now_sub = st.radio("현재 주택청약종합저축 상태", ["가입 및 월 납입 중", "미가입 또는 연체 중"])

    with st.expander("🌱 [10년 후] 주거 목표 설계"):
        fam_10 = st.selectbox("10년 후 가구원 수", fam_options, index=0)
        house_10 = st.selectbox("10년 후 희망 전형", house_options, index=1)
        sub_10 = st.checkbox("10년 후에도 청약 통장 납입 유지 여부", value=True)

    with st.expander("🏡 [20년 후] 주거 목표 설계"):
        fam_20 = st.selectbox("20년 후 가구원 수", fam_options, index=1)
        house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
        sub_20 = st.checkbox("20년 후에도 청약 통장 납입 유지 여부", value=True)

    with st.expander("🌅 [30년 후] 영구 자립 목표 설계"):
        fam_30 = st.selectbox("30년 후 가구원 수", fam_options, index=2)
        house_30 = st.selectbox("30년 후 최종 전형", house_options, index=4)
        sub_30 = st.checkbox("30년간 모은 청약 통장으로 공공분양 도전 여부", value=True)

    submit_btn = st.form_submit_button("🚀 전형별 가점 및 공고 분석 리포트 추출", type="primary")

# 3. 분석 알고리즘 (공고 시기 및 가점 획득 전략 이식)
def generate_lh_details(fam, house, sub_status):
    report = ""
    
    # 청약 상태 체크
    if not sub_status:
        report += "<div class='warning-box'><b>🚨 [치명적 리스크] 청약 납입 중단 경고</b><br>청약 납입 중단 시 건설임대 배점(최대 6점) 및 공공분양 자격이 즉시 박탈됨. 예외 없는 월 2만 원 강제 납입 이행 지시.</div>"

    # 전형별 초정밀 디테일 (공고처/시기/가점 전략)
    if "전세임대" in house:
        report += "<div class='info-box'><b>📑 [전세임대] 공고 확인 및 지원 가이드</b><br>▶ <b>공고 확인처:</b> LH청약플러스(apply.lh.or.kr) 및 관할 주민센터.<br>▶ <b>공고 시기:</b> 자립준비청년 전세임대는 <b>'연중 상시'</b> 신청 가능. 일반/신혼 전세임대는 연초(1~2월) 정기 모집 공고 집중.<br>▶ <b>지원 한도:</b> 수도권 기준 최소 1.2억 원. 90% 부채비율 권리분석 통과 매물 한정.</div>"
        report += "<div class='gasan-box'><b>🎯 [가산점 및 합격 전략]</b><br>1. <b>자립준비청년 1순위 특례 방어:</b> 보호종료 후 5년 이내 신청 시 1순위 자격 즉각 부여됨.<br>2. <b>타지역 출신 가점:</b> 부모의 주민등록지와 다른 지역(인천 등)에 거주/재학 중일 경우 가점 2점 획득.<br>3. <b>소득 통제:</b> 본인 소득 유무가 심사 대상이나, 근로장려금 수급 기준(단독가구 총소득 2,200만 원 미만) 수준으로 통제 시 유리함.</div>"
        
    elif "매입임대" in house:
        report += "<div class='info-box'><b>📑 [매입임대] 공고 확인 및 지원 가이드</b><br>▶ <b>공고 확인처:</b> LH청약플러스 앱 內 '임대주택 ➔ 청년/신혼부부 매입임대' 공고문.<br>▶ <b>공고 시기:</b> <b>매 분기별 정기공고 (3, 6, 9, 12월)</b>. 단, 미계약분 발생 시 매주 금요일 수시모집(줍줍) 공고 발생.</div>"
        report += "<div class='gasan-box'><b>🎯 [가점 배점표 분석 및 획득 지시]</b><br>동일 1순위 내 경합 시 아래 배점표에 따라 당락이 결정됨. 철저한 사전 관리 요망.<br>1. <b>인천 연속 거주 기간 (최대 3점):</b> 주소지를 함부로 타 지역으로 옮기지 말고 인천 내 연속 거주(3년 이상) 요건을 방어할 것.<br>2. <b>주택청약 납입 횟수 (최대 3점):</b> 24회(2년) 이상 납입 시 만점(3점) 획득. 절대 해지 불가.<br>3. <b>소득 활동 (최대 2점):</b> 신청 시점 기준 재직증명서 발급 가능한 소득 활동 시 가점 산입.</div>"
        report += "<div class='lh-secret'><b>💡 [LH 기밀 꿀팁] '관심지역 알리미' 및 상호전환</b><br>경쟁률이 수백 대 일에 달하므로, LH청약플러스 앱에서 '인천광역시' 관심지역 알림을 설정하여 수시모집 공고 알람을 확보할 것. 당첨 후 보증금을 100만 원 단위로 추가 납입(상호전환)하여 월 임대료를 6~10만 원 선으로 극한 통제 요망.</div>"
        
    elif "건설임대" in house:
        report += "<div class='info-box'><b>📑 [건설임대: 행복/국민] 공고 확인 및 지원 가이드</b><br>▶ <b>공고 확인처:</b> LH청약플러스, 마이홈포털, iH(인천도시공사) 홈페이지 교차 확인.<br>▶ <b>공고 시기:</b> 신규 단지 준공 1년 전 모집 (수시), 또는 기존 단지 퇴거자 발생 시 '예비입주자 모집 공고' (반기별 정례화).</div>"
        report += "<div class='gasan-box'><b>🎯 [가점 배점표 분석 및 획득 지시]</b><br>국민임대/행복주택은 서류 심사에서 아래 가점이 당락을 좌우함.<br>1. <b>중소기업 재직 가점:</b> 중소기업기본법에 따른 중소기업 근로 기간(최장 5년 이상 시 3점) 획득 요망.<br>2. <b>해당 지역 거주 기간 (최대 3점):</b> 인천광역시 거주 기간이 길수록 압도적 유리.<br>3. <b>청약저축 납입 (최대 6점):</b> 납입금액 무관, '연체 없는 납입 횟수(60회 이상 만점)'가 핵심 무기임.</div>"
        
    elif "통합공공" in house:
        report += f"<div class='info-box'><b>📑 [통합공공임대] 공고 확인 및 지원 가이드</b><br>▶ <b>공고 시기:</b> 2026년 이후 신규 택지구구(검단, 계양 등) 위주로 연중 수시 모집 공고 발령 예상.<br>▶ <b>면적 및 가점:</b> {fam} 맞춤형 면적 배정. 세대원 수가 많을수록, 맞벌이 부부일수록 우선공급 가점 배정에서 유리한 포지션 점유.</div>"
        
    elif "분양" in house:
        report += "<div class='info-box'><b>📑 [공공분양: 뉴홈] 공고 확인 및 지원 가이드</b><br>▶ <b>공고 확인처:</b> 뉴홈 공식 홈페이지(뉴홈.kr) 사전청약 공고문 및 청약Home 앱.<br>▶ <b>공고 시기:</b> 국토부 연간 사전청약 공급 일정표에 따라 분기별(3, 6, 9, 12월) 공고.</div>"
        report += "<div class='gasan-box'><b>🎯 [사전청약 당첨 및 DSR 관리 전략]</b><br>1. <b>납입 인정 금액 (절대 원칙):</b> 분양 당첨은 횟수가 아닌 '총 납입 인정 금액(매월 최대 10만 원까지만 인정)'으로 줄을 세움. 여력이 생기는 즉시 매월 10만 원으로 자동이체 상향 조정 필수.<br>2. <b>특공(특별공급) 공략:</b> 생애최초, 신혼, 다자녀 특별공급 물량 70% 타겟팅.<br>3. <b>DSR 무결점 방어:</b> 분양 당첨 후 정부 모기지 실행 시 대출 한도를 좌우함. 현금서비스 이력 원천 차단 및 1등급 신용 방어 요망.</div>"

    return report

# 4. 리포트 출력부
if submit_btn:
    st.markdown(f'<div class="report-header">📑 [공식 진단서] {user_name} 청년 주거 및 가점 획득 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**발급연도:** 2026년 | **발급기관:** 인천자립지원전담기관")

    # 1. 현재 섹션
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 자립 출발선 진단</div>', unsafe_allow_html=True)
    if now_sub == "미가입 또는 연체 중":
        st.markdown('<div class="warning-box"><b>🚨 [긴급 행정명령] 청년주택드림청약통장 즉시 개설</b><br>건설임대 가점 및 공공분양 진입 불가 상태임. 명일 수탁은행 즉시 방문하여 계좌 개설 및 최소 2만 원 자동이체 강제 설정.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box"><b>✅ [점검결과] 주택청약 유지 양호 (가점 확보 중)</b><br>현재 인천광역시 거주 기간과 함께 매월 납입 횟수가 곧 LH 배점표의 점수로 축적되고 있음. 해지 절대 금지.</div>', unsafe_allow_html=True)
    
    # 10년, 20년, 30년 후 출력
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 타겟 전형 및 가점 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 타겟 전형 및 가점 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 최종 공공분양 및 자가 확보</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    st.markdown('<div class="info-box" style="background-color: #EAECEE; border-left: 6px solid #5D6D7E;"><b>📋 [담당 멘토 (김정현) 최종 행정 지시]</b><br>막연하게 공고를 기다리는 것은 탈락을 의미함. 위 명시된 각 전형별 <b>공고 발생 시기(분기별/상시)</b>를 메모하고, <b>LH 배점표 기준(인천 거주기간, 청약 횟수, 중소기업 재직 등)</b>을 선제적으로 충족하여 서류 심사 만점을 타겟팅할 것. 이를 기계적으로 이행할 경우 완벽한 주거 자립을 보장함.</div>', unsafe_allow_html=True)
    st.divider()