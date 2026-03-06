import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (가독성 + PDF 인쇄용 페이지 분할 속성 추가)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.7rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 50px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 40px; margin-bottom: 15px;}
    .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #E5E8E8; margin-bottom: 20px; line-height: 1.8;}
    .highlight-text { color: #16A085; font-weight: bold;}
    .tip-box { background-color: #F9E79F; padding: 20px; border-radius: 8px; border-left: 6px solid #F1C40F; margin-top: 15px; margin-bottom: 15px; color: #4D5656; font-size: 0.95rem; line-height: 1.7;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }
    
    /* 🖨️ PDF 인쇄 및 프린트를 위한 마법의 CSS */
    @media print {
        /* 각 단계별로 페이지를 무조건 새로 넘김 */
        .page-break { page-break-before: always !important; }
        
        /* 인쇄할 때 배경색과 테두리가 투명해지는 것을 방지 (원래 색상 그대로 출력) */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        
        /* 인쇄 시 불필요한 스트림릿 기본 메뉴, 헤더, 푸터, 버튼 등 숨기기 */
        header, footer, .stButton { display: none !important; }
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
    st.info("💡 삶의 모습은 언제든 변할 수 있으니 너무 부담 갖지 마세요. 지금 생각하는 가장 이상적인 모습을 편안하게 골라주면 돼요!")
    
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
    house_10 = st.selectbox("어떤 형태의 집에서 살고 싶나요?", house_options, index=1)
    sub_10 = st.checkbox("그때도 청약 통장을 깨지 않고 계속 유지할 수 있을까요?", value=True)

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후에는 몇 명과 함께 살고 싶나요?", fam_options, index=1)
    house_20 = st.selectbox("어떤 형태의 집에서 살고 싶나요?", house_options, index=3)

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립 목표")
    fam_30 = st.selectbox("30년 후에는 몇 명과 함께 살고 싶나요?", fam_options, index=2)
    house_30 = st.selectbox("가장 마지막에 이루고 싶은 주거의 모습은요?", house_options, index=4)

    st.write("")
    submit_btn = st.form_submit_button("🚀 나만의 맞춤형 로드맵 리포트 만들기", type="primary")


# 3. 디테일이 꽉 찬 분석 알고리즘 (동일)
def analyze_current(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
        🏦 <b>청약 통장, 왜 지금 바로 만들어야 할까요?</b><br>
        지금 청약 통장이 없거나 쉬고 계시군요! 청약 통장은 단순히 돈을 모으는 적금이 아니라, <b>'아파트에 들어갈 수 있는 입장권'</b>과 같아요. 나중에 LH 아파트(건설임대)에 들어가거나 내 집 마련(공공분양)을 할 때 이 입장권이 없으면 아예 지원조차 할 수 없답니다.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        여유가 당장 없더라도 괜찮아요. 은행에 가서 <b>'청년주택드림청약통장'</b>을 만들어 달라고 하세요. (일반 청약보다 이자가 최대 4.5%로 훨씬 높아요!) 매월 2만 원씩이라도 자동이체를 걸어두면, 그 '횟수'가 나중에 엄청난 가산점(최대 6점)이 되어 돌아올 거예요. 당장 내일, 신분증을 챙겨서 가까운 은행에 방문해 보는 건 어떨까요?
        </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
        🏦 <b>청약 통장 유지, 100점 만점에 200점이에요!</b><br>
        지금처럼 연체 없이 꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 엄청난 가산점이 될 거예요. 공공분양이나 임대주택은 금액이 많은 것보다 <b>'오래, 꾸준히 낸 사람'</b>을 훨씬 좋아한답니다.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        혹시라도 살다가 너무 급하게 목돈이 필요해서 청약 통장을 깨고 싶어지는 순간이 올 수도 있어요. 그럴 땐 <b>절대 해지하지 말고, '청약예금 담보대출'을 알아보세요.</b> 통장을 깨지 않고도 내가 넣은 돈의 90%까지 아주 싼 이자로 빌릴 수 있답니다. 우리의 입장권은 소중하니까 끝까지 지켜내 보아요!
        </div>
        </div>
        """

    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 소년소녀가정 전세임대 거주 중</b><br>
        현재 살고 계신 전형은 만 20세까지 나라에서 전세지원금에 대한 이자를 전액 면제해 주는 최고의 혜택을 가지고 있어요. 주거비 걱정 없이 학업이나 일에 집중할 수 있는 아주 소중한 시기랍니다.<br><br>
        <ul class='step-list'>
            <li><b>주의할 점:</b> 만 22세 이후부터는 전세금에 대한 소정의 임대료(이자, 약 1~2% 수준)를 매달 납부해야 해요.</li>
            <li><b>준비할 점:</b> 주거비가 전혀 나가지 않는 지금 시기에, 나중에 낼 이자나 독립 자금을 위해 매월 10~20만 원씩은 꼭 없는 돈이라 생각하고 저축해 두는 것을 추천해요.</li>
        </ul>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        지원 한도(수도권 약 1.2억 원) 안에서 이사할 일이 생기면, 꼭 도배/장판 지원금 혜택(1회 약 60만 원 한도)을 신청하세요. 쾌적한 환경에서 지내는 것도 자립의 중요한 부분이랍니다.
        </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 자립준비청년 전세/매입임대 거주 중</b><br>
        보호가 종료된 후 5년 동안 임대료를 50%나 할인받고 계시군요! 정말 현명한 선택을 하셨어요. 지금은 주거 안정이 든든하게 받쳐주고 있으니, 이제는 다가올 미래를 준비할 타이밍이에요.<br><br>
        <ul class='step-list'>
            <li><b>특례 종료 대비:</b> 5년이라는 혜택 기간이 끝나면, 일반 청년 전형으로 바뀌면서 임대료가 원래대로 100% 청구될 거예요. 체감상 월세가 두 배로 뛰는 느낌이 들 수 있어요.</li>
            <li><b>보증금 활용법:</b> 이 충격을 줄이기 위해 지금 모아두신 {assets}만 원을 잘 활용할 수 있어요.</li>
        </ul>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁 (상호전환제도)</b><br>
        LH에는 <b>'전환보증금 제도'</b>라는 마법 같은 제도가 있어요. 여유 자금을 보증금으로 추가 납부하면, 무려 연 6~7%의 이율로 계산해서 매월 내는 월세를 확 깎아준답니다. 은행 예금 이자보다 훨씬 높은 수익률이니, 목돈이 생길 때마다 보증금으로 전환해서 월세를 '치킨 한 마리 값'으로 만들어 보세요!
        </div>
        </div>
        """
    elif "무상거주" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 무상거주 (시설/친인척/지인 등)</b><br>
        매달 나가는 고정적인 집세(월세, 관리비 등)가 없는 지금이 바로 여러분의 인생에서 <b>'종잣돈을 모을 수 있는 절대적인 골든타임'</b>이에요! 이 시기를 어떻게 보내느냐에 따라 10년 뒤의 모습이 완전히 달라질 수 있어요.<br><br>
        <ul class='step-list'>
            <li><b>자금 묶어두기:</b> 자립정착금이나 자립수당 등 들어오는 목돈은 절대 쉽게 꺼내 쓸 수 없도록 '청년도약계좌'나 적금에 단단히 묶어두는 것을 추천해요.</li>
            <li><b>독립 준비:</b> 무상거주 기간 동안 자립준비청년 1순위 자격을 잘 아껴두었다가, 확실하게 독립할 준비가 되었을 때 LH 매입임대나 전세임대로 안전하게 첫발을 내딛어 보아요.</li>
        </ul>
        </div>
        """
    elif "일반 민간 임대" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 일반 민간 임대 (월세/전세)</b><br>
        개인적으로 집을 구해서 지내고 계시군요. 훌륭한 독립이지만, 매달 나가는 높은 월세나 전세 대출 이자는 우리가 자산을 모으는 데 가장 큰 적이 될 수 있어요. 게다가 요즘은 전세사기 같은 위험도 무시할 수 없잖아요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        여러분에게는 일반인들보다 훨씬 유리하게, 보증금 100만 원 수준으로도 들어갈 수 있는 <b>'LH 자립준비청년 1순위 전형'</b>이라는 강력한 카드가 있어요! 비싼 월세로 돈이 새어나가지 않도록, 담당자와 함께 LH 주택으로 이사 갈 방법을 지금 당장 긍정적으로 검토해 보길 진심으로 권장해요.
        </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 고시원 등 주거취약계층 거주 중</b><br>
        지금 지내는 곳이 답답하거나 마음이 쓰이시죠? 무엇보다 여러분의 안전과 따뜻한 잠자리가 가장 중요해요. 혼자서 "내 힘으로 다 해결해야 해"라고 부담 갖지 마세요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        정부에는 <b>'주거취약계층 주거상향 지원사업'</b>이라는 아주 좋은 제도가 있어요. 고시원이나 여관 등에 거주하는 분들이 보증금 부담 없이 안전한 공공임대주택으로 이사할 수 있도록 이사비부터 생필품, 보증금까지 싹 다 지원해 주는 제도랍니다. 이 글을 읽으셨다면 망설이지 말고 꼭! 담당 멘토에게 연락해서 도움을 받아보세요.
        </div>
        </div>
        """
    
    return report

def generate_future(fam, house):
    report = f"<div class='card-box'>👨‍👩‍👧‍👦 <b>목표 가구 구성:</b> {fam}<br>🏡 <b>목표 주거 전형:</b> {house}</div>"
    
    if "전세임대" in house:
        report += """
        <div class='card-box'>
            <b>🔎 전세임대, 하나부터 열까지 상세히 알려줄게요!</b><br>
            전세임대는 내가 살고 싶은 동네의 집을 직접 찾아오면, LH가 집주인과 전세계약을 맺고 나에게 다시 저렴하게 재임대해 주는 아주 유연한 제도예요.<br><br>
            <ul class='step-list'>
                <li><b>신청 시기:</b> 자립준비청년 전형은 <b>'연중 상시'</b> 언제든 신청이 가능해요. 하지만 일반 청년이나 신혼부부 전형은 보통 <b>1월~2월 연초</b>에 모집 공고가 쏟아지니 이때를 놓치지 마세요.</li>
                <li><b>지원 한도:</b> 수도권 기준 약 1.2억 원~1.5억 원까지 지원해 주며, 여러분은 지원금의 5% 정도만 보증금으로 준비하면 돼요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 권리분석(안전한 집 찾기) 꿀팁</b><br>
            LH는 여러분을 지키기 위해 아주 깐깐한 심사를 해요. 집주인이 빚이 많으면 나중에 보증금을 떼일 수 있어서 심사에서 탈락시킵니다. 이걸 '권리분석'이라고 해요.<br>
            👉 <b>(집주인 빚 + 내 보증금)이 주택 가격의 90%를 넘으면 안 돼요!</b><br>
            부동산에 가서 집을 찾을 때 처음부터 당당하게 말씀하세요. <i>"사장님, 저 LH 전세임대로 구하고 있어요. 부채비율 90% 이하로 권리분석 무조건 통과할 수 있는 융자 없는 깨끗한 집만 보여주세요!"</i> 이렇게 말하면 시간 낭비를 확 줄일 수 있답니다.
            </div>
        </div>
        """
    elif "매입임대" in house:
        report += """
        <div class='card-box'>
            <b>🔎 매입임대, 하나부터 열까지 상세히 알려줄게요!</b><br>
            LH가 튼튼하게 잘 지어진 다세대 빌라나 오피스텔을 통째로 사들여서 우리에게 저렴하게 빌려주는 제도예요. 집주인이 LH라서 전세사기 걱정은 0%랍니다!<br><br>
            <ul class='step-list'>
                <li><b>신청 시기:</b> 보통 <b>3월, 6월, 9월, 12월 분기별</b>로 크게 정기 모집 공고가 올라와요.</li>
                <li><b>비용 안내:</b> 1순위 자격이 있다면 보증금 단돈 100만 원으로 입주가 가능하고, 냉장고나 세탁기 같은 기본 옵션이 갖춰진 곳도 많아서 초기 독립 자금을 아끼기 너무 좋아요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '관심지역 알림'과 '줍줍' 꿀팁</b><br>
            매입임대는 인기가 엄청나서 경쟁률이 높아요. 하지만 계약을 포기하는 사람들이 생겨서 남는 집이 꼭 나옵니다. 이걸 '수시모집(줍줍)'이라고 부르는데 보통 매주 금요일쯤 조용히 공고가 올라와요.<br>
            👉 <b>스마트폰에 'LH청약플러스' 앱을 깔고 마이페이지에서 [관심지역 알림]을 '인천광역시'로 꼭 켜두세요!</b> 남들보다 빠르게 빈집 정보를 낚아챌 수 있는 최고의 비법이랍니다.
            </div>
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 아파트(건설임대), 하나부터 열까지 상세히 알려줄게요!</b><br>
            영구임대, 국민임대, 행복주택처럼 LH가 직접 크게 지어서 분양하는 단지형 아파트예요. 경비실도 있고 놀이터도 있어서 매우 안전하고 쾌적하죠.<br><br>
            <ul class='step-list'>
                <li><b>가구원 수에 따른 면적 제한:</b> 아주 중요한 부분이에요! 혼자 사는 1인 가구는 전용면적 40㎡ 이하의 소형 평수만 지원할 수 있어요. 큰 평수에 지원하면 서류에서 바로 탈락하니 주의하세요. {fam}가 되면 46㎡~59㎡의 중형 평수로 넓혀갈 수 있답니다.</li>
                <li><b>거주 기간:</b> 국민임대의 경우 소득과 자산 기준만 계속 유지한다면 <b>최장 30년</b>까지도 이사 걱정 없이 살 수 있는 완벽한 베이스캠프예요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '배점표(가산점)' 만점 꿀팁</b><br>
            아파트는 1순위 안에서도 점수(배점)로 줄을 세워요. 여기서 이기는 두 가지 핵심 무기를 알려드릴게요.<br>
            1. <b>해당 지역 거주 기간:</b> 인천광역시에 주소지를 두고 오래 살수록 유리해요. (타 지역으로 전입신고를 맘대로 옮기면 점수가 깎일 수 있어요!)<br>
            2. <b>청약 통장 납입 횟수:</b> 돈의 액수보다 '얼마나 연체 없이 매월 꾸준히 냈는지'가 중요해요. 60회 이상 꾸준히 내면 여기서 최고점을 받을 수 있어요.
            </div>
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 통합공공임대, 하나부터 열까지 상세히 알려줄게요!</b><br>
            기존의 복잡했던 여러 임대주택 제도를 하나로 합친 2026년 최신 버전의 주거복지 끝판왕 제도예요.<br><br>
            <ul class='step-list'>
                <li><b>소득 연계형 임대료:</b> 예전에는 내 월급이 오르면 임대아파트에서 쫓겨날까 봐 걱정했죠? 통합공공임대는 내 월급이 오르면 임대료만 조금 더 내고 <b>최장 30년</b>까지 계속 살 수 있어요!</li>
                <li><b>우대 가점:</b> 맞벌이를 하거나, 다자녀 가정이 될수록 우선공급에서 훨씬 유리한 고지를 차지할 수 있어요.</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 전략적 준비 꿀팁</b><br>
            검단신도시나 계양신도시 같은 신규 택지지구에서 새 아파트 공고가 수시로 쏟아질 예정이에요. {fam}에 맞는 넓은 평형(최대 84㎡)을 지원할 수 있으니, 무주택 세대 요건을 잘 유지하면서 공고를 꾸준히 모니터링해 보아요.
            </div>
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 공공분양(뉴홈), 내 집 마련의 꿈을 이루는 법!</b><br>
            30년의 여정 끝에, 드디어 온전한 내 집을 갖는 단계예요. LH의 '뉴홈' 브랜드를 통해 주변 아파트 시세의 70% 수준으로 저렴하게 분양받을 수 있어요.<br><br>
            <ul class='step-list'>
                <li><b>특별공급(특공) 공략:</b> 일반 사람들과 경쟁하기엔 너무 치열해요. 우리는 {fam} 상황에 맞춰 <b>'생애최초 특공', '신혼부부 특공', '다자녀 특공'</b>이라는 마법의 문을 두드릴 거예요. 전체 물량의 70%가 특공에 배정된답니다!</li>
            </ul>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 분양 당첨과 신용관리(DSR) 꿀팁</b><br>
            1. <b>청약 통장 인정 금액:</b> 분양 당첨은 횟수가 아니라 통장에 <b>'인정된 총 금액'</b>이 많은 순서대로 뽑아요. 단, 한 달에 최대 10만 원까지만 인정해 줘요. 경제적 여유가 생기는 순간, 청약 자동이체를 월 10만 원으로 올려두는 것이 좋아요.<br>
            2. <b>신용점수 철통 방어:</b> 당첨이 끝이 아니에요! 집값의 80%를 빌려주는 정부의 아주 싼 대출(모기지)을 받으려면 신용점수가 좋아야 해요. <b>신용카드 현금서비스, 리볼빙, 잦은 카드론 사용</b>은 대출 심사(DSR)에서 치명적이니 20대부터 신용 관리에 꼭 신경 써주세요!
            </div>
        </div>
        """
    return report

# 4. 리포트 출력 및 PDF 버튼
if submit_btn:
    st.markdown(f'<div class="report-header">📑 {user_name} 님을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 섹션 1 (페이지 분할용 태그 삽입 안함 - 첫페이지)
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 튼튼하게 다지기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2 (여기서부터 PDF 새 페이지로 넘김)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_10, house_10), unsafe_allow_html=True)

    # 섹션 3
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_20, house_20), unsafe_allow_html=True)

    # 섹션 4
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 영구적인 주거 자립 달성</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_30, house_30), unsafe_allow_html=True)
    
    # 섹션 5 & 6 (마지막 안내장 느낌으로 묶어서 새 페이지)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5. 든든한 주거복지 정보망 (즐겨찾기 필수 사이트)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr/)</b><br>
        실제 집 공고를 보고 청약을 신청하는 공식 사이트예요. 앱을 꼭 다운로드하시고 '관심지역(인천) 알림'을 켜두는 것을 강력히 추천해요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr/)</b><br>
        전국 모든 종류의 주거복지 제도를 한눈에 보여주는 곳이에요. '자가진단' 메뉴를 누르면 내 나이와 소득에 딱 맞는 제도를 컴퓨터가 알아서 찾아준답니다.<br><br>
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
                단순히 공고를 기다리기보다는 미리 요건을 차근차근 준비하는 것이 좋은 결과를 얻는 가장 빠른 지름길입니다.<br><br>
                이 로드맵을 보다가 어려운 말이 있거나, 내 상황에 맞게 계획을 조금 수정하고 싶다면 <b>절대 혼자 고민하지 마세요.</b><br>
                당신의 든든한 내 편이 되어 언제든 함께 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 올림
            </div>
        </div>
    """, unsafe_allow_html=True)

    # PDF 추출 버튼
    st.markdown("---")
    components.html(
        """
        <div style="text-align: center; font-family: sans-serif; padding: 20px;">
            <button onclick="window.parent.print()" style="padding: 18px 40px; font-size: 18px; font-weight: bold; background-color: #2E86C1; color: white; border: none; border-radius: 10px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.15); transition: all 0.3s ease;">
                🖨️ 이 맞춤형 리포트를 PDF로 깔끔하게 저장하기
            </button>
            <p style="color: #7F8C8D; font-size: 14px; margin-top: 15px;">
                버튼을 누른 후 인쇄 화면이 뜨면, 대상(프린터)을 <b>[PDF로 저장]</b>으로 변경해 주세요.<br>
                각 연령대별 계획이 A4 용지 딱 1장씩 떨어지도록 완벽하게 세팅되어 있습니다!
            </p>
        </div>
        """,
        height=180
    )