import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (가독성 및 🖨️ PDF 전체 페이지 인쇄 완벽 제어)
st.markdown("""
    <style>
    /* 기본 폰트 및 배경 설정 */
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.7rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    /* 카드 및 박스 디자인 */
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    .action-box { background-color: #F4F9FF; padding: 22px; border-radius: 10px; border-left: 6px solid #3498DB; margin: 15px 0;}
    .emergency-box { background-color: #FEF5F5; padding: 22px; border-radius: 10px; border-left: 6px solid #E74C3C; margin: 15px 0; color: #C0392B;}
    .tip-box { background-color: #FFF9E6; padding: 22px; border-radius: 10px; border-left: 6px solid #F1C40F; margin: 15px 0; color: #4D5656; font-size: 1rem; line-height: 1.7;}
    .step-list { margin-left: 20px; margin-bottom: 15px; }

    /* 🖨️ PDF 인쇄를 위한 마법의 CSS (스크롤 잘림 방지용) */
    @media print {
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"] {
            height: auto !important; min-height: 100% !important; max-height: none !important;
            overflow: visible !important; display: block !important; position: relative !important; background-color: white !important;
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

# 3. 실무 규칙 가이드 함수 (계약/갱신/연체/파손)
def get_lh_rules_detail(house_type):
    rules = ""
    if "전세임대" in house_type:
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 갱신 및 기간 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년 단위로 계약을 새로 해요. 총 14회까지 재계약이 가능해서 <b>최장 30년</b>까지 살 수 있답니다.</li>
                <li><b>재계약 절차:</b> 계약 끝나기 3개월 전 LH에서 집으로 안내 우편을 보내요. 이때 당황하지 말고 <b>등본, 가족관계증명서, 소득 증빙 서류</b>를 준비해서 LH 지사나 지정된 법무법인에 제출하면 돼요.</li>
                <li><b>임대료(이자) 계산:</b> 지원금(1.2억 기준)에서 내 보증금을 뺀 나머지 금액에 대해 1~2% 이자를 내요. 자립준비청년은 여기서 50%를 할인받아 매달 약 5~8만 원 정도만 내면 된답니다.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 살면서 마주할 위기 대처법</b>
            <ul class='step-list'>
                <li><b>이자 연체 시:</b> 이자가 3개월 이상 밀리면 LH에서 계약 해지 통보가 올 수 있어요. 돈이 부족하면 무조건 피하지 말고 <b>LH 관할 지역본부 전세임대팀</b>에 전화해서 '분할 납부'가 가능한지 사정을 꼭 말해야 해요.</li>
                <li><b>집 수리 문제:</b> 형광등, 수도꼭지 건전지 같은 소모품은 내가 갈아야 해요. 하지만 <b>보일러 고장, 벽면 누수, 싱크대 파손</b>처럼 큰 문제는 집주인이 고쳐줘야 해요. 절대 내 돈으로 먼저 고치지 말고 부동산 사장님께 먼저 말하세요!</li>
                <li><b>이사 가고 싶을 때(이주):</b> 계약 중간에 이사 가려면 최소 2개월 전에는 LH에 <b>'이주 신청서'</b>를 내야 해요. 그래야 다음 집 보증금 지원을 차질 없이 받을 수 있답니다.</li>
            </ul>
        </div>
        """
    elif "매입임대" in house_type:
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 갱신 및 기간 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년 단위로 재계약하며, 무주택 요건만 유지하면 <b>최장 20년</b>까지 거주할 수 있어요.</li>
                <li><b>임대료 수준:</b> 시세의 30~50%로 아주 저렴해요. 보증금 100~200만 원에 월세 10~20만 원 내외예요.</li>
                <li><b>재계약 주의점:</b> 재계약 시점에 취업을 해서 소득이 기준보다 높아지면 임대료가 20~80%까지 할증(추가 납부)될 수 있다는 점을 미리 알고 돈을 모아둬야 해요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 살면서 마주할 위기 대처법</b>
            <ul class='step-list'>
                <li><b>월세 연체:</b> 월세가 밀리면 LH 주거지원 지사에서 연락이 와요. 3회 이상 연체 시 퇴거 대상이 될 수 있으니 주의해야 해요. 자동이체를 꼭 걸어두세요!</li>
                <li><b>시설 고장:</b> 매입임대는 LH가 집주인이라 관리가 편해요. 집안 시설이 고장 나면 <b>'유지보수 접수센터(1600-1004)'</b>로 전화 한 통만 하면 LH에서 기사님을 보내서 고쳐줍니다.</li>
                <li><b>해약 및 퇴거:</b> 나가고 싶을 땐 한 달 전에 <b>'해약 신청서'</b>를 관리실이나 지사에 내야 보증금을 제날짜에 돌려받아요.</li>
            </ul>
        </div>
        """
    else: # 건설/통합/분양
        rules = """
        <div class='action-box'>
            <b>🗓️ 계약 및 생활 가이드</b>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 아파트는 2년 단위 갱신이며 소득 요건 유지 시 <b>최장 30년</b> 거주가 가능해요.</li>
                <li><b>관리비 주의:</b> 아파트는 월세 외에 '관리비'가 따로 나와요. 1인 가구 기준 약 10~15만 원 정도 나오니 예산을 짤 때 월세+관리비를 함께 생각해야 해요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <b>🚨 사고 예방 및 불이익</b>
            <ul class='step-list'>
                <li><b>불법 전대 금지:</b> 친구나 아는 사람에게 내 집을 빌려주고 돈을 받는 건 불법이에요. 걸리면 즉시 쫓겨나고 향후 5년 동안 나라에서 주는 집에는 절대 못 들어가는 큰 벌을 받아요.</li>
                <li><b>관리실 활용:</b> 아파트 살면서 층간소음이나 고장 문제가 생기면 1차적으로 <b>아파트 관리사무소</b>에 가서 도움을 청하세요. 혼자 싸우지 않아도 된답니다.</li>
            </ul>
        </div>
        """
    return rules

# 4. 분석 알고리즘 (현재 진단)
def analyze_current(assets, now_house, now_sub):
    report = ""
    # 청약 진단 (A4 반 페이지 분량 디테일)
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 나의 인생을 바꾸는 마법의 입장권</h3>
            지금 통장이 없다면 미래에 나라에서 지어주는 깨끗하고 싼 아파트는 포기하는 것과 같아요. 남들보다 늦기 전에 지금 당장 준비해야 합니다.<br>
            <div class='action-box'>
                <b>✅ 전문가가 제안하는 긴급 행동 지침</b>
                <ul class='step-list'>
                    <li><b>은행 방문:</b> 신분증만 들고 은행에 가서 <b>'청년주택드림청약통장'</b>을 만들어 달라고 하세요. (일반 청약보다 이자가 최대 4.5%로 매우 높아요!)</li>
                    <li><b>자동이체 설정:</b> 한 달에 딱 2만 원만 넣어두세요. 나중에 아파트에 들어갈 때 '총액'보다 <b>'몇 번이나 꾸준히 냈는지(횟수)'</b>가 당첨을 결정하는 핵심 가산점(최대 6점)이 된답니다.</li>
                    <li><b>자금 확보:</b> 군대에 간다면 군인 적금과 연계해서 더 큰 혜택을 누릴 수 있으니 포기하지 마세요.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 자립의 첫걸음</h3>
            지금처럼 연체 없이 꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 여러분을 지켜주는 가장 큰 무기가 될 거예요. 정말 잘하고 계세요!<br>
            <div class='tip-box'>
                <b>💡 멘토가 알려주는 위기 탈출 비밀 꿀팁</b><br>
                살다 보면 너무 급하게 목돈이 필요해서 청약 통장을 깨고 싶어지는 순간이 올 수 있어요. 그럴 때 <b>절대 해지하지 말고, '청약예금 담보대출'을 알아보세요.</b> 내가 통장에 넣은 돈의 90%까지 아주 싼 이자로 은행에서 빌릴 수 있어요. 이렇게 하면 통장의 소중한 점수(납입 회차)를 지키면서 급한 불을 끌 수 있답니다!
            </div>
        </div>
        """

    # 주거 진단 (현재 상황별 돈 이야기 + 디테일)
    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 소년소녀가정 전세임대 거주 진단</h3>
            <b>주요 혜택:</b> 현재 여러분은 만 20세까지 나라에서 전세지원금 이자를 <b>'0원'</b>으로 만들어주는 최고의 혜택 기간에 있어요. 주거비 부담이 전혀 없는 이 시기를 절대 그냥 보내면 안 돼요.<br>
            <div class='action-box'>
                <b>💰 돈 모으는 실전 지침</b>
                <ul class='step-list'>
                    <li><b>이자가 생기는 시점:</b> 만 22세 이후부터는 지원금 1억 기준, 한 달에 약 8~16만 원의 이자가 발생해요.</li>
                    <li><b>저축 목표:</b> 주거비가 0원인 지금! 매월 20만 원씩 무조건 '없는 돈'이라 생각하고 저축하세요. 이렇게 5년만 모아도 나중에 이사를 가거나 독립할 때 수천만 원의 든든한 밑천이 된답니다.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 자립준비청년 전형 거주 진단</h3>
            <b>주요 혜택:</b> 보호 종료 후 5년 동안 임대료 50% 감면 특례를 아주 현명하게 잘 쓰고 계시네요! 보통 월세가 10~20만 원대인데, 감면을 받으면 5~10만 원대로 뚝 떨어졌을 거예요.<br>
            <div class='tip-box'>
                <b>💡 월세를 '치킨 값'으로 만드는 비밀 (상호전환)</b><br>
                현재 가용 자산 {assets}만 원이 있다면, 혹은 알바비를 모았다면 LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원 단위로 LH에 추가 입금하면 연 6~7%의 엄청난 이율로 계산해서 매월 내는 월세를 확 깎아준답니다. 은행 적금보다 이득이니 목돈이 생길 때마다 보증금으로 전환해 보세요!
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 일반 민간 월세/전세 거주 진단</h3>
            <b>위험 요인:</b> 스스로 집을 구한 건 훌륭하지만, 매달 소멸되는 비싼 월세(40~60만 원)는 여러분이 종잣돈을 모으는 걸 방해하는 가장 큰 적이에요. 게다가 전세사기 리스크도 높죠.<br>
            <div class='action-box'>
                <b>🚀 긴급 주거 상향 전략</b>
                <ul class='step-list'>
                    <li><b>1순위 카드 사용:</b> 여러분은 자립준비청년 1순위 자격이 있어요. 보증금 100만 원이면 안전한 LH 주택에 들어갈 수 있습니다.</li>
                    <li><b>당장 행동하기:</b> 멘토에게 연락해서 'LH 전세임대 상시 모집' 신청 절차를 밟으세요. 아까운 월세 지출을 지금 당장 절반 이하로 줄여야 자립에 성공합니다.</li>
                </ul>
            </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 고시원/여관 거주 긴급 진단</h3>
            지금 환경은 심신의 안정과 성장을 방해하는 매우 힘든 시기예요. 절대 혼자 힘으로 버티려 하지 마세요. 국가가 여러분을 돕기 위해 만든 제도가 있어요.<br>
            <div class='tip-box'>
                <b>💡 멘토가 드리는 긴급 솔루션</b><br>
                <b>'주거취약계층 주거상향 지원사업'</b>을 신청하세요! 보증금 0원, 이사비 지원, 세탁기나 냉장고 같은 생필품 지원까지 싹 다 받으면서 깨끗한 아파트나 빌라로 즉시 이사할 수 있습니다. 당신의 권리이니 지금 바로 저(멘토)에게 연락주세요. 함께 길을 찾아줄게요.
            </div>
        </div>
        """
    return report

# 5. 미래 로드맵 분석 알고리즘 (나이별 상세 + 거주 가이드)
def generate_future_detail(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9; background-color:#F0F7FA;'><b>📅 {age}세 시점의 목표:</b> {fam}와 함께 {house} 거주</div>"
    
    if not sub_status:
        report += """
        <div class='emergency-box'>
            <b>⚠️ 경고: 청약 납입 중단 확인</b><br>
            청약을 중단하면 나중에 넓은 아파트로 이사 가거나 내 집을 마련할 때 다른 사람에게 순위가 밀려 탈락하게 돼요. 형편이 어렵더라도 월 2만 원 자동이체는 끝까지 방어하기를 다정하게 권장해요!
        </div>
        """

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 전세임대 완벽 정복 - 안전한 집 고르기와 비용 (A4 1장 분량)</h4>
            내가 원하는 동네의 깨끗한 민간 빌라나 오피스텔을 직접 골라오면, LH가 대신 전세 계약을 맺어주는 아주 자유로운 제도예요.<br>
            <div class='action-box'>
                <b>📌 실전 권리분석 90% 규칙</b>
                부동산 가서 "LH 전세 되나요?"라고 묻기 전에 직접 등기부등본을 보세요.<br>
                <b>👉 규칙: (집주인의 은행 빚 + 내 보증금) ÷ 집값 ≤ 90%</b><br>
                이 숫자가 90이 넘으면 LH가 승인을 안 해줘요. 부동산 사장님께 처음부터 "부채비율 90% 이하로 깨끗한 집만 보여주세요"라고 당당하게 말하세요!
            </div>
            {get_lh_rules_detail("전세임대")}
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 매입임대 완벽 정복 - 줍줍 전략과 지역 선정 (A4 1장 분량)</h4>
            LH가 도심의 튼튼한 집을 사들여서 저렴하게 빌려주는 제도로, 전세사기 걱정이 0%예요. 에어컨/세탁기 등 풀옵션이 많아 초기 독립 비용을 아끼기 최고죠.<br>
            <div class='tip-box'>
                <b>💡 멘토의 '줍줍' 비밀 타이밍</b><br>
                매입임대는 인기가 많지만 계약을 포기하는 빈집이 매주 나와요. 이걸 '수시 모집'이라 해요.<br>
                👉 <b>행동 지침:</b> 스마트폰에 'LH청약플러스' 앱을 깔고 마이페이지에서 <b>[관심지역 알림 - 인천광역시]</b>를 꼭 켜두세요! 금요일 오후에 알람이 울리면 남들보다 먼저 신청하는 게 핵심이에요.
            </div>
            {get_lh_rules_detail("매입임대")}
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 아파트(건설임대) 가점 관리와 40㎡ 법칙 (A4 1장 분량)</h4>
            경비실, 주차장, 쾌적한 환경이 보장된 단지형 아파트예요. 최장 30년까지 이사 걱정 없이 안심하고 살 수 있는 꿈의 베이스캠프랍니다.<br>
            <div class='action-box'>
                <b>📌 1인 가구 40㎡ 제한 법칙</b>
                혼자 사는 1인 가구는 전용면적 <b>40㎡(약 12평) 이하</b>만 지원할 수 있어요. 넓은 평수에 지원하면 서류에서 100% 탈락하니 주의하세요! 나중에 결혼해서 {fam}가 되면 그때 더 넓은 평수로 상향 지원하는 전략을 짜야 해요.
            </div>
            {get_lh_rules_detail("건설임대")}
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 통합공공임대: 소득이 늘어도 안심하는 평생 주택</h4>
            2026년 최신 제도로, 소득이 높아져도 쫓겨나지 않고 소득에 비례해 임대료만 내며 30년 동안 살 수 있는 최고의 방패입니다.<br>
            <div class='tip-box'>
                <b>💡 신도시 신규 단지를 공략하세요</b><br>
                검단신도시나 계양신도시 등 신규 단지 공고를 노리세요. 다자녀, 맞벌이 가산점이 커서 가족이 늘어났을 때 가장 유리한 전형이에요. 최대 84㎡(약 34평) 아파트까지 배정받을 수 있어 아이 키우기에 최적입니다.
            </div>
            {get_lh_rules_detail("통합공공")}
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 공공분양 '뉴홈' - 자가 소유와 DSR 신용관리</h4>
            30년 로드맵의 최종 목표! 시세보다 30% 저렴하게 온전한 내 집을 갖는 방법이에요. 나중에 집값이 오르면 수익을 LH와 나누는 '나눔형'은 초기 자본이 적어도 가능해요.<br>
            <div class='action-box'>
                <b>📌 당첨과 대출을 위한 신용 사수</b>
                <ul class='step-list'>
                    <li><b>청약 인정 총액:</b> 분양은 '납입 금액'이 중요해요. 여유 생기면 즉시 자동이체 금액을 <b>월 10만 원</b>으로 올리세요.</li>
                    <li><b>DSR 신용 점수:</b> 당첨되어도 신용등급 낮으면 대출 거절돼요. <b>잦은 현금서비스, 카드 리볼빙, 카드론</b>은 절대 금물이에요! 신용 관리가 곧 돈이라는 걸 명심하세요.</li>
                </ul>
            </div>
        </div>
        """
    return report

# 6. 최종 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**대상자:** {user_name} 님 | **작성일:** 2026년 3월 6일")

    st.markdown('<div class="section-title">1단계. 현재의 나 : 출발선 진단과 비상 전략</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2단계. 10년 후 ({current_age+10}세) : 주거 기반 구축과 실전 가이드</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3단계. 20년 후 ({current_age+20}세) : 주거 안정 및 상향 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4단계. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_future_detail(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5단계. 든든한 조력망 및 멘토의 편지</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr)</b><br>
        실제 집 공고를 보고 신청하는 곳! 스마트폰에 앱을 깔고 '관심지역 알림'을 꼭 켜두세요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr)</b><br>
        '자가진단' 메뉴를 누르면 내 나이와 소득에 딱 맞는 제도를 알아서 찾아줍니다.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
        자립준비청년들만을 위한 주거, 금융, 취업 정보가 가득한 전용 포털입니다.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr)</b><br>
        이자가 아주 저렴한 나라의 대출 상품(버팀목, 디딤돌 등)을 알아볼 수 있는 공식 창구입니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                살면서 계획은 언제든 변할 수 있고 상황도 달라질 수 있습니다.<br>
                혼자 고민하다 기회를 놓치지 말고, 이 로드맵을 보다가 궁금한 게 생기면<br>
                <b>언제든 저에게 연락 주세요.</b> 당신의 든든한 내 편이 되어 함께 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당자 김정현 (070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 6. 움직이는 캐릭터 인쇄 버튼 (인쇄 시 자동 숨김)
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