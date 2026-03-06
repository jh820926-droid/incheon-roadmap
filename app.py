import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(
    page_title="2026 인천자립 주거로드맵 - 주거 안심 백과사전",
    page_icon="🏠",
    layout="centered"
)

# 2. 🖨️ PDF 전체 페이지 인쇄 및 가독성 극대화를 위한 CSS
st.markdown("""
    <style>
    /* 웹 화면 디자인 */
    .main-title { font-size: 2.5rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.2rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 2rem; color: #154360; font-weight: 800; border-bottom: 4px solid #1ABC9C; padding-bottom: 10px; margin-top: 50px; margin-bottom: 30px; text-align: center;}
    .section-title { font-size: 1.6rem; color: #2C3E50; font-weight: 800; border-left: 8px solid #1ABC9C; padding-left: 15px; margin-top: 50px; margin-bottom: 20px;}
    
    /* 카드 및 박스 디자인 */
    .card-box { background-color: #FFFFFF; padding: 35px; border-radius: 20px; box-shadow: 0 6px 20px rgba(0,0,0,0.06); border: 1px solid #EAECEE; margin-bottom: 30px; line-height: 2.0;}
    .action-box { background-color: #F0F7FF; padding: 25px; border-radius: 12px; border-left: 6px solid #3498DB; margin: 20px 0;}
    .emergency-box { background-color: #FFF5F5; padding: 25px; border-radius: 12px; border-left: 6px solid #E74C3C; margin: 20px 0; color: #C0392B;}
    .tip-box { background-color: #FFF9E6; padding: 25px; border-radius: 12px; border-left: 6px solid #F1C40F; margin: 20px 0; color: #4D5656;}
    
    .guide-label { font-weight: 800; color: #2E86C1; display: block; margin-bottom: 10px; font-size: 1.1rem; }
    .step-list { margin-left: 20px; margin-bottom: 20px; list-style-type: disc; }
    .step-list li { margin-bottom: 15px; }

    /* 🖨️ PDF 인쇄 시 스크롤 제한 해제 및 레이아웃 강제 펼침 */
    @media print {
        header, footer, [data-testid="stSidebar"], [data-testid="stForm"], button { display: none !important; }
        .main-title, .sub-title, img, hr { display: none !important; }
        
        html, body, #root, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"] {
            height: auto !important;
            min-height: 100% !important;
            overflow: visible !important;
            display: block !important;
            position: static !important;
            background-color: white !important;
        }
        
        .page-break {
            page-break-before: always !important;
            display: block !important;
            height: 0px !important;
            border: none !important;
        }
        
        .card-box { box-shadow: none !important; border: 1px solid #BDC3C7 !important; break-inside: avoid; }
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

# 3. 30년 생애주기 입력 폼
st.subheader("📋 Step 1. 나의 30년 주거 자립 계획 설계")

fam_options = ["1인 가구 (혼자 생활)", "2인 가구 (부부/형제/친구)", "3인 가구 (부부+자녀1)", "4인 이상 (다자녀 가정)"]
house_options = [
    "전세임대 (내가 고른 민간주택 지원)", 
    "매입임대 (LH가 매입한 안심주택)", 
    "건설임대 (국민/행복/영구 아파트)", 
    "통합공공임대 (최장 30년 거주 아파트)", 
    "공공분양 (자가 소유 내 집 마련)"
]
current_house_options = [
    "LH 전세임대 (소년소녀가정 전형 거주)",
    "LH 전세/매입임대 (자립준비청년 전형 거주)",
    "일반 무상거주 (시설/친척/지인 집)",
    "일반 민간 임대 (월세/전세 계약 중)",
    "주거취약계층 (고시원/여관/반지하 등)"
]

with st.form("lifecycle_form"):
    st.info("💡 지금 나의 상황과 미래의 꿈꾸는 모습을 선택해 주세요. 이 데이터를 기반으로 800줄 분량의 맞춤형 지침서가 생성됩니다.")
    user_name = st.text_input("👤 성함 (리포트 수신인)", "김자립")
    col1, col2 = st.columns(2)
    with col1:
        current_age = st.number_input("🎂 현재 나이", min_value=15, max_value=40, value=20)
        assets = st.number_input("💰 현재 가용 자산 (만원 단위)", min_value=0, value=100)
    with col2:
        is_vulnerable = st.checkbox("보호종료(자립준비) 청년 해당 여부", value=True)
        now_sub = st.radio("🏦 주택청약통장 유무", ["네, 가입해서 넣고 있어요", "아니요, 아직 없거나 쉬고 있어요"])
    now_house = st.selectbox("🏠 현재 거주 중인 주거 형태", current_house_options)

    st.markdown("---")
    st.markdown("#### 🌱 [10년 후] 주거 목표")
    fam_10 = st.selectbox("10년 후 가구 구성", fam_options, index=0)
    house_10 = st.selectbox("10년 후 희망 전형", house_options, index=1)
    sub_10 = st.checkbox("10년 후에도 청약 유지를 약속하시겠습니까?", value=True, key="s10")

    st.markdown("---")
    st.markdown("#### 🏡 [20년 후] 주거 목표")
    fam_20 = st.selectbox("20년 후 가구 구성", fam_options, index=1)
    house_20 = st.selectbox("20년 후 희망 전형", house_options, index=3)
    sub_20 = st.checkbox("20년 후에도 청약 유지를 약속하시겠습니까?", value=True, key="s20")

    st.markdown("---")
    st.markdown("#### 🌅 [30년 후] 영구 자립")
    fam_30 = st.selectbox("30년 후 가구 구성", fam_options, index=2)
    house_30 = st.selectbox("최종 종착지 주거 전형", house_options, index=4)
    sub_30 = st.checkbox("청약 통장으로 내 집 마련에 도전하시겠습니까?", value=True, key="s30")

    submit_btn = st.form_submit_button("🚀 나만의 주거 백과사전 리포트 생성", type="primary")

# 4. 실전 거주 가이드 함수 (압도적 디테일 - 떠먹여주는 정보)
def get_detailed_living_guide(house_type):
    if "전세임대" in house_type:
        return f"""
        <div class='action-box'>
            <span class='guide-label'>🗓️ 계약 갱신 및 기간 완벽 가이드</span>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년마다 계약을 갱신해요. 자립준비청년은 총 14회까지 가능해서 <b>최장 30년</b>까지 거주할 수 있답니다.</li>
                <li><b>재계약 절차:</b> 만료 3개월 전 LH에서 우편이 오면 **신분증, 등본, 가족관계증명서, 소득증빙서류**를 들고 지정된 법무법인이나 LH 지사를 방문하면 돼요.</li>
                <li><b>임대료(이자) 계산기:</b> 지원금(1.2억 기준)에서 내 보증금(5%, 600만원)을 뺀 1.14억에 대해 연 1~2% 이자를 내요. 자립준비청년 할인을 받으면 <b>한 달에 약 5~8만 원</b>이면 집세 해결!</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <span class='guide-label'>🚨 위기 발생! 멘토가 알려주는 대처법</span>
            <ul class='step-list'>
                <li><b>이자 연체:</b> 이자가 3개월 이상 밀리면 LH에서 집을 비워달라는 '해지 통보'가 와요. 돈이 부족하다면 무조건 피하지 말고 <b>LH 관할 지역본부 전세임대팀</b>에 전화해서 '분할 납부'를 요청하세요. 상담만 해도 시간을 벌 수 있어요.</li>
                <li><b>보일러나 수도 고장:</b> 형광등이나 건전지는 소모품이라 내가 사야 하지만, <b>보일러, 누수, 싱크대 노후</b>는 집주인이 고쳐줘야 해요. 절대 내 돈 먼저 쓰지 말고 부동산 사장님께 전화해서 "LH에 중재 요청할게요"라고 정중히 말씀하세요.</li>
                <li><b>이사 가고 싶을 때:</b> 계약 도중 이사 가려면 최소 2개월 전 <b>'이주 신청서'</b>를 LH에 내야 보증금을 다음 집으로 안전하게 옮길 수 있어요.</li>
            </ul>
        </div>
        """
    elif "매입임대" in house_type:
        return f"""
        <div class='action-box'>
            <span class='guide-label'>🗓️ 계약 갱신 및 기간 완벽 가이드</span>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 2년마다 재계약하며, 무주택 요건 유지 시 <b>최장 20년</b>까지 살 수 있어요.</li>
                <li><b>임대료 수준:</b> 시세의 30~50% 수준이에요. 보증금 100~200만 원에 월세 10~20만 원 내외로 전국에서 가장 저렴한 집이에요.</li>
                <li><b>재계약 주의점:</b> 재계약할 때 취업을 해서 소득이 오르면 임대료가 할증될 수 있으니 미리 목돈을 모아두는 게 좋아요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <span class='guide-label'>🚨 위기 발생! 멘토가 알려주는 대처법</span>
            <ul class='step-list'>
                <li><b>월세 연체:</b> 통장에 잔액이 없어 3회 이상 밀리면 LH 주거지원 지사에서 독촉이 와요. 연체료가 생각보다 비싸니 꼭 자동이체 잔액을 확인하세요.</li>
                <li><b>수리 문제:</b> 매입임대는 LH가 집주인이라 관리가 아주 잘 돼요. 집안 시설이 고장 나면 <b>'LH 유지보수 접수센터(1600-1004)'</b>로 전화하세요. 기사님이 무료로 고쳐주러 오십니다.</li>
                <li><b>해약 신청:</b> 갑자기 집을 나가야 한다면 최소 한 달 전에 <b>'해약 신청서'</b>를 지사에 내야 보증금을 제때 돌려받고 깔끔하게 마무리할 수 있어요.</li>
            </ul>
        </div>
        """
    else: # 건설/통합/분양
        return f"""
        <div class='action-box'>
            <span class='guide-label'>🗓️ 아파트 계약 및 생활 가이드</span>
            <ul class='step-list'>
                <li><b>갱신 주기:</b> 아파트는 2년 단위 갱신이며 <b>최장 30년</b> 거주가 가능해요.</li>
                <li><b>관리비 주의사항:</b> 아파트는 월세 외에 **관리비(약 10~15만 원)**가 따로 나와요. 예산을 짤 때 월세와 관리비를 합쳐서 생각해야 생활이 안정됩니다.</li>
                <li><b>청약 통장 유지:</b> 아파트 재계약 시 청약 통장을 유지하고 있는지 확인하는 경우가 많으니 절대 통장을 깨지 마세요.</li>
            </ul>
        </div>
        <div class='emergency-box'>
            <span class='guide-label'>🚨 사고 예방 및 불이익 주의</span>
            <ul class='step-list'>
                <li><b>불법 전대 절대 금지:</b> 친구나 아는 사람에게 내 집을 빌려주고 돈 받는 건 범죄예요! 적발 시 즉시 퇴거되고 향후 5년 동안 국가 주택 입주가 불가능해요.</li>
                <li><b>층간소음/시설고장:</b> 아파트 관리사무소는 여러분을 돕기 위해 있는 곳이에요. 이웃과 싸우지 말고 <b>관리사무소</b>를 통해 해결하세요.</li>
            </ul>
        </div>
        """

# 5. 분석 알고리즘 (현재 단계 - 압도적 정보량 복구)
def analyze_now_step_detail(assets, now_house, now_sub):
    report = ""
    # 청약 통장 디테일
    if "아니요" in now_sub:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 내 미래를 지키는 유일한 열쇠</h3>
            지금 통장이 없다는 건 나중에 국가가 주는 모든 주거 혜택을 포기하는 것과 같습니다. 오늘 당장 준비해야 합니다.<br>
            <div class='action-box'>
                <span class='guide-label'>✅ 멘토의 강력 추천 행동 지침</span>
                <ul class='step-list'>
                    <li>신분증만 들고 은행에 가서 <b>'청년주택드림청약통장'</b>을 개설하세요. 이자가 4.5%나 됩니다.</li>
                    <li>매달 딱 <b>2만 원</b>이라도 자동이체를 설정하세요. 금액보다 <b>'몇 번 꾸준히 냈는지(횟수)'</b>가 아파트 당첨을 결정하는 핵심 가산점(최대 6점)이 됩니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 자립의 시작입니다!</h3>
            꾸준히 넣은 횟수가 나중에 아파트에 들어갈 때 여러분을 지켜주는 가장 큰 무기가 될 거예요. 정말 잘하고 계십니다!<br>
            <div class='tip-box'>
                <span class='guide-label'>💡 급전이 필요할 때 꿀팁</span><br>
                혹시 살다가 목돈이 필요해 청약 통장을 깨고 싶을 때가 올 수 있어요. 그럴 때 <b>절대 해지하지 마세요!</b> 은행에 가서 <b>'청약 담보대출'</b>을 받으면 내가 넣은 돈의 90%까지 저렴한 이자로 빌려줍니다. 통장 점수는 지키고 위기는 넘길 수 있습니다.
            </div>
        </div>
        """

    # 현재 주거 진단
    if "소년소녀가정" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 소년소녀가정 전세임대 진단 리포트</h3>
            현재 만 20세까지 전세지원금 이자가 <b>'0원'</b>인 최고의 시기에 있습니다. 주거비 부담이 없는 이 시기를 절대 그냥 보내면 안 됩니다.<br>
            <div class='action-box'>
                <span class='guide-label'>💰 종잣돈 모으는 실전 지침</span>
                <ul class='step-list'>
                    <li>만 22세 이후부터는 지원금 1억 기준, 매달 약 8~16만 원의 이자가 발생합니다.</li>
                    <li><b>목표:</b> 주거비가 전혀 안 나가는 지금! 매월 20만 원씩 무조건 저축해서 5년 뒤 1,500만 원 이상의 독립 자금을 만드세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 자립준비청년 전형 거주 진단 리포트</h3>
            보호 종료 후 5년 동안 임대료 50% 감면 특례를 아주 잘 쓰고 계시네요! 지금은 월세가 5~10만 원대로 저렴할 거예요.<br>
            <div class='tip-box'>
                <span class='guide-label'>💡 월세를 '치킨 한 마리 값'으로 낮추는 비법 (상호전환)</span><br>
                지금 가용 자산 {assets}만 원이 있다면, 혹은 알바비를 모았다면 LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원당 연 6~7% 이율로 월세를 확 깎아줍니다. 은행 적금보다 훨씬 이득입니다.
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 일반 민간 월세 거주 진단 리포트</h3>
            매달 소멸되는 비싼 월세(40~60만 원)는 자립을 방해하는 가장 큰 적입니다. 전세사기 리스크도 매우 높습니다.<br>
            <div class='action-box'>
                <span class='guide-label'>🚀 긴급 주거 상향 탈출 전략</span>
                <ul class='step-list'>
                    <li>여러분은 자립준비청년 1순위 자격이 있습니다. 보증금 100만 원이면 안전한 LH 주택에 들어갈 수 있습니다.</li>
                    <li>지금 바로 멘토에게 연락해 <b>'LH 전세임대 상시 모집'</b> 신청 절차를 밟으세요. 아까운 월세 지출을 지금 당장 절반 이하로 줄여야 합니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 주거취약계층 긴급 지원 리포트</h3>
            지금 환경에서는 미래를 설계하기가 매우 어렵습니다. 국가의 도움을 당당히 받으세요.<br>
            <div class='tip-box'>
                <span class='guide-label'>💡 멘토의 긴급 솔루션</span><br>
                <b>'주거상향 지원사업'</b>을 신청하세요! 보증금 0원, 이사비 지원, 가전제품 지원까지 받으면서 즉시 깨끗한 공공임대주택으로 이사할 수 있습니다. 당신의 권리이니 지금 바로 저에게 연락주세요.
            </div>
        </div>
        """
    return report

# 6. 미래 단계별 리포트 생성 함수
def generate_step_report_rich(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:10px solid #2980B9; background-color:#F0F7FA;'><b>📅 {age}세 시점의 목표:</b> {fam} / {house} 거주</div>"
    
    if not sub_status:
        report += f"<div class='emergency-box'><b>⚠️ 주의:</b> 청약 납입 중단이 확인되었습니다. 이대로면 나중에 아파트 경쟁에서 무조건 탈락합니다. 월 2만 원은 끝까지 사수하세요!</div>"

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 전세임대 완벽 정복 - 안전한 집 고르기와 비용</h4>
            내가 원하는 동네의 민간 빌라나 오피스텔을 직접 골라오면 LH가 대신 계약해주는 최고의 제도예요.<br>
            <div class='action-box'>
                <span class='guide-label'>📌 실전 권리분석 90% 절대 규칙</span>
                부동산 사장님께 전화하기 전, 등기부등본을 떼서 직접 계산하세요.<br>
                <b>👉 공식: (집주인 대출 빚 + 내 보증금) ÷ 집값 ≤ 90%</b><br>
                이 숫자가 90이 넘으면 LH가 승인을 안 해줍니다. 사장님께 처음부터 "부채비율 90% 이하인 안전한 집만 보여주세요"라고 당당하게 말하세요!
            </div>
            {get_detailed_living_guide("전세임대")}
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 매입임대 완벽 정복 - 줍줍 전략과 지역 선정</h4>
            LH가 집주인이라 전세사기 걱정 0%! 에어컨, 세탁기 등 풀옵션이 많아 초기 독립 비용을 아끼기 최고예요.<br>
            <div class='tip-box'>
                <span class='guide-label'>💡 멘토의 '줍줍' 비밀 타이밍</span><br>
                스마트폰에 'LH청약플러스' 앱을 깔고 <b>[관심지역 알림 - 인천광역시]</b>를 꼭 켜두세요. 금요일 오후에 알람이 울리면 남들보다 먼저 신청하는 게 핵심이에요! 예비 번호라도 받아두면 순번이 반드시 옵니다.
            </div>
            {get_detailed_living_guide("매입임대")}
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 아파트(건설임대) 가점 관리와 40㎡ 법칙</h4>
            쾌적한 대단지 아파트예요. 최장 30년까지 거주가 보장되는 꿈의 베이스캠프랍니다.<br>
            <div class='action-box'>
                <span class='guide-label'>📌 1인 가구 40㎡ 제한 법칙</span>
                혼자 살 때는 전용면적 <b>40㎡(약 12평) 이하</b>만 지원할 수 있어요. 큰 평수에 지원하면 서류에서 100% 탈락하니 주의하세요! 나중에 결혼해서 가족이 늘어나면 그때 상향 지원하는 전략을 짜야 해요.
            </div>
            {get_detailed_living_guide("건설임대")}
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 통합공공임대: 소득이 늘어도 안심하는 평생 주택</h4>
            2026년 최신 제도로, 소득에 비례해 임대료만 조절하며 평생 살 수 있는 최고의 방패입니다.<br>
            <div class='tip-box'>
                <span class='guide-label'>💡 신도시 신규 단지를 공략하세요</span><br>
                검단신도시나 계양신도시 등 신규 단지 공고를 노리세요. 다자녀, 맞벌이 가산점이 커서 가족이 늘어났을 때 가장 유리한 전형이에요. 최대 84㎡(약 34평) 아파트까지 배정받을 수 있어 아이 키우기에 최적입니다.
            </div>
            {get_detailed_living_guide("통합공공")}
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 공공분양 '뉴홈' - 자가 소유와 DSR 신용관리</h4>
            주변 시세보다 30% 저렴하게 온전한 내 집을 갖는 방법이에요. 나눔형 전형은 초기 자본이 적어도 가능해요.<br>
            <div class='action-box'>
                <span class='guide-label'>📌 당첨과 대출을 위한 신용 사수</span>
                <ul class='step-list'>
                    <li><b>청약 인정 총액:</b> 분양 당첨은 매달 <b>월 10만 원</b>씩 꾸준히 인정받는 게 핵심이에요. 여유 생기면 즉시 자동이체 금액을 올리세요.</li>
                    <li><b>DSR 신용 점수:</b> 당첨되어도 신용등급 낮으면 대출 거절돼요. <b>잦은 현금서비스, 카드 리볼빙, 카드론</b>은 절대 금물입니다! 신용이 곧 돈입니다.</li>
                </ul>
            </div>
        </div>
        """
    return report

# 7. 최종 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵 백과사전</div>', unsafe_allow_html=True)
    st.write(f"**수신인:** {user_name} 님 | **발급기관:** 인천자립지원전담기관 | **담당자:** 김정현")

    # [1단계] 현재
    st.markdown('<div class="section-title">Step 1. 현재의 나 : 출발선 진단과 비상 전략</div>', unsafe_allow_html=True)
    st.markdown(analyze_now_step_detail(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # [2단계] 10년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 2. 10년 후 ({current_age+10}세) : 주거 기반 구축 가이드</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report_rich(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # [3단계] 20년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 3. 20년 후 ({current_age+20}세) : 주거 안정 및 상향 전략</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report_rich(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # [4단계] 30년 후
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Step 4. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_step_report_rich(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # [5단계] 정보망
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Step 5. 든든한 조력 정보망 (필수 사이트 주소)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (https://apply.lh.or.kr)</b><br>
        실제 집 공고를 보고 신청하는 곳! 앱을 설치하고 '관심지역 알림' 설정을 반드시 하세요.<br><br>
        <b>2️⃣ 마이홈 포털 (https://www.myhome.go.kr)</b><br>
        전국 모든 주거 복지 제도를 검색할 수 있어요. '자가진단' 기능을 꼭 사용해 보세요.<br><br>
        <b>3️⃣ 자립정보ON (https://jaripon.ncrc.or.kr)</b><br>
        우리 청년들만을 위해 주거, 교육, 금융 정보를 모두 모아둔 전용 포털입니다.<br><br>
        <b>4️⃣ 주택도시기금 (https://nhuf.molit.go.kr)</b><br>
        나라에서 빌려주는 이자 저렴한 대출 상품들을 한눈에 비교할 수 있습니다.
        </div>
    """, unsafe_allow_html=True)

    # 담당자 연락처
    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                이 리포트를 보다가 어려운 말이 있거나 연체/수리 등 위기 상황이 생기면<br>
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
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">위 캐릭터를 누르면 전체 리포트가 A4 규격으로 깔끔하게 자동 분할되어 출력(저장)됩니다.</p>
        </center>
        """,
        height=180
    )