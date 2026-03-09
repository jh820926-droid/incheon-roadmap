import streamlit as st
import streamlit.components.v1 as components

# =====================================================================
# [Step 1] 앱 기본 설정 및 메타데이터 (안정성 확보)
# =====================================================================
st.set_page_config(
    page_title="2026 인천자립 주거로드맵 - 주거 안심 백과사전",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =====================================================================
# [Step 2] 초정밀 CSS (화면 깨짐 및 인쇄 레이아웃 완벽 제어)
# =====================================================================
st.markdown("""
<style>
/* 기본 웹 폰트 및 배경 설정 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #F8F9FA;
    color: #2C3E50;
}

/* 타이틀 및 헤더 (가독성 극대화) */
.main-title { font-size: 2.6rem; color: #1A5276; font-weight: 900; text-align: center; margin-bottom: 10px; line-height: 1.4; word-break: keep-all;}
.sub-title { font-size: 1.2rem; color: #546E7A; text-align: center; margin-bottom: 40px; font-weight: 400; word-break: keep-all;}
.report-header { font-size: 2.2rem; color: #0E6251; font-weight: 900; border-bottom: 5px solid #1ABC9C; padding-bottom: 15px; margin-top: 70px; margin-bottom: 40px; text-align: center;}
.section-title { font-size: 1.8rem; color: #17202A; font-weight: 800; border-left: 10px solid #1ABC9C; padding-left: 20px; margin-top: 60px; margin-bottom: 30px; background-color: #E8F8F5; padding-top: 12px; padding-bottom: 12px; border-radius: 0 15px 15px 0;}

/* 정보 블록 디자인 (시선 분산 및 중요도 강조) */
.card-box { background-color: #FFFFFF; padding: 40px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.06); border: 1px solid #EAEDED; margin-bottom: 40px; line-height: 1.9;}
.card-title { font-size: 1.4rem; font-weight: 800; color: #21618C; border-bottom: 2px dashed #AED6F1; padding-bottom: 10px; margin-bottom: 20px;}

.action-box { background-color: #EBF5FB; padding: 30px; border-radius: 15px; border-left: 8px solid #2E86C1; margin: 25px 0; color: #1B4F72;}
.emergency-box { background-color: #FDEDEC; padding: 30px; border-radius: 15px; border-left: 8px solid #CB4335; margin: 25px 0; color: #78281F;}
.tip-box { background-color: #FEF9E7; padding: 30px; border-radius: 15px; border-left: 8px solid #F1C40F; margin: 25px 0; color: #7D6608;}

.highlight-blue { background-color: #D4E6F1; font-weight: bold; padding: 2px 6px; border-radius: 4px;}
.highlight-red { background-color: #F5B7B1; font-weight: bold; padding: 2px 6px; border-radius: 4px;}
.highlight-yellow { background-color: #FCF3CF; font-weight: bold; padding: 2px 6px; border-radius: 4px;}

.step-list { margin-left: 0; margin-bottom: 25px; list-style-type: none; padding-left: 0; }
.step-list li { margin-bottom: 18px; padding-left: 30px; position: relative; word-break: keep-all; }
.step-list li::before { content: '✔️'; position: absolute; left: 0; top: 0; }

.calc-box { background-color: #F4F6F6; padding: 20px; border-radius: 10px; font-family: monospace; font-size: 1.1rem; color: #2C3E50; border: 1px solid #D5DBDB; margin: 15px 0; text-align: center;}

/* 인쇄 시 제목과 내용이 분리되지 않도록 강제 방어 */
.section-title, .card-title, h3, h4 { break-after: avoid !important; page-break-after: avoid !important; }

/* 🖨️ PDF 인쇄를 위한 절대 규칙 (스트림릿 레이아웃 무력화 및 부드러운 페이지 넘김) */
@media print {
    header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button, .print-btn-container { display: none !important; }
    .main-title, .sub-title, img, hr { display: none !important; }
    
    html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"] {
        height: auto !important;
        min-height: 100% !important;
        max-height: none !important;
        overflow: visible !important;
        display: block !important;
        position: static !important;
        background-color: white !important;
    }
    
    .page-break {
        page-break-before: always !important;
        display: block !important;
        height: 1px !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .card-box { box-shadow: none !important; border: 2px solid #BDC3C7 !important; }
    * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
}
</style>
""", unsafe_allow_html=True)

# =====================================================================
# [Step 3] 화면 상단 헤더
# =====================================================================
st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">사회복지 전문가가 제안하는 생애주기별 맞춤 주거 안심 백과사전</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass
st.divider()

# =====================================================================
# [Step 4] 생애주기 30년 데이터 입력 폼
# =====================================================================
st.subheader("📋 Step 1. 나의 30년 주거 자립 계획 설계")

fam_options = ["1인 가구 (혼자 생활)", "2인 가구 (부부/형제/친구)", "3인 가구 (부부+자녀1)", "4인 이상 (다자녀 가정)"]
house_options = [
    "전세임대 (내가 고른 민간주택을 LH가 지원)", 
    "매입임대 (LH가 직접 사서 관리하는 안심 빌라)", 
    "건설임대 (안전하고 쾌적한 국민/행복 아파트)", 
    "통합공공임대 (가족 성장에 맞춘 평생 아파트)", 
    "공공분양 (내 집 소유의 꿈 실현)"
]
current_house_options = [
    "LH 전세임대 (소년소녀가정 전형 거주)",
    "LH 전세/매입임대 (자립준비청년 전형 거주)",
    "일반 무상거주 (시설/친척/지인 집 거주)",
    "일반 민간 임대 (월세/전세 개인 계약)",
    "주거취약계층 (고시원/반지하/여관 등 임시 거주)"
]

with st.form("master_form"):
    st.info("💡 지금 입력하는 데이터는 여러분의 30년 인생을 안전하게 지켜줄 가장 강력한 백과사전을 만드는 재료가 됩니다. 신중하게 선택해 주세요.")
    
    st.markdown("#### 📌 [현재] 나의 출발선 진단")
    user_name = st.text_input("👤 이름 (리포트 수신인)", "김자립")
    
    col1, col2 = st.columns(2)
    with col1:
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 현재 가용 자산 (단위: 만원)", min_value=0, value=100)
    with col2:
        is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 여부", value=True)
        now_sub = st.radio("🏦 주택청약통장 유무", ["네, 가입해서 성실히 납부 중이에요", "아니요, 아직 없거나 멈췄어요"])
        
    now_house = st.selectbox("🏠 현재 거주 중인 주거 형태", current_house_options)

    st.markdown("---")
    st.markdown("#### 🌱 [10년 후] 주거 목표 (성장기)")
    fam_10 = st.selectbox("10년 후 예상 가구원 수", fam_options, index=0)
    house_10 = st.selectbox("10년 후 희망 주거 전형", house_options, index=1)
    sub_10 = st.checkbox("10년 후에도 청약 유지를 약속하시겠습니까?", value=True, key="s10")

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표 (안정기)")
    fam_20 = st.selectbox("20년 후 예상 가구원 수", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 주거 전형", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 유지를 약속하시겠습니까?", value=True, key="s20")

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립 목표 (정착기)")
    fam_30 = st.selectbox("30년 후 예상 가구원 수", fam_options, index=2)
    house_30 = st.selectbox("최종 종착지 주거 전형", house_options, index=4)
    sub_30 = st.checkbox("청약 통장으로 내 집 마련에 성공하시겠습니까?", value=True, key="s30")

    st.write("")
    submit_btn = st.form_submit_button("🚀 나만의 주거 안심 백과사전 생성하기", type="primary")

# =====================================================================
# [Step 5] 실전 거주 생존 매뉴얼 함수 (※주의: 들여쓰기 절대 금지)
# =====================================================================
def get_survival_manual(house_type):
    content = ""
    if "전세임대" in house_type:
        content = """<div class='action-box'>
<div class='card-title'>🗓️ 전세임대 재계약 및 행정 처리 매뉴얼</div>
<ul class='step-list'>
<li><b>재계약 주기와 한도:</b> 기본 2년 단위로 계약합니다. 자립준비청년은 총 14회까지 갱신이 가능해서 <span class='highlight-blue'>최장 30년</span> 동안 쫓겨날 걱정 없이 안전하게 살 수 있어요.</li>
<li><b>재계약 서류 준비:</b> 계약 만료 3개월 전에 LH에서 우편물이 날아옵니다. 이때 당황하지 말고 <b>신분증 사본, 주민등록등본(상세), 가족관계증명서(상세), 금융정보제공동의서</b>를 동봉해서 지정된 법무사 사무실이나 LH 지사로 등기우편을 보내면 끝납니다.</li>
<li><b>소득 초과 시 주의점:</b> 열심히 일해서 소득이 국가 기준을 초과하더라도 당장 쫓겨나지는 않습니다. 대신 임대료(이자)가 <span class='highlight-red'>최대 80%까지 할증</span>될 수 있습니다. (예: 원래 이자가 5만 원이었다면 9만 원으로 오를 수 있음). 이 부분은 미리 저축 예산에 반영해야 합니다.</li>
<li><b>도배/장판 무상 지원:</b> 처음 이사할 때 벽지나 장판이 너무 더럽다면, 내 돈을 절대 쓰지 말고 LH에 <b>도배/장판 지원금(약 60만 원 한도)</b>을 신청하세요. 거주 기간 중 딱 1번 쓸 수 있는 소중한 권리입니다.</li>
</ul>
</div>
<div class='emergency-box'>
<div class='card-title'>🚨 전세임대 거주 중 위기 발생 시 행동 요령</div>
<ul class='step-list'>
<li><b>이자가 연체되었을 때:</b> 이자가 3개월 이상 밀리면 LH에서 내용증명(계약 해지 통보)이 옵니다. 돈이 없다고 무서워서 전화를 피하면 절대 안 됩니다! 즉시 <b>LH 관할 지사 전세임대부</b>에 전화해서 <span class='highlight-red'>"담당자님, 제가 지금 사정이 너무 어려워서 그러는데 밀린 이자를 분할 납부하게 해주세요"</span>라고 읍소하세요. 갚을 의지만 보이면 LH는 강제로 내쫓지 않고 시간을 줍니다.</li>
<li><b>보일러, 누수 등 중대 결함 발생:</b> 형광등 교체, 도어락 건전지 교체 같은 소모품은 내가 내 돈으로 해야 합니다. 하지만 <b>보일러 고장, 천장 누수, 수도관 파열</b> 같은 집의 기본 골조 문제는 무조건 '집주인'이 수리 비용을 내야 합니다. 직접 집주인과 얼굴 붉히며 싸우지 말고 <b>계약했던 부동산 사장님</b>에게 전화해서 중재를 부탁하세요.</li>
<li><b>급하게 이사가고 싶을 때 (이주 절차):</b> 계약 기간 중간에 직장이나 개인 사정으로 급하게 이사해야 한다면, 내 맘대로 짐을 빼면 절대 안 됩니다! 최소 2~3개월 전에 LH에 <b>'이주 신청서'</b>를 제출해야 합니다. 그래야 LH가 집주인에게서 보증금을 돌려받아 내가 갈 새로운 집으로 지원금을 무사히 쏴줄 수 있습니다.</li>
</ul>
</div>"""
    elif "매입임대" in house_type:
        content = """<div class='action-box'>
<div class='card-title'>🗓️ 매입임대 거주 및 재계약 매뉴얼</div>
<ul class='step-list'>
<li><b>재계약 주기와 한도:</b> 2년 단위로 계약하며, 무주택 요건만 유지하면 <span class='highlight-blue'>최장 20년</span>까지 거주할 수 있습니다. LH가 곧 집주인이기 때문에 악덕 집주인 만나서 보증금 떼일 걱정이 아예 없습니다.</li>
<li><b>풀옵션 가전 혜택 활용기:</b> 매입임대 주택 중 '청년형'은 <b>냉장고, 세탁기, 에어컨, 책상</b> 등이 기본 옵션으로 들어있는 경우가 많습니다. 처음 독립할 때 수백만 원에 달하는 가전제품 구매 비용을 세이브할 수 있는 최고의 혜택입니다.</li>
<li><b>관리비 폭탄 주의:</b> 월세 자체는 주변 시세의 30% 수준으로 엄청 저렴하지만, 빌라 특성상 공동청소비, 엘리베이터 유지비 등 <b>공용 관리비(보통 3~7만 원)</b>가 별도로 매달 청구됩니다. 월세+관리비+공과금(가스, 전기)을 모두 합친 금액으로 한 달 주거 예산을 짜야 생활비 펑크를 막을 수 있습니다.</li>
</ul>
</div>
<div class='emergency-box'>
<div class='card-title'>🚨 매입임대 위기 발생 시 멘토의 조언</div>
<ul class='step-list'>
<li><b>월세가 연체되었을 때:</b> 자동이체 통장에 잔고가 없어 3회 이상 밀리면 퇴거 대상 명단에 오릅니다. 연체 이자율도 생각보다 높습니다. 경고 문자가 오면 즉시 <b>LH 주거복지 지사 담당자</b>에게 연락해 분할 납부 계획을 명확히 밝히고 성실히 갚아나가야 집을 지킬 수 있습니다.</li>
<li><b>집안 시설이 고장 났을 때:</b> 매입임대의 가장 큰 장점입니다. 집안 기본 시설(보일러, 기본 옵션 가전 등)이 고장 나면 맘고생 할 필요 없이 <b>'LH 유지보수 접수센터 (☎ 1600-1004)'</b>로 전화 한 통만 하세요. 접수하면 수리 기사님이 직접 방문해서 무료로 깔끔하게 고쳐주십니다.</li>
<li><b>갑자기 방을 빼야 할 때 (중도 해약):</b> 다른 지역으로 취업해서 급히 방을 빼야 한다면, 방을 비우기 최소 <b>1개월 전</b>에 LH 지사나 지역 관리사무소에 <b>'해약 신청서'</b>를 제출해야 합니다. 그래야 보증금에서 엉뚱한 돈이 깎이지 않고 제날짜에 정산받고 나갈 수 있습니다.</li>
</ul>
</div>"""
    else: 
        content = """<div class='action-box'>
<div class='card-title'>🗓️ 공공아파트(건설/통합) 생활 완벽 가이드</div>
<ul class='step-list'>
<li><b>거주 안정성 끝판왕:</b> 2년 단위로 갱신하며 소득 및 자산 요건만 잘 유지하면 <span class='highlight-blue'>최장 30년</span> 거주가 보장됩니다. 2년마다 겪어야 하는 이사 스트레스, 중개수수료, 이사비용을 완벽하게 없앨 수 있습니다.</li>
<li><b>아파트 관리비의 진실:</b> 빌라나 오피스텔보다 경비실, 조경 등 공용 시설이 많아 <b>아파트 관리비(10~15만 원 이상)</b>가 꽤 무겁게 나옵니다. 여름철 에어컨 누진세, 겨울철 난방비까지 합치면 주거비 지출이 커지니 반드시 관리비 예산 통장을 따로 만들어 두세요.</li>
<li><b>자동차 가액 절대 주의:</b> 공공아파트 거주 중에 차를 사게 된다면 매우 조심해야 합니다! <b>국가에서 정한 자동차 가액 기준(약 3,700만 원 선, 매년 변동됨)</b>을 넘는 비싼 차를 명의로 등록하면 재계약 심사에서 즉시 탈락해서 집에서 쫓겨납니다. 중고차를 사거나 구매 전 기준을 꼭 확인하세요.</li>
</ul>
</div>
<div class='emergency-box'>
<div class='card-title'>🚨 아파트 거주 시 절대 주의사항 (강제 퇴거 위험)</div>
<ul class='step-list'>
<li><b>불법 전대 절대 금지:</b> 내가 당첨된 아파트를 싼값에 다른 친구나 지인에게 몰래 월세를 받고 빌려주는 행위(불법 전대)는 심각한 범죄입니다. LH 불시 거주 점검에 걸리면 <span class='highlight-red'>즉각 강제 퇴거 조치되며 향후 5년 이상 모든 국가 주택에 입주할 수 없습니다.</span> 인생을 망치는 지름길입니다.</li>
<li><b>층간소음 및 이웃 분쟁:</b> 아파트는 수백 세대가 모여 사는 공동주택입니다. 위층이 시끄럽다고 천장을 두드리거나 직접 올라가서 얼굴 붉히며 싸우지 마세요. 문제가 생기면 1차적으로 <b>'아파트 관리사무소'</b>나 '경비실'에 정식으로 중재를 요청하는 것이 가장 안전하고 지혜로운 방법입니다.</li>
<li><b>입주 지연 위기 시:</b> 아파트에 당첨되었는데 잔금을 못 치러서 입주를 못 하고 있다면, 혼자 포기하지 말고 지정된 기간 내에 <b>LH 입주지원센터</b>에 전화해서 입주 연기를 신청하거나 보증금 대출 상품(버팀목 전세자금 등)을 안내받아 위기를 넘기세요.</li>
</ul>
</div>"""
    return content

# =====================================================================
# [Step 6] 현재 상황 초정밀 진단 
# =====================================================================
def analyze_current_status(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """<div class='card-box'>
<div class='card-title'>🏦 [긴급] 청약 통장: 완벽한 자립을 위한 유일하고 강력한 방패</div>
지금 청약 통장이 없다는 것은, 훗날 국가가 시세의 반값으로 제공하는 깨끗한 새 아파트에 들어갈 기회를 내 발로 걷어차는 것과 같습니다. 남들보다 뒤처지기 전에 지금 당장, 오늘 시작해야 합니다.<br>
<div class='action-box'>
<span class='highlight-blue'>당장 실천할 과제</span> <b>무조건 내일 은행으로 달려가세요!</b>
<ul class='step-list'>
<li>신분증을 챙겨 은행에 가서 <b>'청년주택드림청약통장'</b>을 개설해 달라고 요구하세요. 일반 청약통장보다 이자율이 최대 4.5%로 매우 높고, 나중에 집 살 때 대출 우대 혜택까지 있는 마법의 통장입니다.</li>
<li>당장 수중에 여유 돈이 없다면 매달 딱 <span class='highlight-yellow'>2만 원</span>만 자동이체 해두세요. 공공임대 아파트에 들어갈 때는 통장에 돈이 얼마 있느냐보다 <b>'단 한 번도 밀리지 않고 꾸준히 낸 횟수'</b>가 합격을 결정짓는 절대적인 점수(최대 6점)가 됩니다. 10년 뒤 나를 위한 최고의 보험입니다.</li>
<li>만약 군 복무를 앞두고 있거나 복무 중이라면, 군인 전용 적금과 연계하여 납입 인정 금액을 폭발적으로 늘릴 수 있으니 담당 멘토에게 꼭 물어보세요.</li>
</ul>
</div>
</div>"""
    else:
        report += """<div class='card-box'>
<div class='card-title'>🏦 [최우수] 청약 통장: 완벽한 자립의 첫 단추를 채웠습니다!</div>
수많은 유혹을 이기고 매달 꾸준히 청약을 넣고 있는 당신을 진심으로 칭찬합니다! 이 성실함이 나중에 아파트 청약 경쟁에서 수백 명을 제치고 당신을 1순위로 만들어 줄 가장 강력하고 날카로운 무기가 될 것입니다.<br>
<div class='tip-box'>
<span class='highlight-yellow'>절대 명심할 꿀팁</span> <b>목돈이 급할 땐 해지 대신 '대출'을 활용하세요!</b><br>
살다 보면 갑자기 병원비가 필요하거나 보증금 때문에 300~500만 원의 급전이 절실해서 청약 통장을 깨고 싶은 아찔한 순간이 무조건 옵니다. 그때 <span class='highlight-red'>절대 해지버튼을 누르지 마세요!</span> 스마트폰 은행 앱에 들어가서 <b>'청약예금 담보대출'</b>을 신청하면, 내가 넣은 돈의 90%까지 아주 싼 이자로 은행에서 바로 빌릴 수 있습니다. 이렇게 하면 내 소중한 청약 가점(납입 횟수)은 지켜내고, 당장의 급한 불도 끌 수 있습니다.
</div>
</div>"""

    if "소년소녀가정" in now_house:
        report += """<div class='card-box'>
<div class='card-title'>🏠 [현재 진단] 소년소녀가정 전세임대 거주 중</div>
<b>최고의 장점:</b> 현재 당신은 만 20세까지 1억이 넘는 전세지원금에 대한 이자가 <span class='highlight-blue'>'완전 무료(0원)'</span>인 인생 최고의 재무적 황금기에 있습니다. 숨만 쉬어도 돈이 굳는 이 귀한 시기를 소비재만 사며 흘려보내면 절대 안 됩니다.<br>
<div class='action-box'>
<span class='highlight-blue'>돈 모으기 미션</span> <b>만 22세를 대비한 강제 저축 플랜</b>
<ul class='step-list'>
<li><b>이자가 생기는 시점을 명심하세요:</b> 영원히 무료가 아닙니다. 만 22세 이후부터는 전세지원금(예: 1억)에 대해 연 1~2%의 이자가 발생합니다. 즉, 어느 날 갑자기 매달 8~16만 원의 청구서가 집으로 날아오게 됩니다.</li>
<li><b>종잣돈 1,500만 원 강제 생성기:</b> 주거비가 1원도 안 나가는 지금! 알바를 하든 생활비를 아끼든 매월 <span class='highlight-yellow'>최소 20만 원 이상</span> 무조건 해지가 어려운 적금에 묶어두세요. 이렇게 5년만 모아도 원금만 1,200만 원이 넘습니다. 이 돈이 나중에 더 넓고 좋은 집으로 이사 갈 때 든든한 보증금이 되어 당신의 삶을 구원할 겁니다.</li>
</ul>
</div>
</div>"""
    elif "자립준비청년" in now_house:
        report += f"""<div class='card-box'>
<div class='card-title'>🏠 [현재 진단] 자립준비청년 전용 임대주택 거주 중</div>
<b>주거 안정성 100%:</b> 보호가 종료된 후 5년 동안 주어지는 '임대료 50% 감면' 특례를 아주 지혜롭게 활용하고 계시네요. 덕분에 주변 친구들이 50만 원씩 월세를 내며 허덕일 때, 당신은 5~10만 원대의 월세로 편안하게 미래를 준비하고 있을 겁니다.<br>
<div class='tip-box'>
<span class='highlight-yellow'>마법의 재무 설계</span> <b>상호전환제도로 월세를 '치킨 한 마리 값'으로 깎아버리세요!</b><br>
현재 모아둔 자산 <b>{assets}만 원</b>이 그저 은행 입출금 통장에서 놀고 있다면, 당장 LH 지사에 전화해서 <b>'전환보증금'</b>을 추가 납부하겠다고 하세요. 100만 원 단위로 보증금을 더 넣을 때마다, LH가 연 6~7%의 높은 이율로 계산해서 매달 내는 월세를 팍팍 깎아줍니다. 시중 은행의 적금 이자가 고작 3~4%인 걸 감안하면 무조건 남는 완벽한 장사입니다. 매달 나가는 월세를 2~3만 원 수준으로 만들어 버리세요!
</div>
</div>"""
    elif "민간 임대" in now_house:
        report += """<div class='card-box'>
<div class='card-title'>🏠 [위험 경고] 일반 민간 주택 (월세/전세) 거주 중</div>
<b>자산 누수 경고:</b> 어린 나이에 일찍 독립하여 스스로 집을 구한 용기와 자립심은 대단합니다! 하지만 매달 건물주에게 바치는 비싼 월세(40~60만 원)는 밑 빠진 독에 물 붓기입니다. 당신이 미래를 위해 종잣돈을 모으는 걸 원천적으로 차단하는 가장 큰 적입니다. 게다가 민간 빌라 전세라면 <b>전세사기 리스크</b>에 무방비로 노출되어 있어 너무 위험합니다.<br>
<div class='emergency-box'>
<span class='highlight-red'>긴급 주거 상향 전략</span> <b>1순위 카드를 지금 당장 빼드세요!</b>
<ul class='step-list'>
<li>당신에게는 대한민국에서 가장 강력하고 위력적인 주거 복지 혜택인 <b>'자립준비청년 1순위 자격'</b>이 있습니다. 보증금 단돈 100만 원이면 국가가 관리하는 안전하고 저렴한 집으로 들어갈 수 있습니다.</li>
<li>이 글을 읽는 즉시 망설이지 말고 담당 멘토에게 전화하세요. "선생님, 저 민간 월세 너무 비싸서 안 되겠어요. LH 전세임대(또는 매입임대) 상시 모집 신청 도와주세요"라고 말하세요. 매달 버려지는 월세 50만 원을 5만 원으로 줄여야만 진짜 자립에 성공할 수 있습니다.</li>
</ul>
</div>
</div>"""
    else:
        report += """<div class='card-box'>
<div class='card-title'>🏠 [초긴급 구제] 고시원, 반지하, 여관 등 주거취약계층 거주 중</div>
<b>멘토의 진심 어린 조언:</b> 지금 좁고 창문도 제대로 없는 방에서 얼마나 답답하고 외로우신가요? 이런 열악한 환경에서는 우울증이 오기 쉽고, 건강한 직장 생활과 미래를 설계하기가 불가능에 가깝습니다. 혼자 모든 걸 짊어지고 버티는 건 미덕이 아닙니다. 국가는 여러분을 구출하기 위한 제도를 이미 완벽하게 만들어 두었습니다.<br>
<div class='emergency-box'>
<span class='highlight-red'>생존을 위한 즉각 행동</span> <b>'주거취약계층 주거상향 지원사업' 무조건 신청하기</b>
<ul class='step-list'>
<li>이 제도를 이용하면 수중에 보증금이 단 0원이더라도 깨끗한 공공임대 아파트나 빌라로 즉시 이사할 수 있습니다.</li>
<li>이사할 때 드는 용달 비용은 물론, 첫 독립에 필수적인 냉장고, 세탁기 등 생필품 구입 비용까지 국가가 싹 다 지원해 줍니다.</li>
<li>부끄러워할 필요 전혀 없습니다. 이 글을 읽는 즉시, 부담감을 내려놓고 저(담당자 김정현 멘토)에게 카톡이나 전화를 주세요. 모든 복잡한 서류 작업과 집을 구하는 과정을 멘토가 여러분의 손을 잡고 함께 발로 뛰겠습니다.</li>
</ul>
</div>
</div>"""
    return report

# =====================================================================
# [Step 7] 미래 10년/20년/30년 생애주기 맞춤 로드맵 생성
# =====================================================================
def generate_future_roadmap(age, fam, house, sub_status):
    report = f"""<div class='card-box' style='border-left:12px solid #1ABC9C; background-color:#F2FBF9; padding-bottom:20px; margin-bottom:20px;'>
<b style='font-size:1.4rem; color:#0E6251;'>📅 {age}세 시점의 청사진:</b> <br>
<span style='font-size:1.1rem;'>나의 소중한 가족 구성은 <b>[{fam}]</b>이며, 안전하고 쾌적한 <b>[{house}]</b>에 거주하는 것을 목표로 합니다.</span>
</div>"""
    
    if not sub_status:
        report += """<div class='emergency-box'>
<span class='highlight-red'>🚨 치명적 경고</span> <b>청약 통장 납입 중단이 감지되었습니다!</b><br>
이 시기에 청약을 중단하면 그동안 힘들게 쌓아온 공든 탑이 한순간에 무너집니다. 나중에 사랑하는 가족이 생겨 넓은 아파트로 이사 가고 싶어도, 청약 점수가 모자라 서류 심사에서 광탈 1순위가 됩니다. 지금 당장 커피 두 잔 안 마신다고 생각하고 <span class='highlight-yellow'>월 2만 원 자동이체</span>를 어떻게든 부활시켜야만 여러분의 미래가 뚫립니다!
</div>"""

    if "전세임대" in house:
        report += f"""<div class='card-box'>
<div class='card-title'>🔎 전세임대 100전 100승 실전 공략 가이드</div>
내가 원하는 동네, 출퇴근하기 편한 역세권의 민간 빌라나 깨끗한 오피스텔을 직접 돌아다니며 골라오면, LH가 집주인과 직접 딜을 해서 내 대신 전세 계약을 맺어주는 매우 자유롭고 유연한 제도입니다.<br>
<div class='action-box'>
<span class='highlight-blue'>핵심 기술</span> <b>부동산 사장님을 내 편으로 만드는 '권리분석 90% 룰' 계산법</b>
<p>LH는 우리 청년들의 피 같은 보증금을 전세사기로부터 지키기 위해 정말 피도 눈물도 없이 깐깐하게 심사합니다. 집주인이 은행 빚(융자)이 많으면 심사 단계에서 무조건 탈락시킵니다. 부동산에 가서 헛걸음하며 시간 낭비하지 않으려면 이 공식을 무조건 외우세요.</p>
<div class='calc-box'>
<b>👉 공식: (집주인 대출금 + 나의 전세 보증금) ÷ 주택의 현재 시세 ≤ 90%</b>
</div>
<ul class='step-list'>
<li><b>실전 계산 예시:</b> 부동산에서 본 집값이 2억인데, 집주인이 은행에서 1억 5천을 빌렸고, 내 보증금이 5천만 원이라면? (1.5억 + 0.5억) / 2억 = 100%. 즉 90%를 초과했기 때문에 LH 심사에서 100% 떨어집니다. 이 집은 포기해야 합니다.</li>
<li><b>부동산 제압 멘트:</b> 공인중개사 사무소 문을 열고 들어가서 기죽지 말고 이렇게 말씀하세요. <span class='highlight-blue'>"사장님, 저 LH 전세임대로 구합니다. 부채비율 90% 이하로 권리분석 무조건 통과할 수 있는 융자 없는 깨끗한 집만 리스트 뽑아주세요!"</span> 이렇게 전문가처럼 당당하게 말해야 사장님도 허위 매물이나 엉뚱한 집을 보여주지 않고 여러분을 VIP로 대우합니다.</li>
</ul>
</div>
{get_survival_manual("전세임대")}
</div>"""
    elif "매입임대" in house:
        report += f"""<div class='card-box'>
<div class='card-title'>🔎 매입임대 100전 100승 실전 공략 가이드</div>
LH가 도심 곳곳의 튼튼하게 지어진 다세대 빌라나 신축 오피스텔을 통째로 사들여서 우리에게 시세의 반의반 값으로 빌려주는 훌륭한 제도입니다. 집주인이 다름 아닌 '국가'이기 때문에 전세보증금을 떼일 걱정이 단 0.1%도 없는 대한민국에서 가장 안전한 주택입니다.<br>
<div class='tip-box'>
<span class='highlight-yellow'>비밀 작전</span> <b>실무자들만 몰래 아는 '줍줍(잔여세대 수시모집)' 타이밍</b>
<p>매입임대는 경쟁률이 수십 대 일에 달할 정도로 인기가 폭발적입니다. 하지만 서류 심사에 떨어지거나 막상 계약 날 변심해서 계약을 포기하는 '빈집'들이 매주 쏟아져 나옵니다. 우리는 남들이 버린 이 황금 같은 빈집을 주워 담아야 합니다.</p>
<ul class='step-list'>
<li><b>알람 설정 필수:</b> 당장 스마트폰에 <b>'LH청약플러스'</b> 앱을 다운받아 로그인하세요. [마이페이지] ➔ [관심지역 알림] 메뉴에 들어가서 <b>'인천광역시'</b>를 체크하고 푸시 알림을 켜두세요.</li>
<li><b>금요일을 노려라:</b> 보통 담당자들이 일주일 업무를 마감하는 <span class='highlight-yellow'>매주 금요일 오후 4~5시쯤</span> 잔여세대 수시모집 공고가 소리 소문 없이 슬쩍 올라옵니다. 스마트폰에 알람이 울리면 일단 앞뒤 조건 재지 말고 무조건 신청 버튼부터 누르세요! 선착순이거나 1순위 뺑뺑이로 당첨되기 때문에 스피드가 생명입니다.</li>
</ul>
</div>
{get_survival_manual("매입임대")}
</div>"""
    elif "건설임대" in house:
        report += f"""<div class='card-box'>
<div class='card-title'>🔎 아파트(건설임대) 가점 관리 및 입주 공략 가이드</div>
보안이 취약한 빌라에서 벗어나 엘리베이터, 지하 주차장, 무인 택배함, 단지 내 헬스장과 도서관 등 완벽한 인프라가 갖춰진 쾌적한 대단지 아파트에 당당히 입주하는 로드맵입니다.<br>
<div class='action-box'>
<span class='highlight-blue'>면적의 법칙</span> <b>1인 가구 40㎡(12평) 강제 제한 룰을 반드시 이해하라</b>
<ul class='step-list'>
<li>국가 법령상, 혼자 사는 1인 가구는 아무리 돈이 많아도 전용면적 <b>40㎡(약 12평 내외)</b> 이하의 소형 평수에만 지원할 수 있도록 엄격하게 제한되어 있습니다. 나 혼자 쾌적하게 살겠다고 방 3개짜리 넓은 평수에 호기롭게 청약을 넣으면, 컴퓨터 서류 심사에서 묻지도 따지지도 않고 100% 탈락 처리됩니다.</li>
<li>만약 더 넓은 집으로 가고 싶다면? 결혼을 하거나 부모님, 형제를 모시고 와서 세대원 수를 {fam}처럼 늘려야만 59㎡(25평형) 이상의 넓은 집으로 상향 지원할 수 있는 자격이 주어집니다. 이것이 바로 생애주기에 맞춰 10년, 20년 로드맵을 치밀하게 짜야 하는 이유입니다.</li>
</ul>
</div>
<div class='tip-box'>
<span class='highlight-yellow'>가점의 비밀</span> <b>아파트 배점표 만점 싹쓸이 전략</b>
<p>아파트 입주는 1순위 자격을 가진 사람들 수천 명이 모여서 점수(배점)로 치열하게 줄을 섭니다. 남들을 밟고 올라가 합격증을 거머쥐려면 이 두 가지를 무조건 사수해야 합니다.</p>
<ul class='step-list'>
<li><b>인천 연속 거주 기간:</b> 인천에 주민등록상 주소지를 두고 오래 살수록 점수가 쑥쑥 올라갑니다. 직장이나 알바 때문에 잠깐 타 지역 고시원에 전입신고를 옮기는 순간, 그동안 공들여 쌓아온 인천 거주 점수가 0점으로 리셋되는 대참사가 발생하니 절대 주의하세요!</li>
<li><b>청약 납입 횟수:</b> 통장에 천만 원을 한 번에 일시불로 넣은 부자보다, 매달 2만 원씩 <span class='highlight-yellow'>60회(5년) 이상 꾸준히 연체 없이 납입</span>한 성실한 청년이 청약 점수에서 최고점(만점)을 받습니다. 자동이체는 여러분의 목숨줄입니다.</li>
</ul>
</div>
{get_survival_manual("건설임대")}
</div>"""
    elif "통합공공" in house:
        report += f"""<div class='card-box'>
<div class='card-title'>🔎 통합공공임대 : 소득이 올라도 안심하는 평생 주택</div>
기존에 국민임대, 영구임대, 행복주택 등으로 너무 복잡하게 쪼개져 있던 제도를 하나로 합친 2026년 최신 주거복지의 '끝판왕' 제도입니다.<br>
<div class='action-box'>
<span class='highlight-blue'>가장 큰 장점</span> <b>연봉이 올라도 절대 쫓겨나지 않습니다!</b>
<ul class='step-list'>
<li>과거의 임대 아파트는 열심히 일해서 연봉이 오르면 "소득 기준 초과"라며 얄짤없이 아파트에서 쫓아냈습니다. 하지만 통합공공임대는 내 소득이 올라가면 쫓아내는 대신, 그냥 그 높아진 소득 구간에 맞춰서 임대료만 조금 더 내며 <b>최장 30년 동안 이사 걱정 없이 평생</b> 살 수 있도록 법이 바뀌었습니다. 진정한 의미의 거주 사다리입니다.</li>
<li>가족 수에 비례하여 최대 84㎡(구 34평형)의 아주 넓은 아파트까지 넉넉하게 배정받을 수 있어 아이 키우기에 이보다 더 좋은 제도는 대한민국에 없습니다.</li>
</ul>
</div>
<div class='tip-box'>
<span class='highlight-yellow'>공략 포인트</span> <b>인천 신도시 신규 물량을 선점하라!</b>
<p>앞으로 인천의 검단신도시, 계양신도시, 부천 대장지구 등 쾌적하게 조성된 새 동네에서 어마어마한 물량의 통합공공임대 새 아파트 공고가 쏟아질 예정입니다. 특히 신생아가 있거나 맞벌이 부부일 경우 가산점을 폭격 수준으로 받으니 마이홈포털을 매일같이 들여다보며 기회를 노려야 합니다.</p>
</div>
{get_survival_manual("통합공공")}
</div>"""
    elif "분양" in house:
        report += f"""<div class='card-box'>
<div class='card-title'>🔎 공공분양 '뉴홈' - 내 집 마련, 내 성을 짓는 완벽한 전략</div>
우리 30년 주거 로드맵의 가장 찬란한 종착지입니다! LH의 '뉴홈' 브랜드를 통해 주변 민간 아파트(자이, 래미안 등) 시세의 70% 수준으로 완전히 내 명의의 튼튼한 집을 소유하는 궁극의 방법입니다.<br>
<div class='action-box'>
<span class='highlight-blue'>치명적 당첨 비결</span> <b>청약 인정 '총액'과 '특별공급'의 완벽한 콜라보</b>
<ul class='step-list'>
<li><b>인정 총액의 마법:</b> 임대 아파트는 '몇 번 냈느냐(횟수)'가 중요했지만, <b>공공 분양 아파트 당첨은 무조건 '총 납입 인정 금액'이 많은 사람 순서</b>대로 뽑아버립니다. 단, 한 달에 딱 10만 원까지만 인정해 줍니다. 경제적 여유가 생기는 즉시 은행에 가서 청약 자동이체 금액을 최고 한도인 <span class='highlight-blue'>월 10만 원</span>으로 끌어올려서 차곡차곡 총액을 불려야 당첨권에 들 수 있습니다.</li>
<li><b>특별공급(특공) 빈틈 노리기:</b> 아무런 조건 없는 일반공급은 경쟁률이 수백 대 일이라 당첨이 불가능에 가깝습니다. 우리는 전체 물량의 무려 70%나 배정된 <b>'생애최초 특별공급', '신혼부부 특별공급', '다자녀 특별공급'</b> 등 나에게 딱 맞는 좁은 문을 집중적으로 노려야 당첨 확률이 10배 이상 치솟습니다.</li>
</ul>
</div>
<div class='emergency-box'>
<span class='highlight-red'>🚨 절대 주의</span> <b>당첨 후 대출 심사(DSR) 철통 방어전</b>
<p>아파트 청약에 덜컥 당첨되었다고 기뻐하기엔 이릅니다. 집값의 80%를 국가에서 아주 싼 저금리(2%대) 모기지로 빌려주는데, 이때 은행에서 여러분의 과거 신용점수와 대출 기록을 현미경 보듯 샅샅이 뒤져봅니다.</p>
<ul class='step-list'>
<li>이때 <b>신용카드 현금서비스, 할부 리볼빙 서비스, 제2금융권(캐피탈) 카드론</b> 사용 이력이 하나라도 발견되면 신용등급이 대폭 깎여 수억 원의 대출이 전면 거절당합니다. 어렵게 당첨된 내 집을 대출이 안 나와서 눈앞에서 허무하게 날려버리는 끔찍한 비극을 맞지 않으려면, 20대 초반부터 신용 관리를 결벽증 수준으로 깨끗하게 유지해야 합니다. <span class='highlight-red'>자본주의 사회에서 신용은 곧 수억 원의 현찰입니다.</span></li>
</ul>
</div>
</div>"""
    return report

# =====================================================================
# [Step 8] 리포트 출력 메인
# =====================================================================
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵 백과사전</div>', unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:right; color:#7F8C8D; font-size:1rem; margin-bottom:10px;'><b>수신인:</b> {user_name} 님 | <b>발급기관:</b> 인천자립지원전담기관 | <b>담당 멘토:</b> 김정현</div>", unsafe_allow_html=True)

    # --- [섹션 1] 현재 상황 진단 ---
    st.markdown('<div class="section-title">Step 1. 현재의 나 : 출발선 정밀 진단과 비상 전략</div>', unsafe_allow_html=True)
    st.markdown(analyze_current_status(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # --- [섹션 2] 10년 후 성장기 ---
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 2. 10년 후 ({current_age+10}세) : 주거 기반 구축 가이드</div>', unsafe_allow_html=True)
    st.markdown(generate_future_roadmap(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # --- [섹션 3] 20년 후 안정기 ---
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 3. 20년 후 ({current_age+20}세) : 주거 안정 및 평수 상향 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_future_roadmap(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # --- [섹션 4] 30년 후 정착기 ---
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 4. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착 로드맵</div>', unsafe_allow_html=True)
    st.markdown(generate_future_roadmap(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # --- [섹션 5] 정보망 및 멘토의 편지 ---
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Step 5. 든든한 조력 정보망 및 멘토의 당부</div>', unsafe_allow_html=True)
    st.markdown("""<div class='card-box'>
<div class='card-title'>🌐 스마트폰 즐겨찾기에 꼭 등록해야 할 필수 생존 사이트</div>
<ul class='step-list'>
<li><b>LH 청약플러스 (https://apply.lh.or.kr)</b><br>
우리의 주거 자립을 책임지는 심장부입니다. 모든 실제 집 공고를 확인하고 청약을 신청하는 핵심 창구입니다. 반드시 스마트폰에 앱을 설치하고 '인천 관심지역 알림' 설정을 켜두세요.</li>
<li><b>마이홈 포털 (https://www.myhome.go.kr)</b><br>
전국 모든 주거 복지 제도를 아주 친절하게 검색할 수 있어요. 특히 '자가진단' 기능을 통해 내 나이와 소득으로 어떤 집에 들어갈 수 있는지 AI가 미리 계산해 주는 최고의 길잡이 사이트입니다.</li>
<li><b>자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
자립준비청년들만을 위해 주거, 교육, 금융, 심리 지원 정보를 모두 모아둔 전용 포털입니다. 여기서 생활비나 장학금 정보도 엄청나게 많이 얻을 수 있으니 주 1회 방문을 무조건 습관화하세요.</li>
<li><b>주택도시기금 (https://nhuf.molit.go.kr)</b><br>
나중에 민간 집으로 이사 갈 때, 나라에서 빌려주는 이자가 아주 저렴한 대출(청년전용 버팀목 전세자금, 내집마련 디딤돌 대출 등) 상품의 요건과 한도를 정확히 비교하고 조회할 수 있습니다. 은행 가기 전 필수 방문 코스입니다.</li>
</ul>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""<div class='card-box' style="background-color: #E8F8F5; border: 3px solid #1ABC9C; text-align: center; margin-top: 40px; box-shadow: 0 10px 20px rgba(26, 188, 156, 0.15);">
<h2 style="color: #117A65; margin-bottom: 20px;">언제든 편하게 연락 주세요! 📞</h2>
<p style="color: #212F3D; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.9; word-break: keep-all;">
세상에 혼자 덩그러니 남겨진 것 같아 두렵고 막막할 때가 분명히 있을 거예요.<br>
하지만 이 리포트가 당신이 길을 잃지 않도록 가장 든든한 지도가 되어줄 것입니다.<br><br>
이 로드맵을 보다가 어려운 말이 있거나, 집주인과 싸움이 났거나, 연체/수리 등 위기 상황이 생기면<br>
<b>절대 밤새 혼자 끙끙 앓으며 고민하지 말고 저에게 바로 전화나 카톡을 주세요.</b><br>
당신의 가장 든든한 내 편이자 방패가 되어, 함께 가장 좋은 길을 찾아 줄게요. 
<br>당신의 눈부신 홀로서기를 온 마음을 다해 응원합니다.
</p>
<hr style="border: 1px dashed #1ABC9C; width: 50%; margin: 35px auto;">
<div style="font-size: 1.5rem; font-weight: 900; color: #0E6251;">
👤 담당자 김정현 멘토 (☎ 070-7663-1153) 올림
</div>
</div>""", unsafe_allow_html=True)

    # =====================================================================
    # [Step 9] 🖨️ PDF 인쇄 실행 버튼 (움직이는 GIF 아이콘, 인쇄 시 자동 숨김)
    # =====================================================================
    st.markdown("---")
    components.html(
        """
        <div class="print-btn-container" style="text-align: center; margin-top: 20px; font-family: 'Noto Sans KR', sans-serif;">
            <a href="#" onclick="window.parent.print(); return false;" title="리포트 전체를 PDF로 예쁘게 저장하기" style="text-decoration: none;">
                <img src="https://media.giphy.com/media/ic06p9J076137681I3/giphy.gif" width="130px" style="border-radius:50%; box-shadow: 0 8px 20px rgba(0,0,0,0.15); cursor:pointer; transition: transform 0.2s ease-in-out;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            </a>
            <p style="color: #7F8C8D; font-size: 15px; margin-top: 20px; font-weight: bold;">
                👆 춤추는 집 요정을 누르면 백과사전 전체가 A4 규격으로 완벽하게 자동 분할되어 출력(저장)됩니다!
            </p>
        </div>
        """,
        height=250
    )