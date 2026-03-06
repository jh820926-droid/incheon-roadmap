import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (인쇄 최적화 및 파이썬 매직 현상 방지 설정)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    /* 가독성 박스 디자인 */
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    .action-box { background-color: #F4F9FF; padding: 22px; border-radius: 10px; border-left: 6px solid #3498DB; margin: 15px 0;}
    .emergency-box { background-color: #FEF5F5; padding: 22px; border-radius: 10px; border-left: 6px solid #E74C3C; margin: 15px 0; color: #C0392B;}
    .tip-box { background-color: #FFF9E6; padding: 22px; border-radius: 10px; border-left: 6px solid #F1C40F; margin: 15px 0; color: #4D5656;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }

    /* 🖨️ PDF 인쇄 시 스크롤 제한 해제 및 레이아웃 강제 펼침 */
    @media print {
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"] {
            height: auto !important; overflow: visible !important; display: block !important; position: relative !important; background-color: white !important;
        }
        .page-break { page-break-before: always !important; display: block !important; height: 0px !important; border: none !important; }
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
st.subheader("📋 Step 1. 나의 30년 주거 자립 계획 설계")

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
    sub_10 = st.checkbox("10년 후에도 청약 유지를 약속할까요?", value=True, key="sub10")

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후 가구 구성", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 유지를 약속할까요?", value=True, key="sub20")

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립")
    fam_30 = st.selectbox("30년 후 가구 구성", fam_options, index=2)
    house_30 = st.selectbox("최종 주거 전형", house_options, index=4)
    sub_30 = st.checkbox("청약 통장으로 내 집 마련에 도전할까요?", value=True, key="sub30")

    submit_btn = st.form_submit_button("🚀 맞춤형 로드맵 리포트 생성", type="primary")

# 3. 실전 거주 가이드 함수 (압도적 디테일 복구)
def get_living_guide(house_type):
    if "전세임대" in house_type:
        return f"""
        <div class='action-box'>
            <b>🗓️ 계약 갱신 및 기간 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년 단위로 계약을 새로 해요. 총 14회까지 재계약이 가능해서 <b>최장 30년</b>까지 살 수 있답니다.</li>
                <li><b>재계약 절차:</b> 계약 끝나기 3개월 전 LH에서 집으로 우편이 와요. <b>주민등록등본, 가족관계증명서, 소득 증빙 서류</b>를 준비해서 LH 지사에 제출하면 끝!</li>
                <li><b>임대료(이자) 계산:</b> 지원금(1.2억 기준)에서 내 보증금을 뺀 나머지 금액에 대해 1~2% 이자를 내요. 자립준비청년은 여기서 50%를 할인받아 한 달에 약 5~8만 원 정도면 충분해요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 살면서 마주할 위기 대처법</b>
            <ul class='step-list'>
                <li><b>이자 연체 시:</b> 3개월 이상 밀리면 계약 해지 경고가 와요. 힘들면 피하지 말고 <b>LH 지역본부 전세임대팀</b>에 전화해서 '분할 납부'를 요청하세요.</li>
                <li><b>수리 문제:</b> 형광등, 건전지는 내가! <b>보일러, 벽면 누수, 싱크대 파손</b>은 집주인이 고쳐줘야 해요. 꼭 부동산 사장님께 먼저 말씀하세요.</li>
                <li><b>이사 가고 싶을 때(이주):</b> 계약 중간에 이사 가려면 최소 2개월 전 LH에 <b>'이주 신청서'</b>를 내야 보증금을 제때 돌려받아요.</li>
            </ul>
        </div>
        """
    elif "매입임대" in house_type:
        return f"""
        <div class='action-box'>
            <b>🗓️ 계약 갱신 및 기간 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년 단위로 재계약하며, 무주택 요건만 유지하면 <b>최장 20년</b>까지 거주할 수 있어요.</li>
                <li><b>임대료 수준:</b> 시세의 30~50%로 아주 저렴해요. 보증금 100~200만 원에 월세 10~20만 원 내외예요.</li>
                <li><b>재계약 주의점:</b> 취업 후 소득이 높아지면 임대료가 20~80%까지 할증될 수 있으니 미리 저축을 시작하세요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 살면서 마주할 위기 대처법</b>
            <ul class='step-list'>
                <li><b>월세 연체:</b> 3회 이상 밀리면 퇴거 대상이 될 수 있어요. <b>LH 주거복지 지사</b> 담당자에게 미리 연락하는 게 가장 중요해요.</li>
                <li><b>시설 고장:</b> 집안 시설이 고장 나면 <b>'유지보수 접수센터(1600-1004)'</b>로 전화하세요. LH에서 기사님을 보내 무료로 고쳐줍니다.</li>
                <li><b>해약 신청:</b> 나가고 싶을 땐 한 달 전에 <b>'해약 신청서'</b>를 관리실에 내야 보증금을 깔끔하게 돌려받아요.</li>
            </ul>
        </div>
        """
    else:
        return f"""
        <div class='action-box'>
            <b>🗓️ 아파트 계약 및 생활 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년 단위 갱신이며 <b>최장 30년</b> 거주가 가능해요.</li>
                <li><b>관리비 주의:</b> 월세 외에 '관리비'가 약 10~15만 원 정도 별도로 나와요. 자동이체를 꼭 설정해 두세요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 사고 예방 및 불이익</b>
            <ul class='step-list'>
                <li><b>불법 전대 절대 금지:</b> 친구에게 내 집을 빌려주고 돈을 받는 건 범죄예요. 적발 시 즉시 퇴거되고 향후 5년 동안 공공주택 입주가 금지됩니다.</li>
                <li><b>고장 상담:</b> 층간소음이나 고장 문제가 생기면 1차적으로 <b>아파트 관리사무소</b>를 방문하세요.</li>
            </ul>
        </div>
        """

# 4. 분석 알고리즘 (현재 진단)
def analyze_current_detail(assets, now_house, now_sub):
    report = ""
    # 청약 통장 디테일
    if "아니요" in now_sub:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 나의 미래를 바꾸는 입장권</h3>
            지금 통장이 없다는 건 국가가 주는 모든 주거 혜택을 포기하는 것과 같아요. 지금 당장 준비해야 합니다.<br>
            <div class='action-box'>
                <b>✅ 멘토의 행동 지침</b>
                <ul class='step-list'>
                    <li>신분증만 들고 은행에 가서 <b>'청년주택드림청약통장'</b>(최대 이율 4.5%)을 개설하세요.</li>
                    <li>매달 2만 원이라도 넣으세요. 나중에 아파트 들어갈 때 <b>'납입 횟수'</b>가 당락을 결정합니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 출발입니다!</h3>
            꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 여러분을 지켜주는 가장 큰 무기가 될 거예요.<br>
            <div class='tip-box'>
                <b>💡 급전이 필요할 때 꿀팁</b><br>
                통장을 해지하지 말고 <b>'청약 담보대출'</b>을 받으세요. 넣은 돈의 90%까지 아주 싼 이자로 빌릴 수 있어, 점수는 지키고 위기는 넘길 수 있습니다.
            </div>
        </div>
        """

    # 현재 주거 진단
    if "소년소녀가정" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 소년소녀가정 전세임대 진단</h3>
            만 20세까지 이자가 0원인 황금기입니다. 이 기간을 종잣돈 모으는 발판으로 삼아야 해요.<br>
            <div class='action-box'>
                <b>💰 돈 모으는 실전 지침</b>
                <ul class='step-list'>
                    <li>만 22세 이후부터는 지원금 1억 기준, 매달 약 8~16만 원의 이자가 발생합니다.</li>
                    <li><b>목표:</b> 주거비가 0원인 지금, 매월 20만 원씩 저축해서 5년 뒤 1,500만 원 이상의 독립 자금을 만드세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 자립준비청년 전형 거주 진단</h3>
            임대료 50% 할인 특례를 아주 잘 쓰고 계시네요! 보통 월세가 5~10만 원대로 저렴할 거예요.<br>
            <div class='tip-box'>
                <b>💡 월세를 '치킨 값'으로 만드는 비밀 (상호전환)</b><br>
                가용 자산 {assets}만 원이 있다면, LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원당 연 6~7% 이율로 월세를 깎아주는데, 어떤 예금보다 이득입니다.
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 일반 민간 월세 거주 진단</h3>
            매달 소멸되는 비싼 월세(40~60만 원)는 자립을 막는 가장 큰 적입니다.<br>
            <div class='action-box'>
                <b>🚀 긴급 주거 상향 전략</b>
                <ul class='step-list'>
                    <li>여러분은 자립준비청년 1순위 자격이 있습니다. 보증금 100만 원이면 LH 주택에 들어갈 수 있습니다.</li>
                    <li>지금 바로 LH청약플러스에서 '상시 모집' 공고를 확인하고 월세를 절반 이하로 줄이세요.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 주거취약계층 긴급 지원 진단</h3>
            지금 환경에서는 자립 계획 수립이 어렵습니다. 국가의 도움을 당당히 받으세요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 솔루션</b><br>
                <b>'주거상향 지원사업'</b>을 통해 보증금 0원, 이사비 지원까지 받으며 즉시 공공임대주택으로 이사할 수 있습니다. 지금 바로 담당자에게 연락주세요.
            </div>
        </div>
        """
    return report

# 5. 미래 로드맵 분석 알고리즘
def generate_future_detail(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9;'><b>📅 {age}세 시점:</b> {fam} / {house} 거주</div>"
    
    if not sub_status:
        report += f"<div class='emergency-box'><b>⚠️ 경고:</b> 청약 납입 중단 시 순위에서 탈락합니다. 월 2만 원은 끝까지 사수하세요!</div>"

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 전세임대 실전 공략 가이드 (A4 1장 분량)</h4>
            내가 원하는 동네의 집을 골라오면 LH가 대신 계약해주는 제도예요.<br>
            <div class='action-box'>
                <b>📌 실전 권리분석 90% 규칙</b>
                <b>👉 규칙: (집주인 빚 + 내 보증금) ÷ 집값 ≤ 90%</b><br>
                부동산 사장님께 처음부터 "부채비율 90% 이하인 안전한 집만 보여주세요"라고 당당하게 말하세요!
            </div>
            {get_living_guide("전세임대")}
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 매입임대 줍줍 전략 (A4 1장 분량)</h4>
            LH가 집주인이라 전세사기 걱정 0%! 에어컨, 세탁기 풀옵션이 많아 몸만 들어가면 돼요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 타이밍</b><br>
                스마트폰에 'LH청약플러스' 앱을 깔고 <b>[관심지역 알림 - 인천광역시]</b>를 꼭 켜두세요. 금요일 오후에 공고가 자주 올라옵니다.
            </div>
            {get_living_guide("매입임대")}
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 아파트(건설임대) 가점 관리 (A4 1장 분량)</h4>
            쾌적한 대단지 아파트예요. 최장 30년까지 거주가 보장된 꿈의 베이스캠프죠.<br>
            <div class='action-box'>
                <b>📌 1인 가구 40㎡ 제한 법칙</b>
                혼자 살 때는 12평 이하만 가능해요. 결혼 후 가족이 늘어나면 더 넓은 평수로 옮겨가는 전략을 짜야 해요.
            </div>
            {get_living_guide("건설임대")}
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 통합공공임대 평생 안심 거주 전략</h4>
            소득이 늘어도 쫓겨나지 않는 2026년 최신 제도예요. 소득에 맞춰 임대료만 조절하며 평생 살 수 있어요.<br>
            <div class='tip-box'>
                <b>💡 신도시 공략</b><br>
                검단, 계양 신도시 공고를 노리세요. 최대 34평까지 배정받을 수 있어 아이 키우기에 최고입니다.
            </div>
            {get_living_guide("통합공공")}
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 공공분양 '뉴홈' 자가 소유 전략</h4>
            내 집 마련의 종착지! 시세보다 30% 저렴하게 온전한 내 집을 갖는 방법이에요.<br>
            <div class='action-box'>
                <b>📌 신용 사수와 대출 준비</b>
                분양 당첨은 <b>'청약 총액'</b> 싸움이에요. 여유 생기면 즉시 월 10만 원으로 올리세요. <b>현금서비스, 리볼빙</b>은 절대 금물입니다!
            </div>
        </div>
        """
    return report

# 6. 최종 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**대상자:** {user_name} 님 | **발급일:** 2026년 3월 6일")

    st.markdown('<div class="section-title">1단계. 현재의 나 : 출발선 진단과 위기 관리</div>', unsafe_allow_html=True)
    st.markdown(analyze_current_detail(assets, now_house, now_sub), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2단계. 10년 후 ({current_age+10}세) 주거 계획과 실전 가이드</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3단계. 20년 후 ({current_age+20}세) 주거 안정과 상향 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4단계. 30년 후 ({current_age+30}세) 최종 자립 및 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5단계. 든든한 조력망 (필수 사이트 주소)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr)</b><br>
        실제 공고 확인 및 신청 창구! 앱을 깔고 '인천 관심지역 알림' 설정을 반드시 하세요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr)</b><br>
        전국 주거 복지 제도를 한눈에 검색하고, '자가진단' 기능을 통해 내 점수를 미리 계산해 보세요.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
        자립준비청년들만을 위한 전용 포털입니다. 주거 외에도 교육, 금융 정보가 가득합니다.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr)</b><br>
        이자 저렴한 대출 상품(버팀목, 디딤돌 등)을 한눈에 비교할 수 있습니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                이 로드맵을 보다가 어려운 말이 있거나 연체/수리 등 위기 상황이 생기면<br>
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
        </center>
        """,
        height=150
    )