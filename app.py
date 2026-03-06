import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (가독성 극대화 및 🖨️ PDF 전체 페이지 인쇄 완벽 제어)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #E5E8E8; margin-bottom: 20px; line-height: 1.8;}
    .tip-box { background-color: #F9E79F; padding: 22px; border-radius: 8px; border-left: 6px solid #F1C40F; margin-top: 15px; margin-bottom: 15px; color: #4D5656; font-size: 1rem; line-height: 1.7;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }
    
    /* 🖨️ PDF 전체 화면 인쇄를 위한 마법의 CSS (스트림릿 스크롤 강제 해제) */
    @media print {
        /* 1. 인쇄 시 불필요한 입력 폼, 사이드바, 헤더, 버튼 등 완벽하게 숨기기 */
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        
        /* 2. 🌟 핵심: 스크롤이 있는 모든 컨테이너의 높이 제한을 풀고 블록 형태로 전환 🌟 */
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"] {
            height: auto !important;
            min-height: 100% !important;
            overflow: visible !important;
            display: block !important;
            position: relative !important;
            background-color: white !important;
        }
        
        /* 3. 각 단계별로 무조건 새로운 A4 용지로 넘기기 */
        .page-break {
            page-break-before: always !important;
            display: block !important;
            height: 0px !important;
            border: none !important;
        }
        
        /* 4. 인쇄할 때 배경색(노란 박스 등)이 하얗게 날아가는 현상 방지 */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 속도에 맞춰 그리는 30년 맞춤형 주거 플랜 백과사전</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass
st.divider()

# 2. 30년 생애주기 입력 폼
st.subheader("📋 Step 1. 나의 30년 주거 계획 세우기")

fam_options = ["1인 가구 (혼자 살아요)", "2인 가구 (부부/형제와 살아요)", "3인 가구 (아이 1명과 살아요)", "4인 이상 (다자녀 가정이에요)"]
house_options = [
    "전세임대 (내가 원하는 동네의 민간주택을 찾을래요)", 
    "매입임대 (LH가 미리 사둔 튼튼한 빌라/오피스텔이 좋아요)", 
    "건설임대 (안전하고 쾌적한 국민/행복 아파트에 살래요)", 
    "통합공공임대 (소득연계형, 이사 안 가고 30년 살래요)", 
    "공공분양 (마지막엔 완전히 내 집을 소유하고 싶어요)"
]
current_house_options = [
    "LH 전세임대 (소년소녀가정 등 혜택 거주 중)",
    "LH 전세/매입임대 (자립준비청년 혜택 거주 중)",
    "일반 무상거주 (시설, 친척집, 지인 등)",
    "일반 민간 임대 (개인적으로 월세/전세 계약)",
    "주거취약계층 (고시원, 여관 등 임시 거주)"
]

with st.form("lifecycle_form"):
    st.info("💡 삶의 모습은 언제든 변할 수 있으니 너무 부담 갖지 마세요. 편안하게 골라주면 돼요!")
    
    st.markdown("#### 📌 [현재] 출발선 확인하기")
    user_name = st.text_input("👤 이름이 무엇인가요?", "김자립")
    col1, col2 = st.columns(2)
    with col1:
        current_age = st.number_input("🎂 현재 나이는요?", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 모아둔 자산 (단위: 만원)", min_value=0, value=100)
    with col2:
        is_vulnerable = st.checkbox("보호종료(자립준비) 청년에 해당하나요?", value=True)
        now_sub = st.radio("🏦 주택청약통장이 있나요?", ["네, 가입해서 넣고 있어요", "아니요, 없거나 쉬고 있어요"])
        
    now_house = st.selectbox("🏠 지금은 어떤 곳에서 지내고 있나요?", current_house_options)

    st.markdown("---")
    st.markdown("#### 🌱 [10년 후] 주거 목표")
    fam_10 = st.selectbox("10년 후에는 몇 명과 함께 살고 싶나요?", fam_options, index=0)
    house_10 = st.selectbox("10년 후 어떤 형태의 집에서 살고 싶나요?", house_options, index=1)
    sub_10 = st.checkbox("10년 후에도 청약 통장을 계속 유지할 예정이에요", value=True)

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후에는 몇 명과 함께 살고 싶나요?", fam_options, index=1)
    house_20 = st.selectbox("20년 후 어떤 형태의 집에서 살고 싶나요?", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 통장을 계속 유지할 예정이에요", value=True)

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립 목표")
    fam_30 = st.selectbox("30년 후에는 몇 명과 함께 살고 싶나요?", fam_options, index=2)
    house_30 = st.selectbox("가장 마지막에 이루고 싶은 주거의 모습은요?", house_options, index=4)
    sub_30 = st.checkbox("모아둔 청약 통장으로 공공분양에 도전할 예정이에요", value=True)

    st.write("")
    submit_btn = st.form_submit_button("🚀 나만의 맞춤형 로드맵 리포트 만들기", type="primary")

# 3. 분석 알고리즘 (현재 빵빵한 디테일)
def analyze_current(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
        🏦 <b>청약 통장, 왜 지금 당장 만들어야 할까요?</b><br>
        현재 청약 통장이 없거나 잠시 쉬고 계시군요! 청약 통장은 단순히 돈을 모으는 적금이 아니에요. 나중에 LH 아파트(건설임대)에 들어가거나 내 집 마련(공공분양)을 할 때 꼭 필요한 <b>'무적의 입장권'</b>과 같답니다. 이 입장권이 없으면 남들이 다 들어가는 좋은 아파트에 지원조차 해볼 수 없어요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        당장 모아둔 돈이 없어도 괜찮아요! 은행에 가서 <b>'청년주택드림청약통장'</b>을 만들어 달라고 꼭 말씀하세요. 일반 청약보다 이자가 최대 4.5%로 훨씬 높아서 혜택이 정말 좋아요. 매월 2만 원씩이라도 자동이체를 걸어두면, 그 '횟수'가 차곡차곡 쌓여서 나중에 서류 심사에서 엄청난 가산점(최대 6점)이 되어 돌아올 거예요. 당장 내일, 신분증을 챙겨서 가까운 은행에 꼭 방문해 보는 걸 추천해요!
        </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
        🏦 <b>청약 통장 유지, 100점 만점에 200점이에요!</b><br>
        지금처럼 연체 없이 꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 엄청난 무기(가산점)가 될 거예요. 공공분양이나 임대주택 심사에서는 한 번에 큰돈을 넣은 사람보다, 소액이라도 <b>'오래, 꾸준히 낸 사람'</b>을 훨씬 우대하고 좋아한답니다. 정말 훌륭하게 잘하고 계세요!<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        우리가 살다 보면 갑자기 목돈이 급하게 필요해서 청약 통장을 깨고 싶어지는 아찔한 순간이 올 수도 있어요. 그럴 땐 <b>절대 통장을 해지하지 말고, 은행에 가서 '청약예금 담보대출'을 물어보세요.</b> 내가 넣은 돈의 90%까지 아주 저렴한 이자로 빌릴 수 있어서, 통장의 점수(생명력)를 깨지 않고도 위기를 넘길 수 있답니다. 소중한 입장권을 끝까지 지켜내 보아요!
        </div>
        </div>
        """

    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 소년소녀가정 전세임대 거주 중</b><br>
        현재 살고 계신 전형은 만 20세까지 나라에서 전세지원금에 대한 이자를 '전액 면제'해 주는 최고의 혜택을 가지고 있어요. 주거비 걱정 없이 온전히 학업이나 나의 성장에만 집중할 수 있는 아주 소중한 시기랍니다.<br><br>
        <ul class='step-list'>
            <li><b>꼭 기억해야 할 점:</b> 영원히 무료는 아니에요! 만 22세 이후부터는 전세금에 대한 소정의 임대료(이자, 약 1~2% 수준)를 매달 LH에 납부해야 한답니다.</li>
            <li><b>미리 준비할 점:</b> 주거비가 0원으로 전혀 나가지 않는 지금 시기에, 나중에 낼 이자나 더 넓은 집으로의 독립 자금을 위해 <b>매월 10~20만 원씩은 꼭 없는 돈이라 생각하고 적금으로 저축</b>해 두는 것을 강력히 추천해요.</li>
        </ul>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        전세임대 지원 한도(수도권 약 1.2억 원) 안에서 이사할 일이 생기면, 내 돈으로 도배를 하지 말고 꼭 <b>LH 도배/장판 지원금 혜택(1회 한정, 약 60만 원 한도)</b>을 신청하세요. 쾌적한 환경에서 지내는 것도 자립의 아주 중요한 부분이랍니다.
        </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 자립준비청년 전세/매입임대 거주 중</b><br>
        보호가 종료된 후 5년 동안 임대료를 무려 50%나 할인받고 계시군요! 정말 현명한 선택으로 안전한 울타리를 마련하셨어요. 지금은 주거비가 크게 절약되어 든든하게 받쳐주고 있으니, 이제는 다가올 미래를 차분히 준비할 타이밍이에요.<br><br>
        <ul class='step-list'>
            <li><b>특례 종료 대비:</b> 5년이라는 혜택 기간이 끝나면, 일반 청년 전형으로 전환되면서 임대료 할인이 끝나고 원래대로 100% 청구될 거예요. 갑자기 월세가 두 배로 뛰는 느낌이 들어 당황할 수 있어요.</li>
        </ul>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁 (상호전환제도)</b><br>
        이때를 대비해 LH의 마법 같은 <b>'전환보증금 제도'</b>를 꼭 활용해 보세요! 여유 자금을 보증금으로 추가 납부하면, 무려 연 6~7%의 이율로 쳐서 매월 내는 월세를 확 깎아준답니다. 은행 예금 이자보다 훨씬 높은 혜택이니, 현재 모아두신 {assets}만 원이나 알바를 통해 목돈이 생길 때마다 보증금으로 돌려서 월세를 '치킨 한 마리 값'으로 만들어 보세요!
        </div>
        </div>
        """
    elif "무상거주" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 무상거주 (시설/친인척/지인 등)</b><br>
        매달 내 통장에서 고정적으로 빠져나가는 집세(월세, 관리비 등)가 없는 지금이 바로 여러분의 인생에서 <b>'종잣돈을 모을 수 있는 절대적인 골든타임'</b>이에요! 이 시기에 돈을 어떻게 관리하느냐에 따라 10년 뒤 나의 통장 잔고가 완전히 달라질 수 있어요.<br><br>
        <ul class='step-list'>
            <li><b>자금 묶어두기:</b> 통장에 들어오는 자립정착금이나 자립수당 등 큰돈은 절대 기분 따라 꺼내 쓸 수 없도록 '청년도약계좌'나 해지하기 어려운 적금에 단단히 묶어두는 것을 진심으로 추천해요.</li>
        </ul>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        지금 당장 급하게 집을 구해서 나가야 하는 상황이 아니라면, 여러분이 가진 <b>'자립준비청년 1순위 자격'</b>이라는 엄청난 카드를 잘 아껴두세요. 목돈이 충분히 모이고 확실하게 독립할 준비가 되었을 때, 이 1순위 카드를 멋지게 꺼내서 LH 매입임대나 전세임대로 안전하게 첫발을 내딛는 계획을 짜보아요.
        </div>
        </div>
        """
    elif "일반 민간 임대" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 일반 민간 임대 (월세/전세)</b><br>
        어린 나이에 스스로 집을 구해서 독립을 하시다니 정말 대단해요! 하지만, 매달 집주인에게 내야 하는 높은 월세나 은행에 갚는 전세 대출 이자는 여러분이 앞으로 자산을 모으는 데 가장 큰 걸림돌이 될 수 있어요. 게다가 요즘 뉴스에 많이 나오는 전세사기 같은 위험도 절대 무시할 수 없답니다.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        여러분에게는 일반 청년들보다 훨씬 유리하게, 보증금 100만 원이라는 아주 적은 돈으로도 들어갈 수 있는 <b>'LH 자립준비청년 1순위 전형'</b>이라는 막강한 방패가 있어요! 아까운 내 돈이 비싼 월세로 허무하게 새어나가지 않도록, 담당자와 함께 LH 주택으로 이사 갈 수 있는 방법을 꼭, 지금 당장 긍정적으로 검토해 보길 진심으로 추천해요.
        </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 고시원 등 주거취약계층 거주 중</b><br>
        지금 지내는 곳이 너무 비좁고 마음이 쓰이시죠? 무엇보다 여러분의 일상에서 '안전하고 따뜻한 잠자리'가 가장 중요해요. "내 힘으로 다 이겨내고 해결해야 해"라고 혼자서 무거운 짐을 지려 하지 마세요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 실전 꿀팁</b><br>
        정부에는 여러분을 돕기 위한 <b>'주거취약계층 주거상향 지원사업'</b>이라는 아주 훌륭하고 따뜻한 제도가 있어요. 고시원이나 여관, 비닐하우스 등에 거주하는 분들이 보증금 부담 없이 쾌적한 공공임대주택으로 이사할 수 있도록 <b>이사비용, 생활 필수 가전제품, 그리고 보증금까지 싹 다 알아서 지원</b>해 주는 제도랍니다. 망설일 이유가 전혀 없어요. 이 글을 읽으셨다면 편하게 담당자에게 꼭 연락해서 새로운 집으로 갈 수 있게 도움을 받아보세요!
        </div>
        </div>
        """
    return report

# 4. 분석 알고리즘 (미래 로드맵 빵빵한 디테일)
def generate_future(age, fam, house, sub_status):
    report = f"<div class='card-box'>👨‍👩‍👧‍👦 <b>목표 가구 구성:</b> {fam}<br>🏡 <b>목표 주거 전형:</b> {house}</div>"
    
    # 청약 유지 여부 피드백 
    if not sub_status:
        report += """
        <div class='card-box'>
        🏦 <b>앗, 청약 납입을 잠시 쉬기로 하셨군요!</b><br>
        살다 보면 경제적으로 힘든 시기가 와서 어쩔 수 없이 납입을 잠시 멈출 수는 있어요. 하지만 청약 통장의 생명력이 멈춰버리면 나중에 좋은 아파트(건설임대)나 내 집 마련(분양) 경쟁을 할 때 순위가 다른 사람보다 뒤로 밀릴 수 있답니다. 주머니 사정에 여유가 조금이라도 생기는 순간, 다시 은행에 가서 꼭 월 2만 원씩이라도 이어나가 보기를 다정하게 권유해 드려요!
        </div>
        """

    if "전세임대" in house:
        if age < 40:
            title = "🔎 청년/신혼부부 전세임대, 하나부터 열까지 알려줄게요!"
            desc = f"지금 계획하신 {age}세 즈음에는 청년이나 신혼부부를 위한 전세임대를 적극 활용해 볼 수 있어요. 내가 살고 싶은 동네의 맘에 드는 집을 직접 찾아오면, LH가 집주인과 전세계약을 맺고 나에게 다시 저렴하게 빌려주는 아주 자유롭고 유연한 제도랍니다."
        else:
            title = "🔎 일반/다자녀 전세임대, 하나부터 열까지 알려줄게요!"
            desc = f"{age}세가 되신 시점이라면, 청년 특례보다는 소득 기준에 맞춘 일반 전세임대나 가족 수에 혜택을 주는 다자녀 전세임대를 활용해 볼 수 있어요. 직장이나 아이들 학교 등 거주지를 자유롭게 선택할 수 있어 {fam}의 라이프스타일에 맞추기 아주 좋답니다."
            
        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <ul class='step-list'>
                <li><b>신청 시기:</b> 보통 <b>1월~2월 연초</b>에 모집 공고가 한꺼번에 쏟아지니 이때 LH청약플러스 앱을 꼭 확인하세요.</li>
                <li><b>지원 한도:</b> 가구원 수에 따라 다르지만 수도권 기준 약 1.2억 원~1.5억 원까지 넉넉하게 지원해 주며, 여러분은 지원받는 금액의 딱 5% 정도만 본인 보증금으로 준비하면 돼요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 권리분석(안전한 집 찾기) 핵심 꿀팁</b><br>
            LH는 여러분의 보증금을 지키기 위해 정말 깐깐한 심사를 해요. 집주인이 은행에 빚이 많으면 나중에 보증금을 돌려받지 못할 수 있어서 심사에서 가차 없이 탈락시킵니다. 이걸 '권리분석'이라고 불러요.<br>
            👉 <b>절대 원칙: (집주인 빚 + 내 보증금)이 주택 가격의 90%를 넘으면 안 돼요!</b><br>
            그러니 부동산에 가서 집을 찾을 때, 이것저것 보지 말고 처음부터 당당하게 말씀하세요. <i>"사장님, 저 LH 전세임대 구하는데요, 부채비율 90% 이하로 권리분석 무조건 통과할 수 있는 융자 없고 깨끗한 안전한 집만 보여주세요!"</i> 이렇게 말하면 사장님도 딱 맞는 집만 찾아주셔서 헛걸음하는 시간을 확 줄일 수 있답니다.
            </div>
        </div>
        """
        
    elif "매입임대" in house:
        if age < 40:
            title = "🔎 청년/신혼부부 매입임대, 하나부터 열까지 알려줄게요!"
            desc = "LH가 도심 곳곳에 튼튼하게 지어진 빌라나 오피스텔을 통째로 사들여서 우리에게 시세보다 훨씬 저렴하게 빌려주는 훌륭한 제도예요. 집주인이 개인이 아니라 '국가(LH)'이기 때문에 전세사기를 당할 걱정이 0%랍니다!"
        else:
            title = "🔎 일반/고령자 매입임대, 하나부터 열까지 알려줄게요!"
            desc = f"연령대가 높아질수록 계단 오르기 등 거주 환경의 편리함이 중요해져요. {age}세 시점에는 일반 매입임대나 건강 상황에 맞춰 1층을 우선 배정해 주는 우대 전형 등 안전하고 편안한 주택을 1순위로 노려볼 수 있어요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <ul class='step-list'>
                <li><b>신청 시기:</b> 보통 <b>3월, 6월, 9월, 12월 이렇게 분기별</b>로 크게 정기 모집 공고가 올라와요.</li>
                <li><b>옵션 혜택:</b> 냉장고나 세탁기, 에어컨, 책상 같은 기본 가전/가구 옵션이 풀세트로 갖춰진 곳이 많아서 처음 이사 갈 때 비용을 아끼기에 너무너무 좋아요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '관심지역 알림'과 '줍줍' 특급 꿀팁</b><br>
            매입임대는 인기가 하늘을 찌르지만, 의외로 계약 당일에 포기하는 사람들이 생겨서 남는 빈집이 꼭 나옵니다. 이걸 우리가 '수시모집(줍줍)'이라고 부르는데, 보통 매주 금요일 오후에 홈페이지에 조용히 올라와요.<br>
            👉 <b>스마트폰에 'LH청약플러스' 앱을 깔고 마이페이지에 들어가서 [관심지역 알림]을 '인천광역시'로 꼭 켜두세요!</b> 알람이 울리자마자 남들보다 빠르게 빈집 정보를 낚아챌 수 있는 실무자들만 아는 최고의 비법이랍니다.
            </div>
        </div>
        """
        
    elif "건설임대" in house:
        if age < 40:
            title = "🔎 행복주택/국민임대 아파트, 하나부터 열까지 알려줄게요!"
            desc = "빌라가 아닌, 새로 지어지는 깨끗한 대단지 아파트에 입주할 수 있는 기회예요. 단지 안에 경비실도 있고 헬스장이나 작은 도서관, 놀이터도 있어서 생활의 질이 아주 쾌적해진답니다."
        else:
            title = "🔎 국민임대/영구임대 아파트, 안정적인 장기 거주를 준비해 봐요!"
            desc = f"{age}세 이후에는 잦은 이사로 에너지를 낭비하기보다 한 곳에 짐을 풀고 정착하는 것이 중요하죠. 소득 요건만 잘 유지한다면 국민임대 아파트에서 최장 30년까지 마음 편히 거주할 수 있는 아주 든든한 전형이에요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <ul class='step-list'>
                <li><b>가구원 수에 따른 면적 제한 (매우 중요):</b> 혼자 사는 1인 가구는 전용면적 40㎡(약 12평) 이하의 소형 평수만 지원할 수 있도록 법으로 정해져 있어요. 혼자 살면서 넓은 평수에 무작정 지원하면 서류에서 100% 탈락하니, 꼭 {fam} 기준에 맞는 평수를 지원하셔야 해요!</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '배점표' 만점받기 꿀팁</b><br>
            인기 있는 아파트는 1순위 자격을 가진 사람들끼리 모여서 점수(배점)로 다시 줄을 세워요. 여기서 남들을 이길 수 있는 두 가지 핵심 무기를 알려드릴게요.<br>
            1. <b>해당 지역 거주 기간:</b> 인천광역시에 주소지를 두고 오래 살수록 유리해요. (이사 갈 일이 없는데 타 지역으로 전입신고를 맘대로 옮기면 그동안 쌓은 거주 점수가 싹 날아갈 수 있어요!)<br>
            2. <b>청약 통장 납입 횟수:</b> 통장에 돈이 얼마나 많은지 액수보다 <b>'얼마나 연체 없이 다달이 꾸준히 냈는지'</b>가 훨씬 중요해요. 60회(5년) 이상 꾸준히 납입하면 여기서 6점 최고점을 싹쓸이할 수 있답니다.
            </div>
        </div>
        """
        
    elif "통합공공" in house:
        if age < 40:
            title = "🔎 통합공공임대, 첫 입주를 지혜롭게 노려봐요!"
            desc = "기존에 영구임대, 국민임대, 행복주택 등으로 복잡하게 나뉘어 있던 제도를 하나로 합친 2026년 최신 버전의 주거복지 끝판왕 제도예요. 특히 신혼부부나 신생아 출산 가정을 위한 특별공급을 활용하면 아주 유리하게 첫 입주를 할 수 있어요."
        else:
            title = "🔎 통합공공임대, 30년 안심 거주를 누려봐요!"
            desc = f"{age}세 시점에는 여러분의 연봉이나 소득이 예전보다 훨씬 올랐을 수 있어요. 과거에는 월급이 오르면 임대아파트에서 나가라고 했지만, 이 전형은 소득이 올라도 쫓겨나지 않고 소득에 맞춰 임대료만 조금 더 내며 30년 동안 이사 안 가고 평생 살 수 있는 최고의 방패랍니다."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <ul class='step-list'>
                <li><b>평형 선택의 엄청난 자유:</b> 기존 임대주택은 좁은 집만 갈 수 있었지만, 통합공공임대는 {fam}의 인원수에 맞춰서 최대 84㎡(약 34평형) 아파트까지 지원할 수 있어서 주거 환경이 획기적으로 좋아져요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 전략적 준비 꿀팁</b><br>
            맞벌이를 하거나 자녀를 둔 다자녀 가정이 될수록 가산점을 듬뿍듬뿍 받을 수 있는 유리한 전형이에요. 앞으로 인천의 검단신도시나 계양신도시 같은 새로운 동네에서 새 아파트 모집 공고가 쏟아질 테니, 마이홈포털 등에서 공고문을 꾸준히 확인해 보는 것을 적극 추천해요.
            </div>
        </div>
        """
        
    elif "분양" in house:
        if age < 40:
            title = "🔎 공공분양(뉴홈), 생애 첫 내 집 마련의 꿈을 이루는 법!"
            desc = "30년 로드맵의 가장 멋진 목표네요! LH의 '뉴홈' 브랜드를 통해 주변 민간 아파트 시세의 70% 수준으로 아주 저렴하게 새 아파트를 분양받아 완전한 내 집을 가질 수 있는 절호의 기회랍니다."
        else:
            title = "🔎 공공분양, 영구적인 내 집을 가져봐요!"
            desc = f"{age}세까지 차곡차곡 인내심을 갖고 모아둔 청약 통장의 힘을 폭발시킬 때예요! 그동안 쌓인 '납입 인정 금액'으로 일반공급에 당당히 도전하거나, 특별공급을 통해 온전하고 여유로운 내 집을 마련해 볼 수 있어요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <ul class='step-list'>
                <li><b>특별공급(특공) 절대 공략:</b> 일반 사람들과 섞여서 경쟁하기엔 너무 치열해요. 우리는 {fam} 상황에 꼭 맞춰서 <b>'생애최초 특공', '신혼부부 특공', '다자녀 특공'</b>이라는 덜 막히는 마법의 문을 두드릴 거예요. 전체 아파트 물량의 무려 70%가 특공에 배정되어 있답니다!</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 분양 당첨과 신용관리(DSR) 진짜 꿀팁</b><br>
            1. <b>청약 통장 인정 금액:</b> 분양 당첨은 횟수가 아니라 <b>'매월 최대 10만 원씩 통장에 인정받은 총 누적 금액'</b>이 많은 순서대로 줄을 세워서 뽑아요. 경제적 여유가 생기면 무조건 당장 월 10만 원으로 청약 자동이체 금액을 꽉 채워 올려두세요.<br>
            2. <b>신용점수 철통 방어:</b> 분양에 당첨되었다고 끝이 아니에요! 집값의 최대 80%까지 나라에서 아주 싼 이자로 빌려주는 대출(모기지)을 일으키려면, 여러분의 은행 신용점수가 무조건 좋아야 해요. <b>잦은 신용카드 현금서비스, 할부 리볼빙, 무분별한 카드론 사용</b>은 대출 심사(DSR)에서 치명적인 독이 되니 20대부터 신용 관리를 깨끗하게 해주세요!
            </div>
        </div>
        """
    return report

# 5. 리포트 출력 및 PDF 버튼
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 섹션 1 (현재) - 이 내용부터 인쇄 1페이지 시작
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 튼튼하게 다지기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2 (10년 후) - 여기서부터 PDF 2페이지로 넘어감
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # 섹션 3 (20년 후) - 여기서부터 PDF 3페이지로 넘어감
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # 섹션 4 (30년 후) - 여기서부터 PDF 4페이지로 넘어감
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 영구적인 주거 자립 달성</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # 섹션 5 & 6 (도움망 및 편지) - 여기서부터 PDF 5페이지 (마지막 장)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5. 든든한 주거복지 정보망 (즐겨찾기 필수 사이트)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr/)</b><br>
        실제 집 공고를 보고 청약을 신청하는 공식 사이트예요. 스마트폰에 앱을 꼭 다운로드하시고 '관심지역(인천) 알림'을 켜두는 것을 강력히 추천해요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr/)</b><br>
        전국 모든 종류의 주거복지 제도를 한눈에 보여주는 길잡이 곳이에요. '자가진단' 메뉴를 누르면 내 나이와 소득에 딱 맞는 제도를 컴퓨터가 알아서 찾아준답니다.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr/)</b><br>
        자립준비청년들만을 위해 주거뿐만 아니라 장학금, 금융, 취업 정보까지 모두 모아둔 정말 유용한 전용 포털이에요. 자주 들어가 볼수록 돈이 되는 정보가 가득해요.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr/)</b><br>
        나중에 전셋집을 구하거나 집을 살 때, 이자가 아주 저렴한 나라의 대출 상품(청년전용 버팀목, 디딤돌 대출 등)을 알아볼 수 있는 공식 창구랍니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                사람마다 처한 상황이 다르고, 세워둔 계획은 살면서 언제든 변할 수 있어요.<br>
                단순히 막연하게 공고를 기다리기보다는 미리 요건을 차근차근 준비하는 것이 좋은 결과를 얻는 가장 빠른 지름길입니다.<br><br>
                이 로드맵을 보다가 어려운 말이 있거나, 내 상황에 맞게 계획을 조금 수정하고 싶다면 <b>절대 혼자 고민하지 마세요.</b><br>
                당신의 든든한 내 편이 되어 언제든 함께 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)