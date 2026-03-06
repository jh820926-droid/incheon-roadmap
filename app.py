import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정 (수식 오류 방지를 위해 기호 사용 최적화)
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (인쇄 시 스크롤 잘림 방지 및 가독성 극대화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    /* 가독성 중심 카드 디자인 */
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    .action-box { background-color: #F4F9FF; padding: 20px; border-radius: 10px; border-left: 5px solid #3498DB; margin: 15px 0;}
    .tip-box { background-color: #FFF9E6; padding: 22px; border-radius: 10px; border-left: 5px solid #F1C40F; margin: 15px 0; color: #4D5656;}
    
    /* 인쇄용 특수 설정 */
    @media print {
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"] {
            height: auto !important; overflow: visible !important; display: block !important; background-color: white !important;
        }
        .page-break { page-break-before: always !important; display: block !important; height: 0px !important; }
        * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 성장에 맞춰 설계하는 30년 주거 안심 백과사전</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass
st.divider()

# 2. 30년 생애주기 입력 폼
st.subheader("📋 Step 1. 나의 30년 주거 자립 계획")

fam_options = ["1인 가구 (혼자 생활)", "2인 가구 (부부/형제)", "3인 가구 (부부+자녀1)", "4인 이상 (다자녀 가정)"]
house_options = [
    "전세임대 (내가 고른 민간주택 지원)", 
    "매입임대 (LH가 매입한 안심주택)", 
    "건설임대 (국민/행복 아파트)", 
    "통합공공임대 (최장 30년 거주 아파트)", 
    "공공분양 (자가 소유 내 집 마련)"
]
current_house_options = [
    "LH 전세임대 (소년소녀가정 전형 거주)",
    "LH 전세/매입임대 (자립준비청년 전형 거주)",
    "일반 무상거주 (시설/친척/지인)",
    "일반 민간 임대 (월세/전세 계약)",
    "주거취약계층 (고시원/여관 등 임시)"
]

with st.form("lifecycle_form"):
    st.info("💡 지금 나의 상황과 미래의 꿈꾸는 모습을 차분하게 골라주세요.")
    
    st.markdown("#### 📌 [현재] 나의 출발선")
    user_name = st.text_input("👤 성함", "김자립")
    col1, col2 = st.columns(2)
    with col1:
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 가용 자산 (만원 단위)", min_value=0, value=100)
    with col2:
        is_vulnerable = st.checkbox("보호종료 청년 해당", value=True)
        now_sub = st.radio("🏦 주택청약통장 유무", ["네, 가입 중", "아니요, 미가입"])
    now_house = st.selectbox("🏠 현재 주거 형태", current_house_options)

    st.markdown("---")
    st.markdown("#### 🌱 [10년 후] 주거 목표")
    fam_10 = st.selectbox("10년 후 가구 구성", fam_options, index=0)
    house_10 = st.selectbox("10년 후 희망 전형", house_options, index=1)
    sub_10 = st.checkbox("10년 후에도 청약 유지를 약속할까요?", value=True)

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후 가구 구성", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 유지를 약속할까요?", value=True)

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립")
    fam_30 = st.selectbox("30년 후 가구 구성", fam_options, index=2)
    house_30 = st.selectbox("최종 주거 전형", house_options, index=4)
    sub_30 = st.checkbox("청약 통장으로 내 집 마련에 도전할까요?", value=True)

    submit_btn = st.form_submit_button("🚀 맞춤형 로드맵 리포트 생성", type="primary")

# 3. 디테일 끝판왕 분석 알고리즘
def analyze_current(assets, now_house, now_sub):
    report = ""
    # 청약 정밀 진단
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 [필수] 청약 통장: 자립의 가장 강력한 무기</h3>
            청약 통장은 단순히 저축이 아니라 <b>'공공 주택 입주권'</b>입니다. 지금 통장이 없다는 것은 미래에 제공될 모든 국가 주거 혜택을 포기하는 것과 같습니다.<br>
            <div class='action-box'>
                <b>✅ 전문가 긴급 처방</b>
                <ul style="margin-top:10px;">
                    <li><b>'청년주택드림청약통장'</b>으로 개설하세요. 이자율이 무려 4.5%입니다.</li>
                    <li>매달 2만 원이라도 자동이체를 설정하세요. 금액보다 <b>'납입 횟수'</b>가 가산점의 핵심(최대 6점)입니다.</li>
                    <li>군 복무 중이라면 군 적금과 연계하여 더 큰 혜택을 챙길 수 있습니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 [양호] 청약 통장: 아주 훌륭한 자립 태도</h3>
            꾸준한 납입은 미래의 배점 경쟁에서 압도적인 우위를 점하게 해줍니다. 정말 잘하고 계세요!<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                혹시 급전이 필요해 통장을 깨고 싶다면 <b>'청약예금 담보대출'</b>을 먼저 알아보세요. 내가 넣은 돈의 90%까지 아주 싼 이자로 빌릴 수 있어, 통장의 점수(납입 회차)를 지키면서 위기를 넘길 수 있습니다.
            </div>
        </div>
        """

    # 주거 형태 정밀 진단
    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [진단] 소년소녀가정 전세임대 거주 중</h3>
            만 20세까지 이자가 전액 면제되는 인생의 재무적 황금기입니다. 주거비가 0원인 이 기회를 절대 놓치지 마세요.<br>
            <div class='action-box'>
                <b>✅ 현재 시점 집중 과제</b>
                <ul style="margin-top:10px;">
                    <li><b>종잣돈 1,000만 원 형성:</b> 만 22세 이후부터는 이자가 발생합니다. 지금 나가는 돈이 없는 시기에 매월 20만 원씩 적금을 들어 독립 자금을 미리 강제로 만드세요.</li>
                    <li><b>권리분석 예습:</b> 지금 살고 있는 집의 등기부등본을 떼어보세요. (집주인 빚+보증금)이 집값의 90% 이하인지 확인하며 실무 감각을 익히세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [진단] 자립준비청년 전형 거주 중</h3>
            보호 종료 후 5년 특례(임대료 50% 감면)를 아주 잘 활용하고 계시네요. 주거 안정이 최고입니다!<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁 (상호전환제도 활용)</b><br>
                현재 가용 자산 {assets}만 원이 있다면, LH의 <b>'상호전환제도'</b>를 신청해 보증금을 더 넣으세요. 연 6~7%의 높은 이율로 계산하여 월세를 깎아주는데, 이는 웬만한 은행 적금보다 훨씬 이득입니다. 월세를 '치킨 한 마리 가격'으로 만드는 재무 전략을 짜보세요.
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [경고] 민간 월세/전세: 자산 누수 위험</h3>
            매달 소멸되는 비싼 월세와 전세사기 리스크에 노출되어 있습니다. 자립 초기 자산 형성에 가장 큰 방해 요인입니다.<br>
            <div class='action-box'>
                <b>✅ 긴급 탈출 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>1순위 카드 사용:</b> 여러분은 자립준비청년 1순위 자격이 있습니다. 보증금 100만 원이면 LH 안심 주택으로 들어갈 수 있습니다.</li>
                    <li><b>담당자 상담:</b> 지금 바로 멘토에게 연락하여 LH 전세/매입임대 상시 모집 신청 절차를 밟으세요. 월세로 나가는 40~50만 원을 저축으로 돌려야 합니다.</li>
                </ul>
            </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [긴급] 고시원/여관: 최우선 주거상향 대상</h3>
            현재의 환경에서는 심신의 안정과 자립 계획 수립이 어렵습니다. 국가의 긴급 지원을 즉시 받아야 합니다.<br>
            <div class='tip-box'>
                <b>💡 멘토의 긴급 솔루션</b><br>
                <b>'주거취약계층 주거상향 지원사업'</b>을 통해 보증금 0원, 이사비 지원, 생필품 지원까지 받으며 즉시 공공임대아파트로 이사할 수 있습니다. 부끄러워하지 말고 지금 바로 담당자에게 도움을 요청하세요. 당신의 권리입니다.
            </div>
        </div>
        """
    return report

def generate_future(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9;'><b>📅 {age}세 목표:</b> {fam} / {house}</div>"
    
    if not sub_status:
        report += "<div class='action-box' style='border-left-color:#E74C3C;'><b>⚠️ 주의:</b> 청약 납입 중단 시 향후 아파트 입주 순위에서 밀려날 위험이 큽니다. 가급적 소액이라도 유지를 권장합니다.</div>"

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 전세임대 실전 공략 가이드</h4>
            내가 원하는 동네의 깨끗한 민간 주택을 고르면 LH가 대신 전세계약을 맺어주는 자유로운 제도입니다.<br>
            <div class='action-box'>
                <b>📌 실전 행동 지침</b>
                <ul style="margin-top:10px;">
                    <li><b>부동산 공략법:</b> 방문 전 전화로 "LH 전세 전용면적 85㎡ 이하 물건 있나요?"라고 미리 확인하여 시간 낭비를 줄이세요.</li>
                    <li><b>권리분석 90% 룰:</b> (선순위 채권+내 보증금) / 주택 가격 ≤ 90% 공식은 절대적입니다. 빚이 많은 집은 LH가 승인해주지 않으니 집 고를 때 이 점을 반드시 부동산 사장님께 강조하세요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                이사할 때 도배/장판 비용(약 60만 원 한도) 지원이 가능하니 계약 전 LH 담당자에게 꼭 물어보세요. 또한 보증금 보험 가입은 필수이니 서류 제출 시 확인하세요.
            </div>
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 매입임대 실전 공략 가이드</h4>
            LH가 직접 사들인 검증된 빌라나 오피스텔에 입주하는 제도로, 전세사기 걱정이 없고 관리가 철저합니다.<br>
            <div class='action-box'>
                <b>📌 실전 행동 지침</b>
                <ul style="margin-top:10px;">
                    <li><b>'줍줍' 타이밍 확보:</b> LH청약플러스 앱에서 <b>'관심지역 알림(인천)'</b>을 켜두세요. 수시 모집 공고는 금요일 오후에 자주 올라옵니다.</li>
                    <li><b>예비 순번 사수:</b> 당첨이 안 되더라도 예비 번호를 받아두면 나중에 빈집이 생길 때 순서대로 연락이 옵니다. 일단 뜨면 무조건 신청하세요!</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                매입임대는 에어컨, 세탁기, 냉장고 등 기본 가전이 빌트인된 경우가 많습니다. 초기 독립 비용을 아껴 그 돈을 다시 청약이나 적금에 투자하는 선순환을 만드세요.
            </div>
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 아파트(건설임대) 가점 관리법</h4>
            안전하고 생활 인프라가 완벽한 LH 대단지 아파트에 입주하여 최장 30년까지 거주하는 꿈의 전형입니다.<br>
            <div class='action-box'>
                <b>📌 배점표 만점 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>거주지 배점:</b> 인천광역시에 주소지를 두고 오래 살수록 유리합니다. 직장 때문에 잠깐 주소를 옮길 때 거주 기간 점수가 깎이지 않는지 확인하세요.</li>
                    <li><b>청약 납입 횟수:</b> 금액과 상관없이 <b>'연체 없는 60회(5년)'</b>가 만점 기준입니다. 자동이체를 한 번도 끊기지 않게 방어하세요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁 (면적 제한)</b><br>
                혼자 사는 1인 가구는 전용 40㎡ 이하만 가능합니다. 하지만 20년 뒤 가족이 늘어나면 46㎡, 59㎡로 상향 지원이 가능하니 생애주기에 맞춘 전략이 필요합니다.
            </div>
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 통합공공임대: 30년 안심 거주 전략</h4>
            내 소득이 높아져도 쫓겨나지 않고, 소득에 비례해 임대료만 조절하며 평생 살 수 있는 2026년 최신 제도입니다.<br>
            <div class='action-box'>
                <b>📌 실전 행동 지침</b>
                <ul style="margin-top:10px;">
                    <li><b>평형의 자유:</b> 인원수에 따라 최대 84㎡(34평형) 아파트까지 배정받을 수 있습니다. 아이가 생기면 즉시 평형 상향 신청을 고려하세요.</li>
                    <li><b>특별공급 활용:</b> 신생아 출산, 맞벌이 부부 가산점을 노려 검단/계양 신도시 등 신규 단지 공략이 유리합니다.</li>
                </ul>
            </div>
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 공공분양 '뉴홈' 자가 소유 전략</h4>
            로드맵의 최종 목적지인 내 집 마련입니다. 주변 시세의 70% 가격으로 온전한 내 집을 갖는 방법입니다.<br>
            <div class='action-box'>
                <b>📌 당첨 및 대출 방어 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>청약 인정 총액:</b> 분양 당첨은 '총액' 싸움입니다. 매달 10만 원까지만 인정되니, 여력이 생기면 즉시 자동이체 금액을 10만 원으로 올리세요.</li>
                    <li><b>DSR 신용 점수 관리:</b> 당첨 후 집값의 80%를 빌릴 때 신용등급이 낮으면 대출이 거절됩니다. <b>현금서비스, 리볼빙, 카드론은 절대 금물</b>입니다!</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                '나눔형' 전형을 선택하면 나중에 집을 팔 때 수익의 일부를 LH와 나누는 대신 훨씬 싼 가격에 첫 집을 마련할 수 있어 초기 자금이 부족한 청년들에게 유리합니다.
            </div>
        </div>
        """
    return report

# 4. 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵 리포트</div>', unsafe_allow_html=True)
    st.write(f"**수신자:** {user_name} 님 | **발급일:** 2026년 3월 6일")

    # 섹션 1: 현재
    st.markdown('<div class="section-title">Step 1. 현재의 나 : 출발선 진단</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2: 10년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 2. 10년 후 ({current_age+10}세) : 주거 기반 구축기</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # 섹션 3: 20년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 3. 20년 후 ({current_age+20}세) : 주거 안정 및 상향기</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # 섹션 4: 30년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 4. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # 섹션 5: 정보망 및 담당자
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Step 5. 든든한 조력망 및 멘토의 편지</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ <a href="https://apply.lh.or.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">LH 청약플러스 바로가기 👆</a></b><br>
        실제 집 공고를 보고 신청하는 핵심 사이트! 앱을 깔고 '관심지역 알림'을 켜두는 게 필수입니다.<br><br>
        <b>2️⃣ <a href="https://www.myhome.go.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">마이홈 포털 자가진단 바로가기 👆</a></b><br>
        내가 어떤 전형에 가장 유리한지 AI가 미리 알려주는 아주 유용한 사이트예요.<br><br>
        <b>3️⃣ <a href="https://jaripon.ncrc.or.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">자립정보ON 바로가기 👆</a></b><br>
        주거뿐만 아니라 취업, 금융 정보까지 우리 청년들만을 위해 모아둔 백과사전입니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.1rem; margin-bottom: 0px; line-height: 1.8;">
                살면서 계획은 언제든 변할 수 있고 상황도 달라질 수 있습니다.<br>
                혼자 고민하다 기회를 놓치지 말고, 이 로드맵을 보다가 궁금한 게 생기면<br>
                <b>언제든 저에게 연락 주세요.</b> 당신의 든든한 내 편이 되어 함께 길을 찾겠습니다.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 6. 움직이는 캐릭터 인쇄 버튼 (인쇄 시 숨겨짐)
    st.markdown("---")
    components.html(
        """
        <center>
            <a href="#" onclick="window.parent.print(); return false;" title="리포트 전체 페이지 PDF로 저장하기">
                <img src="https://media.giphy.com/media/ic06p9J076137681I3/giphy.gif" width="100px" style="border-radius:50%; box-shadow:0 4px 10px rgba(0,0,0,0.1); cursor:pointer;">
            </a>
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">위 캐릭터를 누르면 리포트가 A4 용지 규격으로 깔끔하게 자동 분할되어 출력(저장)됩니다.</p>
        </center>
        """,
        height=180
    )