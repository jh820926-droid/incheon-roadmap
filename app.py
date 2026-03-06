import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (가독성 극대화 및 깔끔한 여백)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.7rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 50px; margin-bottom: 30px;}
    .section-title { font-size: 1.4rem; color: #2C3E50; font-weight: 800; margin-top: 40px; margin-bottom: 15px;}
    .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #E5E8E8; margin-bottom: 20px; line-height: 1.7;}
    .highlight-text { color: #16A085; font-weight: bold;}
    .tip-box { background-color: #F9E79F; padding: 15px; border-radius: 8px; border-left: 5px solid #F1C40F; margin-top: 10px; color: #4D5656; font-size: 0.95rem;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 속도에 맞춰 그리는 30년 맞춤형 주거 플랜</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass

st.divider()

# 2. 30년 생애주기 입력 폼
st.subheader("📋 Step 1. 나의 30년 주거 계획 세우기")

fam_options = ["1인 가구 (혼자 살아요)", "2인 가구 (부부/형제와 살아요)", "3인 가구 (아이 1명과 살아요)", "4인 이상 (다자녀 가정이에요)"]
house_options = [
    "전세임대 (내가 원하는 동네의 집을 찾을래요)", 
    "매입임대 (LH가 마련한 빌라/오피스텔이 좋아요)", 
    "건설임대 (안전한 국민/행복 아파트에 살래요)", 
    "통합공공임대 (이사가기 싫어요, 30년 살래요)", 
    "공공분양 (내 집을 완전히 소유하고 싶어요)"
]
current_house_options = [
    "LH 전세임대 (소년소녀가정 등 혜택 중)",
    "LH 전세/매입임대 (자립준비청년 혜택 중)",
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

# 3. 분석 알고리즘 (친절한 구어체 & 가독성 개선)
def analyze_current(assets, now_house, now_sub):
    report = ""
    # 청약 안내
    if "아니요" in now_sub:
        report += "<div class='card-box'>🏦 <b>청약 통장은 자립의 무기예요!</b><br>지금 청약 통장이 없거나 쉬고 계시군요. 나중에 LH 아파트나 내 집 마련을 할 때 청약 통장이 없으면 너무 아쉬울 수 있어요. 한 달에 2만 원씩이라도 은행에 가서 만들어두는 것을 꼭 추천해요!</div>"
    else:
        report += "<div class='card-box'>🏦 <b>청약 통장 관리를 정말 잘하고 있어요!</b><br>지금처럼 연체 없이 꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 엄청난 가산점이 될 거예요. 힘들더라도 절대 깨지 말고 유지해 보아요!</div>"

    # 주거 형태별 안내
    if "소년소녀가정" in now_house:
        report += "<div class='card-box'>🏠 <b>현재 주거: 소년소녀가정 전세임대</b><br>만 20세까지는 이자가 완전히 면제되어서 주거비 부담이 없는 정말 좋은 시기랍니다.<br><br><span class='highlight-text'>💡 담당자의 꿀팁:</span> 만 22세 이후부터는 조금씩 임대료(이자)를 내야 할 수도 있어요. 주거비가 굳는 지금! 여유 돈을 차곡차곡 모아두면 큰 도움이 될 거예요.</div>"
    elif "자립준비청년" in now_house:
        report += f"<div class='card-box'>🏠 <b>현재 주거: 자립준비청년 혜택 적용 중</b><br>보호가 끝난 후 5년 동안은 임대료를 50%나 할인받을 수 있어서 정말 든든해요.<br><br><span class='highlight-text'>💡 담당자의 꿀팁:</span> 5년 혜택이 끝나갈 무렵엔 임대료가 조금 오를 수 있어요. 지금 모아둔 {assets}만 원을 보증금으로 전환해서 나중에 월세를 줄이는 데 활용해 보면 어떨까요?</div>"
    elif "무상거주" in now_house:
        report += "<div class='card-box'>🏠 <b>현재 주거: 시설이나 지인과 함께 생활 중</b><br>주거비(월세)가 따로 나가지 않는 지금이 바로 '종잣돈'을 모을 수 있는 최고의 골든타임이에요!<br><br><span class='highlight-text'>💡 담당자의 꿀팁:</span> 청년도약계좌 같은 좋은 적금에 돈을 묶어두고, 나중에 독립할 때 자립준비청년 1순위 자격으로 안전한 LH 주택으로 이사 가는 걸 목표로 해봐요.</div>"
    elif "일반 민간 임대" in now_house:
        report += "<div class='card-box'>🏠 <b>현재 주거: 개별적으로 구한 월세/전세</b><br>매달 나가는 월세가 장기적으로는 자산을 모으는 데 큰 부담이 될 수 있어요.<br><br><span class='highlight-text'>💡 담당자의 꿀팁:</span> 여러분은 보증금 부담이 적고 훨씬 안전한 LH 임대주택에 1순위로 들어갈 수 있는 자격이 있어요! 담당자와 함께 LH 주택으로 이사 갈 방법을 꼭 상의해 보길 바라요.</div>"
    elif "주거취약계층" in now_house:
        report += "<div class='card-box'>🏠 <b>현재 주거: 고시원 등 도움이 필요한 곳</b><br>지금 지내는 곳이 불편하거나 마음이 쓰인다면 절대 혼자서 고민하지 마세요.<br><br><span class='highlight-text'>💡 담당자의 꿀팁:</span> '주거상향 지원사업'처럼 여러분을 더 안전하고 따뜻한 집으로 안내해 줄 수 있는 정부 지원이 많이 준비되어 있어요. 언제든 담당자에게 꼭 알려주세요!</div>"
    
    return report

def generate_future(fam, house):
    report = f"<div class='card-box'>👨‍👩‍👧‍👦 <b>목표 가족:</b> {fam}<br>🏡 <b>목표 주거:</b> {house}</div>"
    
    if "전세임대" in house:
        report += """
        <div class='card-box'>
            <b>🔎 전세임대, 이렇게 준비해 봐요!</b><br>
            내가 원하는 동네, 맘에 드는 집을 고르면 LH가 보증금을 대신 내주는 제도예요. 일반이나 신혼 유형은 보통 연초(1~2월)에 모집 공고가 많이 나온답니다.<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 합격 팁</b><br>
            집주인에게 빚이 많은 집(부채비율 90% 초과)은 LH에서 위험하다고 판단해서 계약을 안 해줘요. 부동산에 갈 때 처음부터 "LH 전세가 가능한 빚 없는 안전한 집만 보여주세요"라고 당당하게 요청하세요!
            </div>
        </div>
        """
    elif "매입임대" in house:
        report += """
        <div class='card-box'>
            <b>🔎 매입임대, 이렇게 준비해 봐요!</b><br>
            LH가 직접 튼튼한 다세대 주택이나 오피스텔을 사서 싸게 빌려주기 때문에 전세사기 걱정이 0%랍니다. 보통 3, 6, 9, 12월에 크게 모집을 해요.<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 합격 팁</b><br>
            LH청약플러스 앱을 깔고 '관심지역 알림'을 켜두세요. 빈집이 생기면 수시로 공고가 뜨거든요! 또 당첨 후에 보증금을 조금 더 내면 매달 내는 월세를 치킨 한 마리 값 수준으로 뚝 떨어뜨릴 수 있답니다.
            </div>
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 건설임대(아파트), 이렇게 준비해 봐요!</b><br>
            단지 내 쾌적한 환경을 누리며 안전하게 살 수 있어요. {fam}에 맞는 예쁜 평형의 아파트를 배정받게 될 거예요.<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 합격 팁</b><br>
            아파트 입주는 인기가 많아서 점수 관리가 필수예요. <b>청약 통장에 연체 없이 꾸준히 돈을 넣은 횟수</b>와 <b>인천에 얼마나 오래 살았는지</b>가 당첨을 결정짓는 가장 큰 무기가 된답니다.
            </div>
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 통합공공임대, 이렇게 준비해 봐요!</b><br>
            나중에 취업을 해서 월급이 오르더라도 방 빼라고 쫓겨나지 않아요! 내 소득에 맞춰서 임대료를 내며 최장 30년까지 편하게 살 수 있는 아주 든든한 아파트예요.<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 합격 팁</b><br>
            맞벌이를 하거나 다자녀 가정이 될수록 가산점을 받기 유리한 전형이에요. 신규 택지구구(검단, 계양 등)에서 모집 공고가 자주 뜰 테니 눈여겨봐요!
            </div>
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <b>🔎 공공분양, 내 집 마련 이렇게 준비해 봐요!</b><br>
            LH의 '뉴홈' 같은 제도를 통해 특별공급(생애최초, 신혼부부 등)을 활용하면 주변 시세보다 훨씬 저렴하게 진짜 내 집을 가질 수 있어요.<br><br>
            <div class='tip-box'>
            <b>💡 담당자가 알려주는 합격 팁</b><br>
            분양 당첨은 청약 통장에 <b>'매월 10만 원씩 꾸준히 인정받은 금액'</b>이 많을수록 유리해요! 또 당첨 후에 이자가 싼 나라의 대출을 잘 받으려면, 휴대폰 요금을 밀리지 않는 등 건강한 신용점수를 유지하는 게 정말 중요해요.
            </div>
        </div>
        """
    return report

# 4. 리포트 출력 및 PDF 버튼
if submit_btn:
    st.markdown(f'<div class="report-header">📑 {user_name} 님을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 섹션 1
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 확인하기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_10, house_10), unsafe_allow_html=True)

    # 섹션 3
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_20, house_20), unsafe_allow_html=True)

    # 섹션 4
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 안정적인 주거 자립</div>', unsafe_allow_html=True)
    st.markdown(generate_future(fam_30, house_30), unsafe_allow_html=True)
    
    # 섹션 5. 도움받는 곳
    st.markdown('<div class="section-title">5. 든든한 주거복지 정보망 (도움받는 곳)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr/)</b><br>
        실제 집 공고를 보고 신청하는 곳이에요. 앱을 깔고 '관심지역 알림'을 켜두면 좋아요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr/)</b><br>
        나에게 맞는 혜택이 뭔지 모를 때, '자가진단' 메뉴를 통해 미리 테스트해 볼 수 있어요.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr/)</b><br>
        자립준비청년들을 위해 주거, 금융, 취업 정보를 모두 모아둔 전용 포털이에요.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr/)</b><br>
        나중에 집을 구할 때, 이자가 아주 저렴한 나라의 대출(버팀목, 디딤돌 등)을 알아볼 수 있어요.
        </div>
    """, unsafe_allow_html=True)

    # 6. 담당자 핫라인
    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.1rem; margin-bottom: 0px;">
                로드맵을 보다가 어려운 말이 있거나, 계획을 바꾸고 싶다면 절대 혼자 고민하지 마세요.<br>
                당신의 든든한 내 편이 되어 언제든 함께 길을 찾아 줄게요.
            </p>
            <div style="font-size: 1.2rem; font-weight: bold; color: #2C3E50; margin-top: 20px;">
                👤 담당자 김정현<br>
                ☎️ 직통 번호: 070-7663-1153
            </div>
        </div>
    """, unsafe_allow_html=True)

    # PDF 추출 버튼 (HTML/JavaScript 삽입)
    st.markdown("---")
    components.html(
        """
        <div style="text-align: center; font-family: sans-serif;">
            <button onclick="window.parent.print()" style="padding: 15px 30px; font-size: 18px; font-weight: bold; background-color: #2E86C1; color: white; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                📄 이 리포트를 PDF로 저장하기
            </button>
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">버튼을 누른 후 '대상' 또는 '프린터'를 <b>[PDF로 저장]</b>으로 변경해 주세요.</p>
        </div>
        """,
        height=150
    )