import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (가독성 + PDF 인쇄 영역 완벽 통제)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.7rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 40px; margin-bottom: 15px;}
    .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #E5E8E8; margin-bottom: 20px; line-height: 1.8;}
    .highlight-text { color: #16A085; font-weight: bold;}
    .tip-box { background-color: #F9E79F; padding: 20px; border-radius: 8px; border-left: 6px solid #F1C40F; margin-top: 15px; margin-bottom: 15px; color: #4D5656; font-size: 0.95rem; line-height: 1.7;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }
    
    /* 🖨️ PDF 인쇄를 위한 마법의 CSS */
    @media print {
        /* 입력 폼 등 인쇄할 때 숨기고 싶은 영역 */
        .hide-on-print { display: none !important; }
        
        /* 각 단계별로 페이지를 무조건 새로 넘김 */
        .page-break { page-break-before: always !important; }
        
        /* 스트림릿 기본 요소(헤더, 사이드바 등) 숨기기 */
        header, footer, div[data-testid="stSidebar"], .stButton { display: none !important; }
        
        /* 배경색 유지 */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# [화면 노출 영역] 인쇄 시 숨겨지는 부분 시작
# ---------------------------------------------------------
st.markdown('<div class="hide-on-print">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 속도에 맞춰 그리는 30년 맞춤형 주거 플랜 백과사전</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass
st.divider()

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
    house_10 = st.selectbox("어떤 형태의 집에서 살고 싶나요?", house_options, index=1)
    sub_10 = st.checkbox("그때도 청약 통장을 계속 유지할 수 있을까요?", value=True)

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

st.markdown('</div>', unsafe_allow_html=True)
# ---------------------------------------------------------
# [화면 노출 영역] 인쇄 시 숨겨지는 부분 끝
# ---------------------------------------------------------

# 3. 디테일이 꽉 찬 분석 알고리즘 (현재)
def analyze_current(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
        🏦 <b>청약 통장, 왜 지금 바로 만들어야 할까요?</b><br>
        지금 청약 통장이 없거나 쉬고 계시군요! 청약 통장은 단순히 돈을 모으는 적금이 아니라, <b>'아파트에 들어갈 수 있는 입장권'</b>과 같아요. 나중에 LH 아파트(건설임대)에 들어가거나 내 집 마련(공공분양)을 할 때 이 입장권이 없으면 아예 지원조차 할 수 없답니다.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        여유가 당장 없더라도 괜찮아요. 은행에 가서 <b>'청년주택드림청약통장'</b>을 만들어 달라고 하세요. (일반 청약보다 이자가 훨씬 높아요!) 매월 2만 원씩이라도 자동이체를 걸어두면, 그 '횟수'가 나중에 엄청난 가산점(최대 6점)이 되어 돌아올 거예요. 
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
        혹시라도 목돈이 급하게 필요해져도 <b>절대 해지하지 말고, '청약예금 담보대출'을 알아보세요.</b> 통장을 깨지 않고도 내가 넣은 돈의 90%까지 싼 이자로 빌릴 수 있답니다. 우리의 입장권은 소중하니까 끝까지 지켜내 보아요!
        </div>
        </div>
        """

    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 소년소녀가정 전세임대 거주 중</b><br>
        만 20세까지 나라에서 전세지원금에 대한 이자를 전액 면제해 주는 최고의 혜택을 받고 계시네요. 주거비 걱정 없이 학업이나 일에 집중할 수 있는 아주 소중한 시기랍니다.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        만 22세 이후부터는 조금씩 임대료(이자)를 내야 할 수도 있어요. 주거비가 굳는 지금, 여유 돈을 차곡차곡 모아두면 큰 도움이 될 거예요. 이사할 일이 생기면 도배/장판 지원금 혜택(1회)도 꼭 챙겨서 신청해 보세요.
        </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 자립준비청년 전세/매입임대 거주 중</b><br>
        보호가 종료된 후 5년 동안 임대료를 50%나 할인받고 계시군요! 지금은 주거 안정이 든든하게 받쳐주고 있으니, 이제는 다가올 미래를 준비할 타이밍이에요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁 (상호전환제도)</b><br>
        5년 특례 기간이 끝나갈 무렵엔 임대료가 오를 수 있어요. 이때를 대비해 LH의 <b>'전환보증금 제도'</b>를 활용해 보세요. 현재 모아두신 {assets}만 원 같은 여유 자금을 보증금으로 추가 납부하면, 월세를 치킨 한 마리 값 수준으로 뚝 떨어뜨릴 수 있답니다!
        </div>
        </div>
        """
    elif "무상거주" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 무상거주 (시설/친인척/지인 등)</b><br>
        매달 나가는 고정적인 월세가 없는 지금이 바로 여러분의 인생에서 <b>'종잣돈을 모을 수 있는 골든타임'</b>이에요!<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        자립정착금이나 자립수당 등은 쉽게 꺼내 쓸 수 없도록 '청년도약계좌'나 적금에 단단히 묶어두는 것을 추천해요. 확실하게 독립할 준비가 되었을 때 자립준비청년 1순위 자격으로 LH 매입/전세임대로 안전하게 첫발을 내딛어 보아요.
        </div>
        </div>
        """
    elif "일반 민간 임대" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 일반 민간 임대 (월세/전세)</b><br>
        훌륭하게 독립을 하셨지만, 매달 나가는 높은 월세나 전세 대출 이자는 자산을 모으는 데 부담이 될 수 있어요. 전세사기 같은 위험도 무시할 수 없고요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        여러분에게는 일반인들보다 훨씬 유리하게 들어갈 수 있는 <b>'LH 자립준비청년 1순위 전형'</b>이라는 강력한 카드가 있어요! 비싼 월세로 돈이 새어나가지 않도록, 담당자와 함께 LH 주택으로 이사 갈 방법을 긍정적으로 검토해 보길 권장해요.
        </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
        🏠 <b>현재 주거 상황: 고시원 등 주거취약계층 거주 중</b><br>
        지금 지내는 곳이 답답하거나 마음이 쓰이시죠? 여러분의 안전과 따뜻한 잠자리가 가장 중요해요. "내 힘으로 다 해결해야 해"라고 혼자 부담 갖지 마세요.<br><br>
        <div class='tip-box'>
        <b>💡 담당자의 다정한 꿀팁</b><br>
        정부의 <b>'주거취약계층 주거상향 지원사업'</b>을 활용하면 이사비, 생필품, 보증금 지원을 받아 쾌적한 공공임대주택으로 이사할 수 있어요. 망설이지 말고 꼭 담당 멘토에게 연락해서 도움을 받아보세요.
        </div>
        </div>
        """
    return report

# 연령과 가족구성에 따라 내용이 진화하는 알고리즘
def generate_future(age, fam, house):
    report = f"<div class='card-box'>👨‍👩‍👧‍👦 <b>목표 가구 구성:</b> {fam}<br>🏡 <b>목표 주거 전형:</b> {house}</div>"
    
    # 1. 전세임대 연령별 진화
    if "전세임대" in house:
        if age < 40:
            title = "🔎 청년/신혼부부 전세임대, 이렇게 준비해 봐요!"
            desc = "내가 살고 싶은 동네의 집을 찾아오면, LH가 집주인과 전세계약을 맺고 저렴하게 재임대해 주는 제도예요. 보통 연초(1~2월)에 청년이나 신혼부부 모집 공고가 쏟아진답니다."
        else:
            title = "🔎 일반/다자녀 전세임대, 이렇게 준비해 봐요!"
            desc = f"{age}세가 되신 시점이라면, 청년 특례보다는 소득 기준에 맞춘 일반 전세임대나 가족 수에 맞춘 다자녀 전세임대를 활용해 볼 수 있어요. 안정적인 주거지를 구하는 데 큰 도움이 될 거예요."
            
        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 권리분석(안전한 집 찾기) 꿀팁</b><br>
            집주인이 빚이 많으면 나중에 보증금을 떼일 수 있어서 심사(권리분석)에서 탈락해요. <b>(집주인 빚 + 내 보증금)이 주택 가격의 90%를 넘으면 안 된답니다!</b> 부동산에 갈 때 "LH 전세가 가능한, 부채비율 90% 이하인 안전한 집만 보여주세요"라고 꼭 요청해 보세요.
            </div>
        </div>
        """
        
    # 2. 매입임대 연령별 진화
    elif "매입임대" in house:
        if age < 40:
            title = "🔎 청년/신혼부부 매입임대, 이렇게 준비해 봐요!"
            desc = "LH가 튼튼하게 지어진 빌라나 오피스텔을 통째로 사서 빌려주기 때문에 전세사기 걱정이 0%예요. 보통 3, 6, 9, 12월에 크게 모집을 한답니다."
        else:
            title = "🔎 일반/고령자 매입임대, 이렇게 준비해 봐요!"
            desc = f"연령대가 높아질수록 주거의 편리함이 중요해져요. {age}세 시점에는 일반 매입임대나 엘리베이터가 잘 갖춰진 1층 우대 전형 등 상황에 맞는 안전한 주택을 노려볼 수 있어요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '관심지역 알림' 꿀팁</b><br>
            계약을 포기하는 사람들이 생겨서 남는 집이 꼭 나와요. 스마트폰에 'LH청약플러스' 앱을 깔고 마이페이지에서 <b>[관심지역 알림]을 인천광역시로 꼭 켜두세요!</b> 알림이 울리면 바로 지원해서 빈집을 낚아챌 수 있답니다. 인천에 오래 살았을수록 점수가 높아져 당첨 확률이 올라가요.
            </div>
        </div>
        """
        
    # 3. 건설임대 연령별 진화
    elif "건설임대" in house:
        if age < 40:
            title = "🔎 행복주택/국민임대, 이렇게 준비해 봐요!"
            desc = "새로 지어지는 깨끗한 단지형 아파트에 입주할 수 있어요. 1인 가구는 소형 평수에, 가족이 늘어나면 조금 더 넓은 평수로 옮겨갈 수 있답니다."
        else:
            title = "🔎 국민임대/영구임대, 안정적인 장기 거주를 준비해 봐요!"
            desc = f"{age}세 이후에는 이사를 자주 다니기보다 정착하는 것이 중요하죠. 소득 요건만 유지한다면 국민임대 아파트에서 최장 30년까지 마음 편히 거주할 수 있는 아주 든든한 전형이에요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 '배점표' 만점 꿀팁</b><br>
            아파트 입주는 인기가 많아서 점수 관리가 필수예요. <b>1. 인천에 얼마나 오래 살았는지</b> (전입신고 유지!), <b>2. 청약 통장에 연체 없이 꾸준히 돈을 넣은 횟수</b>가 당첨을 결정짓는 가장 강력한 무기가 된답니다. 
            </div>
        </div>
        """
        
    # 4. 통합공공 연령별 진화
    elif "통합공공" in house:
        if age < 40:
            title = "🔎 통합공공임대, 첫 진입을 노려봐요!"
            desc = "복잡한 제도를 하나로 합친 진화된 임대아파트예요. 신혼부부나 신생아 특별공급을 활용하면 아주 유리하게 첫 입주를 할 수 있어요."
        else:
            title = "🔎 통합공공임대, 30년 안심 거주를 준비해요!"
            desc = "내 월급이나 소득이 조금 오르더라도 쫓겨나지 않고, 소득에 맞춰 임대료만 조금 더 내며 30년 동안 이사 안 가고 살 수 있는 정말 좋은 제도예요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 전략적 준비 꿀팁</b><br>
            맞벌이를 하거나 다자녀 가정이 될수록 가산점을 듬뿍 받을 수 있어요. 검단, 계양 같은 신규 택지지구에서 새 아파트 공고가 쏟아질 테니 공고문을 꾸준히 모니터링해 보는 것을 권장해요.
            </div>
        </div>
        """
        
    # 5. 분양 연령별 진화
    elif "분양" in house:
        if age < 40:
            title = "🔎 공공분양(뉴홈), 첫 내 집 마련을 준비해요!"
            desc = "특별공급(생애최초, 신혼부부 등) 물량이 70%나 돼요. 주변 시세보다 훨씬 저렴하게 새 아파트를 가질 수 있는 절호의 기회랍니다."
        else:
            title = "🔎 공공분양(일반/다자녀), 완전한 내 집을 가져봐요!"
            desc = f"{age}세까지 차곡차곡 모아둔 청약 통장의 힘을 발휘할 때예요! 그동안 쌓인 납입 인정 금액으로 일반공급에 도전하거나, 다자녀 특별공급을 통해 넉넉한 내 집을 마련해 볼 수 있어요."

        report += f"""
        <div class='card-box'>
            <b>{title}</b><br>{desc}<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 분양 당첨과 신용관리(DSR) 꿀팁</b><br>
            1. <b>청약 통장 인정 금액:</b> 분양은 횟수가 아니라 통장에 <b>'매월 최대 10만 원씩 인정받은 총 금액'</b>이 많은 순서대로 뽑아요. 경제적 여유가 생기면 꼭 월 10만 원으로 자동이체를 맞춰두세요.<br>
            2. <b>신용점수 철통 방어:</b> 당첨 후 집값의 최대 80%를 빌려주는 싼 대출(모기지)을 받으려면 신용점수가 좋아야 해요. 잦은 현금서비스나 리볼빙은 절대 피하고 신용 관리를 꼼꼼히 해주세요.
            </div>
        </div>
        """
    return report

# 4. 리포트 출력 및 PDF 버튼
if submit_btn:
    # 여기서부터는 인쇄 시 첫 페이지가 됨
    st.markdown(f'<div class="report-header">📑 {user_name} 님을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 섹션 1
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 튼튼하게 다지기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2 (여기서부터 PDF 새 페이지)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10), unsafe_allow_html=True)

    # 섹션 3 (여기서부터 PDF 새 페이지)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20), unsafe_allow_html=True)

    # 섹션 4 (여기서부터 PDF 새 페이지)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 영구적인 주거 자립 달성</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30), unsafe_allow_html=True)
    
    # 섹션 5 & 6 (안내장은 마지막 페이지)
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
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # PDF 추출 버튼 (이 버튼도 인쇄 시 안 보이게 CSS에서 숨김 처리 완료)
    st.markdown("---")
    components.html(
        """
        <div style="text-align: center; font-family: sans-serif; padding: 20px;">
            <button onclick="window.parent.print()" style="padding: 18px 40px; font-size: 18px; font-weight: bold; background-color: #2E86C1; color: white; border: none; border-radius: 10px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.15); transition: all 0.3s ease;">
                🖨️ 이 맞춤형 리포트를 PDF로 깔끔하게 저장하기
            </button>
            <p style="color: #7F8C8D; font-size: 14px; margin-top: 15px;">
                버튼을 누른 후 인쇄 화면이 뜨면, 대상(프린터)을 <b>[PDF로 저장]</b>으로 변경해 주세요.<br>
                (입력창은 사라지고 오직 리포트만 각 연령대별로 1장씩 예쁘게 분할되어 저장됩니다!)
            </p>
        </div>
        """,
        height=180
    )