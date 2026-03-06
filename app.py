import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (부드럽고 신뢰감 있는 색상 유지)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 4px solid #154360; padding-bottom: 10px; margin-top: 40px; margin-bottom: 20px;}
    .section-title { font-size: 1.4rem; color: #2980B9; font-weight: 700; background-color: #EBF5FB; padding: 12px; border-radius: 8px; margin-top: 35px; margin-bottom: 15px;}
    .info-box { background-color: #FDFEFE; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px; line-height: 1.6;}
    .warning-box { background-color: #FDEDEC; padding: 20px; border-radius: 8px; border-left: 6px solid #E74C3C; margin-bottom: 15px; line-height: 1.6;}
    .lh-secret { background-color: #F5EEF8; padding: 20px; border-radius: 8px; border-left: 6px solid #9B59B6; margin-bottom: 15px; line-height: 1.6;}
    .gasan-box { background-color: #E8F8F5; padding: 20px; border-radius: 8px; border-left: 6px solid #1ABC9C; margin-bottom: 15px; line-height: 1.6;}
    .current-box { background-color: #FEF9E7; padding: 20px; border-radius: 8px; border-left: 6px solid #F1C40F; margin-bottom: 15px; line-height: 1.6;}
    .site-box { background-color: #F4F6F7; padding: 20px; border-radius: 8px; border-left: 6px solid #7F8C8D; margin-bottom: 15px; line-height: 1.6;}
    .contact-box { background-color: #E8F8F5; padding: 25px; border-radius: 10px; text-align: center; border: 2px solid #1ABC9C; margin-top: 40px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵 시스템</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 속도에 맞춰 그리는 30년 맞춤형 주거 플랜</div>', unsafe_allow_html=True)

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
current_house_options = [
    "LH 전세임대 (소년소녀가정 등 전형)",
    "LH 전세/매입임대 (자립준비청년 전형)",
    "일반 무상거주 (시설, 친척집, 지인 등)",
    "일반 민간 임대 (월세/전세)",
    "주거취약계층 (고시원, 여관, 비닐하우스 등)"
]

with st.form("lifecycle_form"):
    st.info("💡 삶의 모습은 언제든 변할 수 있어요. 지금 생각하는 가장 이상적인 모습을 편안하게 선택해 주세요.")
    
    with st.expander("📌 [현재] 기본 정보 및 출발선", expanded=True):
        user_name = st.text_input("👤 성명", "김자립")
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 현재 가용 자산 (단위: 만원)", min_value=0, value=100)
        is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 (우선공급 대상)", value=True)
        
        st.write("---")
        now_house = st.selectbox("🏠 현재 거주 중인 주거 형태", current_house_options)
        now_sub = st.radio("🏦 현재 주택청약종합저축 상태", ["가입 및 월 납입 중", "미가입 또는 연체 중"])

    with st.expander("🌱 [10년 후] 주거 목표"):
        fam_10 = st.selectbox("10년 후 가구원 수", fam_options, index=0)
        house_10 = st.selectbox("10년 후 희망 전형", house_options, index=1)
        sub_10 = st.checkbox("10년 후에도 청약 통장 납입을 꾸준히 유지할 계획인가요?", value=True)

    with st.expander("🏡 [20년 후] 주거 목표"):
        fam_20 = st.selectbox("20년 후 가구원 수", fam_options, index=1)
        house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
        sub_20 = st.checkbox("20년 후에도 청약 통장 납입을 꾸준히 유지할 계획인가요?", value=True)

    with st.expander("🌅 [30년 후] 영구 자립 목표"):
        fam_30 = st.selectbox("30년 후 가구원 수", fam_options, index=2)
        house_30 = st.selectbox("30년 후 최종 전형", house_options, index=4)
        sub_30 = st.checkbox("모아둔 청약 통장으로 공공분양 등에 도전해 보시겠습니까?", value=True)

    submit_btn = st.form_submit_button("🚀 맞춤형 로드맵 리포트 추출하기", type="primary")

# 3. 분석 알고리즘 (부드러운 권고 및 디테일 안내)
def analyze_current_status(age, assets, now_house, now_sub):
    report = ""
    if now_sub == "미가입 또는 연체 중":
        report += "<div class='warning-box'><b>💡 [전문가 조언] 청년주택드림청약통장 가입 권장</b><br>현재 청약통장이 없다면 향후 아파트(건설임대/분양) 입주 시 불리할 수 있음. 여력이 될 때 은행을 방문하여 소액(2만 원)이라도 가입해 두는 것을 적극 권장함.</div>"
    else:
        report += "<div class='info-box'><b>✅ [점검결과] 주택청약 유지 우수</b><br>아주 잘하고 있음! 현재 납입 기간과 횟수가 모두 미래의 소중한 자산이 되므로, 무리하지 않는 선에서 꾸준히 유지하는 것이 좋음.</div>"

    if "소년소녀가정" in now_house:
        report += "<div class='current-box'><b>🎯 [맞춤 제안] 소년소녀가정 전세임대 거주 시</b><br>▶ 만 20세까지 이자가 면제되는 훌륭한 주거 환경임.<br>▶ 만 22세 이후부터는 소정의 임대료(이자)가 발생할 수 있으니, 지금부터 주거비 여유분을 조금씩 저축하여 미래의 독립 자금으로 활용하는 것을 추천함.</div>"
    elif "자립준비청년" in now_house:
        report += "<div class='current-box'><b>🎯 [맞춤 제안] 자립준비청년 전세/매입임대 거주 시</b><br>▶ 보호종료 후 5년 이내 임대료 감면 혜택을 받고 있어 안정적임.<br>▶ 특례 기간이 종료될 무렵 임대료 상승이 있을 수 있으므로, 현재 가용 자산(" + str(assets) + "만 원)을 기반으로 미리 전환보증금 추가 납입 등을 계획해 보는 것이 좋음.</div>"
    elif "무상거주" in now_house:
        report += "<div class='current-box'><b>🎯 [맞춤 제안] 무상거주 (시설/친인척) 시</b><br>▶ 현재 주거비 지출이 없는 시기를 '종잣돈 마련의 골든타임'으로 활용해 볼 것.<br>▶ 향후 독립 시 자립준비청년 1순위 자격을 활용해 안전한 LH 임대주택으로 첫발을 내딛기를 권장함.</div>"
    elif "일반 민간 임대" in now_house:
        report += "<div class='warning-box'><b>💡 [전문가 조언] LH 주거복지 제도로의 전환 검토</b><br>▶ 민간 월세 지출은 장기적인 자산 형성에 부담이 될 수 있음.<br>▶ 본인의 자립준비청년 등 1순위 자격을 활용하여 보증금 부담이 적은 LH 매입/전세임대로 이전하는 것을 담당 멘토와 함께 긍정적으로 검토해 볼 것.</div>"
    elif "주거취약계층" in now_house:
        report += "<div class='warning-box'><b>💡 [전문가 조언] 주거 상향 지원제도 적극 활용</b><br>▶ 현재의 주거 환경이 불편하다면 혼자 고민하지 말고 멘토에게 도움을 요청할 것.<br>▶ '주거취약계층 주거상향 지원사업' 등 안전한 곳으로 이사할 수 있는 다양한 정부 지원이 준비되어 있음.</div>"
    return report

def generate_lh_details(fam, house, sub_status):
    report = ""
    if not sub_status:
        report += "<div class='warning-box'><b>💡 [참고 사항] 청약 납입 중지 시 영향</b><br>개인의 경제적 상황에 따라 납입을 쉴 수는 있으나, 향후 임대주택 및 공공분양 경쟁에서 배점이 낮아질 수 있음을 참고하여 가능하면 유지를 권장함.</div>"

    if "전세임대" in house:
        report += "<div class='info-box'><b>📑 [전세임대] 유연한 활용 가이드</b><br>▶ <b>신청 시기:</b> 자립준비청년 전세임대는 언제든 상시 신청 가능. 일반/신혼 유형은 주로 연초(1~2월)에 공고가 집중됨.<br>▶ <b>지원 내용:</b> 내가 원하는 동네의 집을 고르면 LH가 보증금을 지원해 주는 방식.</div>"
        report += "<div class='gasan-box'><b>🎯 [성공적인 입주 팁]</b><br>1. <b>안전한 집 고르기:</b> 집에 빚이 많으면(부채비율 90% 초과) LH 승인이 나지 않음. 부동산에 처음부터 \"LH 전세가 가능한 안전한 집\"을 찾아달라고 요청할 것.<br>2. <b>가점 관리:</b> 본인의 소득과 재산을 일정 수준 이하로 잘 관리하면 당첨에 훨씬 유리함.</div>"
    elif "매입임대" in house:
        report += "<div class='info-box'><b>📑 [매입임대] 유연한 활용 가이드</b><br>▶ <b>신청 시기:</b> 보통 3, 6, 9, 12월에 정기 모집 공고가 나옴.<br>▶ <b>지원 내용:</b> LH가 튼튼하게 지어진 다세대나 오피스텔을 미리 사두고 저렴하게 빌려주는 방식이라 전세사기 걱정이 없음.</div>"
        report += "<div class='gasan-box'><b>🎯 [성공적인 입주 팁]</b><br>1. <b>수시모집(줍줍) 노리기:</b> 빈집이 생기면 수시로 공고가 올라옴. LH청약플러스 앱에서 '관심지역 알림'을 켜두면 남들보다 빨리 정보를 얻을 수 있음.<br>2. <b>지역 거주 및 청약 가점:</b> 인천에 오래 살았거나 청약통장을 연체 없이 꾸준히 냈다면 가산점을 받아 당첨 확률이 매우 높아짐.</div>"
    elif "건설임대" in house:
        report += "<div class='info-box'><b>📑 [건설임대: 행복/국민] 유연한 활용 가이드</b><br>▶ <b>신청 시기:</b> 새 아파트는 지어지기 약 1년 전에 공고가 나며, 기존 아파트는 예비입주자를 수시로 모집함.<br>▶ <b>지원 내용:</b> " + fam + "에 맞는 평형의 아파트에 저렴하게 입주하여 단지 내 쾌적한 환경을 누릴 수 있음.</div>"
        report += "<div class='gasan-box'><b>🎯 [성공적인 입주 팁]</b><br>1. 아파트 입주는 인기가 많아 점수 경쟁이 치열함. <b>청약저축 연체 없는 납입 횟수</b>와 <b>해당 지역(인천) 거주 기간</b>이 당첨을 좌우하는 핵심 열쇠임.</div>"
    elif "통합공공" in house:
        report += f"<div class='info-box'><b>📑 [통합공공임대] 유연한 활용 가이드</b><br>▶ <b>신청 시기:</b> 신규 택지지구를 중심으로 수시 공고 예정.<br>▶ <b>지원 내용:</b> 나중에 소득이 좀 오르더라도 쫓겨나지 않고 내 소득에 맞춰 임대료를 내며 최장 30년까지 편안하게 살 수 있는 진화된 아파트 전형임.</div>"
    elif "분양" in house:
        report += "<div class='info-box'><b>📑 [공공분양: 뉴홈] 내 집 마련 가이드</b><br>▶ <b>신청 시기:</b> 분기별 사전청약 일정에 따라 진행됨.<br>▶ <b>지원 내용:</b> " + fam + " 상황에 맞춰 특별공급(생애최초, 신혼, 다자녀 등)을 활용하면 시세보다 저렴하게 진짜 내 집을 가질 수 있음.</div>"
        report += "<div class='lh-secret'><b>💡 [LH 기밀 꿀팁] 청약통장 활용과 신용 관리</b><br>분양 당첨은 청약통장에 '매월 10만 원씩 꾸준히 인정받은 금액'이 많을수록 유리함. 또한 당첨 후 원활한 대출을 위해 휴대폰 요금 연체나 카드론 사용 등을 피하고 깨끗한 신용점수를 유지하는 것이 중요함.</div>"
    return report

# 4. 리포트 출력부
if submit_btn:
    st.markdown(f'<div class="report-header">📑 {user_name} 청년의 속도에 맞춘 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 1. 현재 
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 확인하기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current_status(current_age, assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 10년, 20년, 30년
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 안정적인 주거 자립</div>', unsafe_allow_html=True)
    st.markdown(generate_lh_details(fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # 5. 필수 사이트 안내 (신규 추가)
    st.markdown('<div class="section-title">5. 든든한 주거복지 정보망 (도움받는 곳)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='site-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr/)</b><br>
        - <b>어떤 도움인가요?</b> 실제 임대주택 및 분양 공고문을 확인하고, 청약을 신청하는 공식 사이트입니다.<br>
        - <b>활용 팁:</b> 앱을 다운로드하여 '관심지역(인천광역시) 알리미'를 설정해 두면 수시로 뜨는 줍줍 공고를 놓치지 않을 수 있어요.
        <br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr/)</b><br>
        - <b>어떤 도움인가요?</b> 전국 모든 종류의 주거복지 제도를 한눈에 검색하고, 내 조건에 맞는 혜택을 찾아주는 길잡이 사이트입니다.<br>
        - <b>활용 팁:</b> '자가진단' 메뉴를 통해 내가 어떤 전형에 유리한지 미리 테스트해 볼 수 있습니다.
        <br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr/)</b><br>
        - <b>어떤 도움인가요?</b> 자립준비청년만을 위해 마련된 전용 정보 포털로 주거, 금융, 취업 정보를 통합 제공합니다.
        <br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr/)</b><br>
        - <b>어떤 도움인가요?</b> 청년전용 버팀목 전세자금 등 이자가 매우 싼 국가 대출 상품들을 안내해 줍니다.
        </div>
    """, unsafe_allow_html=True)

    # 6. 담당자 연락처 (신규 추가)
    st.markdown(f"""
        <div class='contact-box'>
            <h3 style="color: #16A085; margin-bottom: 5px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.1rem; margin-bottom: 0px;">
                사람마다 처한 상황이 다르고, 계획은 언제든 변할 수 있습니다.<br>
                로드맵을 보다가 추가적인 설명이 필요하거나, 나에게 맞는 계획으로 수정하고 싶다면 혼자 고민하지 말고 멘토에게 연락 주세요. 당신의 든든한 내 편이 되어 함께 길을 찾겠습니다.
            </p>
            <hr style="border: 1px solid #1ABC9C; width: 50%; margin: 15px auto;">
            <p style="font-size: 1.2rem; font-weight: bold; color: #2C3E50; margin-bottom: 0px;">
                👤 담당 멘토: 김정현<br>
                ☎️ 직통 번호: 070-7663-1153
            </p>
        </div>
    """, unsafe_allow_html=True)