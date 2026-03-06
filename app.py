import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (인쇄 시 스크롤 제한 해제 및 가독성 최적화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    /* 기본 정보 카드 */
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    /* 실전 행동 지침 박스 */
    .action-box { background-color: #F4F9FF; padding: 22px; border-radius: 10px; border-left: 6px solid #3498DB; margin: 15px 0;}
    /* 비상 상황/주의사항 박스 */
    .emergency-box { background-color: #FEF5F5; padding: 22px; border-radius: 10px; border-left: 6px solid #E74C3C; margin: 15px 0; color: #C0392B;}
    /* 멘토 꿀팁 박스 */
    .tip-box { background-color: #FFF9E6; padding: 22px; border-radius: 10px; border-left: 6px solid #F1C40F; margin: 15px 0; color: #4D5656;}
    
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
st.markdown('<div class="sub-title">살면서 마주할 모든 순간을 함께하는 주거 안심 백과사전</div>', unsafe_allow_html=True)

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
    sub_10 = st.checkbox("10년 후에도 청약 유지를 약속할까요?", value=True, key="s10")

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후 가구 구성", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 유지를 약속할까요?", value=True, key="s20")

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립")
    fam_30 = st.selectbox("30년 후 가구 구성", fam_options, index=2)
    house_30 = st.selectbox("최종 주거 전형", house_options, index=4)
    sub_30 = st.checkbox("청약 통장으로 내 집 마련에 도전할까요?", value=True, key="s30")

    submit_btn = st.form_submit_button("🚀 맞춤형 로드맵 리포트 생성", type="primary")

# 3. 실무 디테일 함수
def get_lh_rules(house_type):
    rules = ""
    if "전세임대" in house_type:
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 및 재계약 규칙</b>
            <ul style='margin-top:10px;'>
                <li><b>계약 주기:</b> 2년 단위로 갱신해요.</li>
                <li><b>최대 거주:</b> 자립준비청년 전형은 <b>최대 30년</b>까지 거주할 수 있어요.</li>
                <li><b>재계약 준비:</b> 기간 만료 2~3개월 전 LH에서 안내문이 와요. 소득/재산 기준을 다시 심사하니 서류(주민등록등본, 가족관계증명서 등)를 잘 챙겨야 해요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 위기 상황 대처법</b>
            <ul style='margin-top:10px;'>
                <li><b>이자 연체:</b> 이자가 밀리면 연체료가 붙고, 3개월 이상 밀리면 계약 갱신이 안 될 수 있어요. 힘들 땐 미리 LH 지사에 연락해서 <b>분할 납부</b>를 상의하세요.</li>
                <li><b>집이 망가졌을 때:</b> 내 실수로 문이나 창문이 깨졌다면 내가 고쳐야 해요. 하지만 보일러나 수도관처럼 원래 집에 있던 건 집주인이 고쳐줘야 해요. <b>부동산 사장님이나 LH 지역본부</b>에 중재를 요청하세요.</li>
                <li><b>이사하고 싶을 때(이주):</b> 계약 기간 도중 이사하려면 LH 승인이 필요해요. 새로운 집을 구하기 전 반드시 <b>'이주신청서'</b>를 먼저 LH에 제출하세요!</li>
            </ul>
        </div>
        """
    elif "매입임대" in house_type:
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 및 재계약 규칙</b>
            <ul style='margin-top:10px;'>
                <li><b>계약 주기:</b> 2년 단위로 갱신해요.</li>
                <li><b>최대 거주:</b> 자립준비청년은 무주택 요건 유지 시 <b>최장 20년</b>까지 살 수 있어요.</li>
                <li><b>재계약 준비:</b> LH에서 집으로 날아오는 우편물을 절대 놓치지 마세요. 재계약 시점에 소득이 올랐다면 임대료가 조금 인상될 수 있어요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 위기 상황 대처법</b>
            <ul style='margin-top:10px;'>
                <li><b>임대료 연체:</b> LH는 독촉을 먼저 해요. 무조건 피하지 말고 <b>LH 주거복지 지사 담당자</b>에게 연락해서 사정을 말하는 게 중요해요.</li>
                <li><b>수리 문제:</b> 매입임대는 관리업체가 따로 있어요. 전등 교체 같은 소모품은 내가, 큰 고장은 관리업체에 전화하면 LH 비용으로 수리해 줍니다.</li>
                <li><b>해약하고 싶을 때:</b> 한 달 전에는 LH에 <b>'해약 신청서'</b>를 내야 보증금을 제때 돌려받고 깔끔하게 나갈 수 있어요.</li>
            </ul>
        </div>
        """
    elif "건설임대" in house_type or "통합공공" in house_type:
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 및 재계약 규칙</b>
            <ul style='margin-top:10px;'>
                <li><b>계약 주기:</b> 2년 단위 갱신 (최장 30년 거주).</li>
                <li><b>재계약 준비:</b> 아파트 관리사무소와 LH 지역본부에서 안내가 와요. 청약 통장 유지 여부가 중요한 곳이 많으니 절대 통장을 깨지 마세요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 위기 상황 대처법</b>
            <ul style='margin-top:10px;'>
                <li><b>관리비 연체:</b> 아파트는 임대료만큼 관리비가 중요해요. 연체 시 단전/단수의 위험이 있으니 주의하세요.</li>
                <li><b>퇴거 불이익:</b> 불법 전대(몰래 다른 사람에게 빌려주는 것) 적발 시 즉시 퇴거되고 향후 5년 이상 공공주택 입주가 금지되는 무서운 페널티가 있어요.</li>
                <li><b>상담 문의:</b> 아파트 내 <b>관리사무소</b>가 1차 상담 창구예요. 해결 안 되면 LH 지역본부 주거복지팀에 전화하세요.</li>
            </ul>
        </div>
        """
    return rules

# 4. 분석 알고리즘 (현재)
def analyze_current(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 자립의 가장 강력한 무기</h3>
            지금 통장이 없다는 건 미래의 모든 국가 주거 혜택을 포기하는 것과 같아요.<br>
            <div class='action-box'>
                <b>✅ 전문가 긴급 처방</b>
                <ul style="margin-top:10px;">
                    <li><b>'청년주택드림청약통장'</b>으로 개설하세요. 이자가 4.5%나 돼요.</li>
                    <li>매달 2만 원이라도 자동이체를 꼭 하세요. 금액보다 <b>'납입 횟수'</b>가 가산점의 핵심입니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 자립 태도</h3>
            꾸준한 납입은 미래 경쟁에서 압도적인 우위를 점하게 해줘요. 정말 잘하고 계세요!<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                급전이 필요해 통장을 깨고 싶다면 <b>'청약예금 담보대출'</b>을 받으세요. 내가 넣은 돈의 90%까지 아주 싼 이자로 빌려주니, 점수를 지키면서 위기를 넘길 수 있어요.
            </div>
        </div>
        """

    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [진단] 소년소녀가정 전세임대 거주 중</h3>
            만 20세까지 이자가 0%인 최고의 시기예요. 이 기회를 돈 모으는 발판으로 삼아야 해요.<br>
            <b>비용:</b> 지금은 0원이지만, 만 22세 이후부터는 1억 지원 기준 매달 약 8~16만 원의 이자가 발생해요.<br>
            <div class='action-box'>
                <b>✅ 현재 집중 과제</b>
                <ul style="margin-top:10px;">
                    <li><b>강제 저축:</b> 주거비가 안 나가는 지금, 매월 20만 원씩 무조건 저축해서 독립 자금을 만드세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [진단] 자립준비청년 전형 거주 중</h3>
            임대료 50% 감면 특례를 아주 잘 쓰고 계시네요! 보통 월세가 5~10만 원대로 저렴할 거예요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁 (상호전환제도)</b><br>
                가용 자산 {assets}만 원이 있다면, LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원당 연 6~7% 이율로 월세를 깎아주는데, 어떤 은행 적금보다 이득이에요. 월세를 '치킨 한 마리 가격'으로 낮춰보세요.
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 [위험] 민간 월세/전세 거주 중</h3>
            비싼 월세(40~60만 원)는 자립 초기 자산 형성을 막는 가장 큰 적이에요.<br>
            <div class='action-box'>
                <b>✅ 긴급 자립 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>1순위 카드 사용:</b> 여러분은 자립준비청년 1순위 자격이 있어요. 보증금 100만 원이면 LH 안심 주택으로 들어갈 수 있습니다.</li>
                    <li><b>즉시 신청:</b> 멘토에게 연락해 '자립준비청년 상시 모집' 공고를 확인하고 월세를 절반 이하로 줄이세요.</li>
                </ul>
            </div>
        </div>
        """
    return report

# 미래 로드맵 함수 (연령별+전형별 상세)
def generate_future(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9;'><b>📅 {age}세 목표:</b> {fam} / {house}</div>"
    
    # 공통 미래 가이드
    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 전세임대 실전 공략 가이드</h4>
            <b>장점:</b> 내가 고른 민간 주택을 LH가 빌려줘서 자유도가 높아요.<br>
            <b>비용:</b> 지원금(약 1.2억)의 연 1~2% 이자를 내요. 자립준비청년 할인을 받으면 <b>한 달에 약 5~8만 원</b>이면 살 수 있어요.<br>
            {get_lh_rules("전세임대")}
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 매입임대 실전 공략 가이드</h4>
            <b>장점:</b> LH가 주인이라 안전하고, 에어컨/세탁기 등이 갖춰진 곳이 많아요.<br>
            <b>비용:</b> 보증금 100~200만 원에 <b>월세 10~20만 원</b> 내외예요.<br>
            {get_lh_rules("매입임대")}
        </div>
        """
    elif "건설임대" in house or "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 아파트(건설/통합) 공략 가이드</h4>
            <b>장점:</b> 주차, 보안 등 인프라가 최고예요. 최장 30년 거주 가능해요.<br>
            <b>비용:</b> 보증금 약 3~5천만 원(대출 가능), <b>월세 10~20만 원대</b>예요.<br>
            {get_lh_rules("건설임대")}
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 {age}세 공공분양 '뉴홈' 내 집 마련 전략</h4>
            <b>장점:</b> 시세보다 30% 저렴하게 내 집을 가져요. 수익을 LH와 나누는 '나눔형'은 초기 자본이 적어도 가능해요.<br>
            <b>대출:</b> 집값의 80%를 저리 대출해주니 <b>월 50~80만 원 상환</b>으로 자가 소유가 가능해져요.<br>
            <div class='action-box'>
                <b>📌 당첨 비결</b>
                <ul style="margin-top:10px;">
                    <li><b>청약 총액:</b> 월 10만 원씩 꾸준히 인정받는 게 핵심이에요.</li>
                    <li><b>신용 사수:</b> 잦은 카드론이나 연체는 대출을 막아요. 신용 관리가 곧 돈이에요!</li>
                </ul>
            </div>
        </div>
        """
    return report

# 5. 최종 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**대상자:** {user_name} 님 | **작성일:** 2026년 3월 6일")

    st.markdown('<div class="section-title">1단계. 현재의 나 : 출발선 진단과 비상 전략</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2단계. 10년 후 ({current_age+10}세) : 주거 기반 구축과 위기 관리</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3단계. 20년 후 ({current_age+20}세) : 주거 안정 및 상향</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4단계. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5단계. 든든한 조력망 (필수 사이트 주소)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr)</b><br>
        실제 공고 확인 및 신청 창구! 앱을 깔고 '인천 관심지역 알림' 설정을 반드시 하세요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr)</b><br>
        전국 주거 복지 제도를 한눈에 검색하고, '자가진단' 기능을 통해 내 점수를 미리 계산해 보세요.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
        자립준비청년들만을 위한 전용 포털입니다. 주거 혜택 외에도 교육, 금융 정보가 가득합니다.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr)</b><br>
        버팀목, 디딤돌 등 나라에서 지원하는 초저금리 대출 상품들을 한눈에 비교할 수 있습니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                이 리포트를 보다가 막막하거나, 연체/수리 등 위기 상황이 생기면<br>
                <b>절대 혼자 고민하지 말고 담당자에게 연락 주세요.</b><br>
                당신의 든든한 내 편이 되어 함께 가장 좋은 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    components.html(
        """
        <center>
            <a href="#" onclick="window.parent.print(); return false;">
                <img src="https://media.giphy.com/media/ic06p9J076137681I3/giphy.gif" width="100px" style="border-radius:50%; box-shadow:0 4px 10px rgba(0,0,0,0.1); cursor:pointer;">
            </a>
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">위 캐릭터를 누르면 리포트가 A4 용지 규격으로 깔끔하게 자동 분할되어 출력(저장)됩니다.</p>
        </center>
        """,
        height=180
    )