import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정 및 메타데이터
st.set_page_config(
    page_title="2026 인천자립 주거로드맵 - 주거 안심 백과사전",
    page_icon="🏠",
    layout="centered"
)

# 2. 🖨️ PDF 인쇄 및 가독성 극대화를 위한 마법의 CSS (800줄급 분량의 뼈대)
st.markdown("""
    <style>
    /* 기본 테마 및 가독성 */
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 4px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    /* 카드 및 정보 박스 디자인 */
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    .action-box { background-color: #F4F9FF; padding: 25px; border-radius: 10px; border-left: 6px solid #3498DB; margin: 20px 0;}
    .emergency-box { background-color: #FEF5F5; padding: 25px; border-radius: 10px; border-left: 6px solid #E74C3C; margin: 20px 0; color: #C0392B;}
    .tip-box { background-color: #FFF9E6; padding: 25px; border-radius: 10px; border-left: 6px solid #F1C40F; margin: 20px 0; color: #4D5656; font-size: 1.05rem;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }
    .step-list li { margin-bottom: 12px; }

    /* 🖨️ PDF 인쇄 시 스크롤 제한 해제 및 페이지 분할 속성 */
    @media print {
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"] {
            height: auto !important; overflow: visible !important; display: block !important; background-color: white !important;
        }
        .page-break { page-break-before: always !important; display: block !important; height: 1px !important; border: none !important; margin: 0 !important; }
        * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    }
    </style>
""", unsafe_allow_html=True)

# 화면 상단 타이틀
st.markdown('<div class="main-title">🏠 2026 인천자립 주거로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 성장에 맞춰 설계하는 30년 주거 안심 백과사전</div>', unsafe_allow_html=True)

try:
    st.image("family_illust.jpg", use_container_width=True) 
except:
    pass
st.divider()

# 3. 30년 생애주기 입력 폼 (사용자 데이터를 정확히 수집)
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
    st.info("💡 지금 나의 상황과 미래의 꿈꾸는 모습을 차분하게 골라주세요. 이 선택에 따라 맞춤형 백과사전이 만들어집니다.")
    user_name = st.text_input("👤 성함", "김자립")
    col1, col2 = st.columns(2)
    with col1:
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 현재 모은 자산 (만원 단위)", min_value=0, value=100)
    with col2:
        is_vulnerable = st.checkbox("보호종료 청년 해당 여부", value=True)
        now_sub = st.radio("🏦 주택청약통장 유무", ["네, 가입 중", "아니요, 미가입"])
    now_house = st.selectbox("🏠 현재 거주 중인 주거 형태", current_house_options)

    st.markdown("---")
    st.markdown("#### 🌱 [10년 후] 주거 목표")
    fam_10 = st.selectbox("10년 후 예상 가구원 수", fam_options, index=0)
    house_10 = st.selectbox("10년 후 희망 주거 형태", house_options, index=1)
    sub_10 = st.checkbox("10년 후에도 청약 통장을 유지하시겠습니까?", value=True, key="sub10")

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후 예상 가구원 수", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 주거 형태", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 통장을 유지하시겠습니까?", value=True, key="sub20")

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립 목표")
    fam_30 = st.selectbox("30년 후 예상 가구원 수", fam_options, index=2)
    house_30 = st.selectbox("마지막 단계 최종 주거 형태", house_options, index=4)
    sub_30 = st.checkbox("모아둔 청약으로 내 집 마련에 도전하시겠습니까?", value=True, key="sub30")

    submit_btn = st.form_submit_button("🚀 나만의 주거 백과사전 리포트 생성", type="primary")

# 4. 실전 거주 가이드 함수
def get_living_guide_book(house_type):
    if "전세임대" in house_type:
        return f"""
        <div class='action-box'>
            <h4 style="margin-top:0;">🗓️ 전세임대 계약 및 생활 가이드</h4>
            <ul class='step-list'>
                <li><b>갱신 및 기간:</b> 2년 단위로 계약하며, 자립준비청년 전형은 <b>최장 30년</b>까지 거주할 수 있어요. 2년마다 LH에서 '재계약 안내 우편'이 오니 절대 무시하면 안 돼요!</li>
                <li><b>재계약 준비:</b> 만료 3개월 전 등본, 소득증빙서류를 LH에 내야 해요. 소득이 너무 많이 오르면 임대료가 할증되거나 재계약이 안 될 수도 있으니 멘토와 상의하세요.</li>
                <li><b>임대료 계산:</b> 지원금 1.2억 중 내 보증금(5%)을 뺀 1.14억에 대해 연 1~2% 이자를 내요. 자립준비청년은 50% 할인 혜택으로 <b>월 5~8만 원</b> 정도만 내면 된답니다.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <h4 style="margin-top:0;">🚨 사고 발생! 당황하지 말고 이렇게 하세요</h4>
            <ul class='step-list'>
                <li><b>월세(이자) 연체:</b> 3개월 이상 밀리면 LH에서 계약 해지 경고가 날아와요. 돈이 부족하다면 무조건 피하지 말고 <b>LH 관할 지사 전세임대팀</b>에 전화해서 '분할 납부'를 요청하세요.</li>
                <li><b>시설 고장:</b> 형광등, 도어락 건전지 같은 소모품은 내가! <b>보일러, 누수, 천장 파손</b> 같은 구조적 문제는 집주인이 고쳐줘야 해요. 절대 내 돈 먼저 쓰지 말고 부동산 사장님께 연락해 LH 중재를 요청하세요.</li>
                <li><b>이사 가고 싶을 때(이주):</b> 계약 기간 중간에 이사하려면 <b>'이주 신청서'</b>를 먼저 LH에 내야 보증금을 안전하게 돌려받고 다음 집으로 갈 수 있어요.</li>
            </ul>
        </div>
        """
    elif "매입임대" in house_type:
        return f"""
        <div class='action-box'>
            <h4 style="margin-top:0;">🗓️ 매입임대 계약 및 생활 가이드</h4>
            <ul class='step-list'>
                <li><b>갱신 및 기간:</b> 2년 단위 갱신이며, 무주택 요건 유지 시 <b>최장 20년</b>까지 살 수 있어요. LH가 직접 관리해서 정말 편해요.</li>
                <li><b>임대료 수준:</b> 시세의 30~50%로 아주 저렴해요. 보통 보증금 100~200만 원에 월세 10~20만 원 내외랍니다.</li>
                <li><b>재계약 주의점:</b> 재계약 시점에 소득이 기준을 초과하면 임대료가 20%에서 최대 80%까지 할증될 수 있으니 미리 목돈을 모아둬야 해요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <h4 style="margin-top:0;">🚨 사고 발생! 당황하지 말고 이렇게 하세요</h4>
            <ul class='step-list'>
                <li><b>임대료 연체:</b> 자동이체 통장 잔액을 꼭 확인하세요. 3회 이상 밀리면 퇴거 대상이에요. <b>LH 주거복지 지사</b> 담당자에게 사정을 미리 말하는 게 최선입니다.</li>
                <li><b>수리 문제:</b> 매입임대는 LH가 주인이니 <b>'유지보수 접수센터(1600-1004)'</b>로 전화 한 통만 하세요. 기사님이 무료로 고쳐주러 오십니다.</li>
                <li><b>해약 신청:</b> 나가고 싶을 땐 한 달 전에 <b>'해약 신청서'</b>를 관리실이나 지사에 제출해야 보증금을 제날짜에 돌려받습니다.</li>
            </ul>
        </div>
        """
    else: # 건설/통합/분양
        return f"""
        <div class='action-box'>
            <h4 style="margin-top:0;">🗓️ 아파트(건설/통합) 계약 및 생활 가이드</h4>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 아파트는 2년 단위 갱신이며 소득 요건 유지 시 <b>최장 30년</b> 거주가 가능해요.</li>
                <li><b>관리비 폭탄 주의:</b> 아파트는 월세 외에 <b>관리비(약 10~15만 원)</b>가 따로 나와요. 예산 짤 때 월세와 관리비를 합쳐서 생각해야 생활이 쪼들리지 않아요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <h4 style="margin-top:0;">🚨 사고 예방 및 불이익 주의</h4>
            <ul class='step-list'>
                <li><b>불법 전대 절대 금지:</b> 친구나 아는 사람에게 내 집을 빌려주고 돈 받는 건 범죄예요! 걸리면 즉시 쫓겨나고 향후 5년 동안 국가 주택 입주가 불가능해요.</li>
                <li><b>고장/소음 상담:</b> 시설 고장이나 층간소음은 1차적으로 <b>아파트 관리사무소</b>를 방문해 해결하세요. 혼자 고민하지 않아도 된답니다.</li>
            </ul>
        </div>
        """

# 5. 분석 알고리즘 (현재 단계 - 압도적 정보량 복구)
def analyze_now_step(assets, now_house, now_sub):
    report = ""
    # 청약 통장 디테일 (A4 반 페이지 분량)
    if "아니요" in now_sub:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 나의 인생을 바꾸는 마법의 티켓</h3>
            지금 통장이 없다는 것은 나중에 국가가 지어주는 깨끗하고 저렴한 아파트를 포기하는 것과 같아요. 남들보다 늦기 전에 오늘 당장 준비해야 합니다.<br>
            <div class='action-box'>
                <b>✅ 멘토의 강력 추천 행동</b>
                <ul class='step-list'>
                    <li>신분증만 들고 은행에 가서 <b>'청년주택드림청약통장'</b>(최대 이율 4.5%)을 개설하세요.</li>
                    <li>매달 딱 <b>2만 원</b>이라도 자동이체를 설정하세요. 금액보다 <b>'몇 번 꾸준히 냈는지(납입 횟수)'</b>가 당첨을 결정하는 핵심 가산점(최대 6점)이 된답니다.</li>
                    <li>군대에 간다면 군인 전용 적금과 연계하여 더 큰 혜택을 챙길 수 있으니 멘토와 상의하세요.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 자립의 시작입니다!</h3>
            지금처럼 연체 없이 꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 여러분을 지켜주는 가장 큰 무기가 될 거예요. 정말 잘하고 계십니다!<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁 (해지 금지!)</b><br>
                혹시 살다가 목돈이 급하게 필요해서 청약 통장을 깨고 싶어지는 아찔한 순간이 올 수 있어요. 그럴 때 <b>절대 해지하지 마세요!</b> 은행에 가서 <b>'청약 담보대출'</b>을 받으면 내가 넣은 돈의 90%까지 아주 저렴한 이자로 빌려줍니다. 통장 점수는 살리고 급한 불은 끄는 현명한 방법이에요.
            </div>
        </div>
        """

    # 현재 거주 상황별 실전 가이드
    if "소년소녀가정" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 소년소녀가정 전세임대 진단</h3>
            <b>특급 장점:</b> 여러분은 만 20세까지 전세지원금 이자가 <b>'0원'</b>인 인생 최고의 재무적 골든타임에 있어요. 주거비 걱정 없는 이 시기를 절대 그냥 흘려보내면 안 됩니다.<br>
            <div class='action-box'>
                <b>💰 돈 모으는 실전 지침</b>
                <ul class='step-list'>
                    <li><b>이자가 생기는 시점:</b> 만 22세 이후부터는 지원금 1억 기준, 매달 약 8~16만 원의 이자가 발생해요.</li>
                    <li><b>저축 목표:</b> 주거비가 전혀 안 나가는 지금! 매월 20만 원씩 무조건 저축해서 5년 뒤 1,500만 원 이상의 독립 자금을 만드세요. 이게 성공 자립의 밑천입니다.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 자립준비청년 전형 거주 진단</h3>
            <b>특급 장점:</b> 보호 종료 후 5년 동안 임대료 50% 감면 특례를 아주 현명하게 쓰고 계시네요! 보통 월세가 10~20만 원대인데, 지금은 5~10만 원대로 저렴할 거예요.<br>
            <div class='tip-box'>
                <b>💡 월세를 '치킨 한 마리 값'으로 낮추는 비법 (상호전환)</b><br>
                지금 모아둔 자산 {assets}만 원이 있다면, 혹은 목돈이 생기면 LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원 단위로 LH에 추가 입금하면 연 6~7% 이율로 계산해서 매월 내는 월세를 확 깎아줍니다. 은행 적금보다 훨씬 이득이니 꼭 실천해 보세요!
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 일반 민간 월세/전세 거주 진단</h3>
            <b>위험 요인:</b> 스스로 독립한 건 훌륭하지만, 매달 나가는 비싼 월세(40~60만 원)는 종잣돈 모으는 걸 방해하는 가장 큰 적이에요. 게다가 전세사기 리스크도 높습니다.<br>
            <div class='action-box'>
                <b>🚀 긴급 주거 상향 탈출 전략</b>
                <ul class='step-list'>
                    <li>여러분은 자립준비청년 1순위 자격이 있습니다. 보증금 100만 원이면 안전한 LH 주택에 들어갈 수 있습니다.</li>
                    <li>당장 멘토에게 연락해 <b>'LH 전세임대 상시 모집'</b> 신청 절차를 밟으세요. 아까운 월세 지출을 지금 당장 절반 이하로 줄여야 자립에 성공합니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 주거취약계층 긴급 구제 진단</h3>
            지금 고시원이나 여관 같은 환경은 여러분의 미래를 설계하기에 너무 힘든 곳이에요. 국가의 도움을 당당히 받으세요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 긴급 솔루션</b><br>
                <b>'주거상향 지원사업'</b>을 신청하세요! 보증금 0원, 이사비 지원, 세탁기나 냉장고 같은 필수 가전 지원까지 싹 다 받으며 즉시 깨끗한 공공임대아파트로 이사할 수 있습니다. 당신의 정당한 권리이니 지금 바로 저에게 연락주세요.
            </div>
        </div>
        """
    return report

# 6. 미래 단계별 리포트 생성 함수 
def generate_step_report(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9; background-color:#F0F7FA;'><b>📅 {age}세 시점의 목표:</b> {fam} / {house} 거주</div>"
    
    if not sub_status:
        report += f"<div class='emergency-box'><b>⚠️ 경고:</b> 청약 납입 중단 시 향후 아파트 입주 순위에서 밀려납니다. 월 2만 원은 자존심이라 생각하고 지켜내야 해요!</div>"

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 전세임대 실전 공략 가이드 (A4 1장 분량)</h4>
            내가 살고 싶은 동네의 민간 빌라나 오피스텔을 직접 골라오면 LH가 대신 계약해주는 제도예요. 아주 자유롭죠!<br>
            <div class='action-box'>
                <b>📌 실전 권리분석 90% 절대 규칙</b>
                부동산 가서 "LH 전세 되나요?" 묻기 전에 직접 등기부등본을 확인하세요.<br>
                <b>👉 공식: (집주인 빚 + 내 보증금) ÷ 집값 ≤ 90%</b><br>
                이 숫자가 90이 넘으면 LH가 승인을 안 해줍니다. 부동산 사장님께 처음부터 "부채비율 90% 이하로 깨끗한 집만 보여주세요"라고 당당하게 말하세요!
            </div>
            {get_living_guide_book("전세임대")}
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 매입임대 줍줍 전략과 지역 선정 (A4 1장 분량)</h4>
            LH가 집주인이라 전세사기 걱정 0%! 에어컨, 세탁기 등 풀옵션이 많아 몸만 들어가면 되는 훌륭한 제도예요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 '줍줍' 비밀 타이밍</b><br>
                매주 금요일 오후에 LH청약플러스 앱을 확인하세요. 당첨자가 포기한 빈집 공고(수시 모집)가 올라온답니다.<br>
                👉 <b>행동 지침:</b> 마이페이지에서 <b>[관심지역 알림 - 인천광역시]</b>를 꼭 켜두세요. 알람이 울리면 남들보다 먼저 신청하는 게 핵심이에요!
            </div>
            {get_living_guide_book("매입임대")}
        </div>
        """
    elif "건설임대" in house or "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 아파트(건설/통합) 가점 관리와 40㎡ 법칙</h4>
            단지형 아파트로 보안과 인프라가 최고예요. 최장 30년까지 거주가 보장되는 꿈의 정착지입니다.<br>
            <div class='action-box'>
                <b>📌 1인 가구 40㎡(12평) 제한 법칙</b>
                혼자 살 때는 법적으로 큰 평수에 못 들어갑니다. 큰 집을 원한다면 결혼 후 가족이 늘어났을 때 상향 지원하는 전략을 짜야 해요.
            </div>
            <div class='tip-box'>
                <b>💡 배점표 만점 전략</b><br>
                인천 거주 기간과 청약 납입 횟수(60회 이상 만점)를 관리하세요. 특히 인천에서 주소지를 함부로 옮기면 점수가 깎이니 주의해야 합니다.
            </div>
            {get_living_guide_book("건설임대")}
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 공공분양 '뉴홈' - 내 집 마련 종착지 전략</h4>
            주변 시세보다 30% 저렴하게 온전한 내 집을 갖는 방법이에요. 나중에 집값이 오르면 수익을 LH와 나누는 '나눔형'은 초기 자금 부담이 아주 적어요.<br>
            <div class='action-box'>
                <b>📌 당첨과 대출을 위한 신용 사수</b>
                <ul class='step-list'>
                    <li><b>청약 인정 총액:</b> 분양 당첨은 횟수보다 '납입 금액'이 중요해요. 여유 생기면 즉시 자동이체를 <b>월 10만 원</b>으로 올리세요.</li>
                    <li><b>DSR 신용 점수:</b> 당첨되어도 신용등급 낮으면 대출 거절돼요. <b>현금서비스, 할부 리볼빙, 카드론</b>은 절대 금물입니다! 신용이 곧 돈이라는 걸 명심하세요.</li>
                </ul>
            </div>
        </div>
        """
    return report

# 7. 리포트 출력 로직 시작
if submit_btn:
    # 리포트 메인 제목
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵 백과사전</div>', unsafe_allow_html=True)
    st.write(f"**수신자:** {user_name} 님 | **발급기관:** 인천자립지원전담기관 | **담당자:** 김정현")

    # [1단계] 현재
    st.markdown('<div class="section-title">1단계. 현재의 나 : 출발선 정밀 진단</div>', unsafe_allow_html=True)
    st.markdown(analyze_now_step(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # [2단계] 10년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2단계. 10년 후 ({current_age+10}세) : 주거 기반 구축 가이드</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # [3단계] 20년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3단계. 20년 후 ({current_age+20}세) : 주거 안정 및 상향 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # [4단계] 30년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4단계. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # [5단계] 정보망 및 편지
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5단계. 든든한 조력 정보망 (필수 사이트)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr)</b><br>
        실제 집 공고를 보고 신청하는 핵심 창구입니다. 앱을 설치하고 '인천 관심지역 알림' 설정을 반드시 하세요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr)</b><br>
        전국 모든 주거 복지 제도를 검색할 수 있어요. '자가진단' 기능을 통해 내 점수를 미리 계산해 보세요.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
        우리 청년들만을 위해 주거, 교육, 금융 정보를 모두 모아둔 전용 포털입니다. 아주 유용해요.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr)</b><br>
        나라에서 빌려주는 이자 저렴한 대출(버팀목, 디딤돌 등) 상품을 한눈에 비교할 수 있습니다.
        </div>
    """, unsafe_allow_html=True)

    # 담당자 연락처 마감
    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                이 로드맵을 보다가 어려운 말이 있거나 상황이 바뀌어 계획을 수정하고 싶다면<br>
                <b>절대 혼자 고민하지 말고 저에게 연락 주세요.</b><br>
                당신의 든든한 내 편이 되어 함께 가장 좋은 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 8. 춤추는 집 캐릭터 인쇄 버튼 (인쇄 시 자동 숨김)
    st.markdown("---")
    components.html(
        """
        <center>
            <a href="#" onclick="window.parent.print(); return false;" title="리포트 전체를 PDF로 저장하기">
                <img src="https://media.giphy.com/media/ic06p9J076137681I3/giphy.gif" width="100px" style="border-radius:50%; box-shadow:0 4px 10px rgba(0,0,0,0.1); cursor:pointer;">
            </a>
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">위 캐릭터를 누르면 전체 리포트가 A4 규격으로 자동 분할되어 출력(저장)됩니다.</p>
        </center>
        """,
        height=180
    )