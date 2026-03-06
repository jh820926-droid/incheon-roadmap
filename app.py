import streamlit as st
import streamlit.components.v1 as components

# 1. 앱 기본 설정
st.set_page_config(page_title="2026 인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (인쇄 최적화 및 가독성 극대화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: 900; text-align: center; margin-bottom: 5px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 30px;}
    .report-header { font-size: 1.8rem; color: #154360; font-weight: 800; border-bottom: 3px solid #1ABC9C; padding-bottom: 10px; margin-top: 20px; margin-bottom: 30px;}
    .section-title { font-size: 1.5rem; color: #2C3E50; font-weight: 800; margin-top: 30px; margin-bottom: 15px;}
    
    .card-box { background-color: #FFFFFF; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #EAECEE; margin-bottom: 25px; line-height: 1.9;}
    .action-box { background-color: #F4F9FF; padding: 20px; border-radius: 10px; border-left: 5px solid #3498DB; margin: 15px 0;}
    .tip-box { background-color: #FFF9E6; padding: 22px; border-radius: 10px; border-left: 5px solid #F1C40F; margin: 15px 0; color: #4D5656;}
    
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

# 3. 디테일 끝판왕 분석 알고리즘
def analyze_current(assets, now_house, now_sub):
    report = ""
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 자립의 가장 강력한 무기</h3>
            청약 통장은 단순히 저축이 아니라 <b>'공공 주택 입주권'</b>입니다. 지금 통장이 없다는 것은 미래의 모든 국가 주거 혜택을 포기하는 것과 같습니다.<br>
            <div class='action-box'>
                <b>✅ 전문가 긴급 처방</b>
                <ul style="margin-top:10px;">
                    <li><b>'청년주택드림청약통장'</b>으로 개설하세요. 이자율이 최대 4.5%로 매우 높습니다.</li>
                    <li>매달 2만 원이라도 자동이체를 설정하세요. 금액보다 <b>'납입 횟수'</b>가 가산점의 핵심(최대 6점)입니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏦 청약 통장: 아주 훌륭한 자립 태도</h3>
            꾸준한 납입은 미래의 배점 경쟁에서 압도적인 우위를 점하게 해줍니다. 정말 잘하고 계세요!<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                혹시 급전이 필요해 통장을 깨고 싶다면 <b>'청약예금 담보대출'</b>을 먼저 알아보세요. 내가 넣은 돈의 90%까지 아주 싼 이자로 빌릴 수 있어, 통장의 점수를 지키면서 위기를 넘길 수 있습니다.
            </div>
        </div>
        """

    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 소년소녀가정 전세임대 거주 중</h3>
            <b>장점:</b> 만 20세까지 전세지원금 이자가 0%입니다. 주거비가 아예 안 나가는 황금기죠.<br>
            <b>주의:</b> 만 22세 이후부터는 연 1~2%의 이자가 발생합니다. 1억 지원 기준 한 달에 약 8~16만 원 정도예요.<br>
            <div class='action-box'>
                <b>✅ 현재 시점 집중 과제</b>
                <ul style="margin-top:10px;">
                    <li><b>강제 저축:</b> 주거비가 0원인 지금, 나중에 낼 이자나 독립 자금을 위해 매월 20만 원씩 무조건 저축하세요.</li>
                    <li><b>권리분석 예습:</b> 지금 집의 등기부등본을 떼어보세요. (집주인 빚+내 보증금)이 집값의 90% 이하인지 확인하며 실무 감각을 익히세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 자립준비청년 전형 거주 중</h3>
            <b>장점:</b> 보호 종료 후 5년 동안 임대료 50% 감면 혜택을 받습니다.<br>
            <b>비용:</b> 보통 월세가 10~20만 원대인데, 감면받으면 5~10만 원대로 떨어집니다.<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁 (상호전환제도 활용)</b><br>
                현재 가용 자산 {assets}만 원이 있다면, LH에 <b>'전환보증금'</b>을 신청하세요. 100만 원 단위로 추가 입금 시 연 6~7% 이율로 계산하여 월세를 깎아줍니다. 월세를 '치킨 한 마리 가격'으로 만드는 재무 전략을 짜보세요.
            </div>
        </div>
        """
    elif "민간 임대" in now_house:
        report += """
        <div class='card-box'>
            <h3 style="color:#2C3E50;">🏠 일반 민간 월세/전세 거주 중</h3>
            <b>주의:</b> 매달 40~60만 원의 비싼 월세는 자립의 가장 큰 장애물입니다. 게다가 전세사기 리스크도 높죠.<br>
            <div class='action-box'>
                <b>✅ 긴급 탈출 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>1순위 권리 행사:</b> 자립준비청년 1순위 자격으로 보증금 100만 원이면 LH 안심 주택에 들어갈 수 있습니다.</li>
                    <li><b>즉시 신청:</b> LH청약플러스에서 '자립준비청년 전세임대 상시모집' 공고를 확인하고 지금 바로 신청하세요. 월세를 절반 이하로 줄여야 합니다.</li>
                </ul>
            </div>
        </div>
        """
    return report

def generate_future(age, fam, house, sub_status):
    report = f"<div class='card-box' style='border-left:8px solid #2980B9;'><b>📅 {age}세 목표:</b> {fam} / {house}</div>"
    
    if not sub_status:
        report += "<div class='action-box' style='border-left-color:#E74C3C;'><b>⚠️ 경고:</b> 청약 납입 중단 시 향후 아파트 입주 순위에서 밀려납니다. 단돈 2만 원이라도 유지를 권장합니다.</div>"

    if "전세임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 전세임대 실전 공략 가이드</h4>
            <b>장점:</b> 내가 원하는 위치의 깨끗한 민간 빌라나 오피스텔을 직접 골라 살 수 있습니다.<br>
            <b>임대료:</b> LH 지원금(수도권 약 1.2억) 중 내 보증금(5%)을 뺀 나머지 금액에 대해 연 1~2% 이자를 냅니다. 자립준비청년은 여기서 50%를 또 할인받아 한 달에 약 5~8만 원 정도면 충분합니다.<br>
            <div class='action-box'>
                <b>📌 실전 행동 지침</b>
                <ul style="margin-top:10px;">
                    <li><b>권리분석 90% 룰:</b> (선순위 채권+내 보증금) / 주택 가격 ≤ 90% 공식은 절대적입니다. 빚 많은 집은 LH가 승인 안 해줍니다.</li>
                    <li><b>부동산 매너:</b> 방문 시 "LH 전세 전용면적 85㎡ 이하 물건 있나요?"라고 미리 확인하세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "매입임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 매입임대 실전 공략 가이드</h4>
            <b>장점:</b> LH가 주인이라 전세사기 걱정 0%입니다. 에어컨, 냉장고 등 기본 가전이 빌트인된 경우가 많아 초기 비용이 거의 안 듭니다.<br>
            <b>임대료:</b> 주변 시세의 30~50% 수준입니다. 보증금 100~200만 원에 월세 10~20만 원 내외입니다.<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                <b>'줍줍' 타이밍 확보:</b> LH청약플러스 앱에서 '관심지역 알림(인천)'을 켜두세요. 당첨자가 포기한 빈집 공고(수시 모집)는 금요일 오후에 자주 올라옵니다. 예비 번호라도 받아두면 순서가 반드시 옵니다.
            </div>
        </div>
        """
    elif "건설임대" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 아파트(건설임대) 가점 관리법</h4>
            <b>장점:</b> 경비실, 주차장, 헬스장 등 인프라가 완벽합니다. 소득 요건 유지 시 최장 30년 거주 가능합니다.<br>
            <b>비용:</b> 시세 60~80% 수준입니다. 행복주택 기준 보증금 약 3~5천만 원, 월세 10~20만 원대입니다.<br>
            <div class='action-box'>
                <b>📌 배점표 만점 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>인천 거주 기간:</b> 주소지를 함부로 옮기지 마세요. 인천 거주 기간이 길수록 만점입니다.</li>
                    <li><b>청약 60회:</b> 금액 상관없이 '연체 없는 60회(5년)' 납입이 만점 기준입니다.</li>
                    <li><b>면적 주의:</b> 1인 가구는 40㎡ 이하만 가능하니, 결혼 후 가족이 늘어날 때 59㎡로 상향 지원하세요.</li>
                </ul>
            </div>
        </div>
        """
    elif "통합공공" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 통합공공임대: 30년 안심 거주 전략</h4>
            <b>특징:</b> 소득이 높아져도 쫓겨나지 않는 2026년 최신 제도입니다. 소득 수준에 따라 임대료가 계단식으로 변합니다.<br>
            <b>장점:</b> 최대 84㎡(34평형)까지 거주 가능하여 아이를 키우기에 최적입니다.<br>
            <div class='tip-box'>
                <b>💡 멘토의 비밀 꿀팁</b><br>
                다자녀, 맞벌이 부부 가산점이 큽니다. 신규 택지지구(검단, 계양 등) 공고를 노리세요. 입주 시점에 소득이 낮을수록 임대료 할인이 크니 초기 진입 시점을 잘 잡으세요.
            </div>
        </div>
        """
    elif "분양" in house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50;">🔎 공공분양 '뉴홈' 자가 소유 전략</h4>
            <b>장점:</b> 주변 시세의 70% 가격으로 온전한 내 집을 갖습니다. 수익 공유형(나눔형) 선택 시 초기 자금 부담이 훨씬 적습니다.<br>
            <b>대출:</b> 집값의 80%를 저금리(2%대)로 최대 40년 동안 나누어 갚을 수 있습니다.<br>
            <div class='action-box'>
                <b>📌 당첨 및 대출 방어 전략</b>
                <ul style="margin-top:10px;">
                    <li><b>청약 인정 총액:</b> 분양 당첨은 '총액' 싸움입니다. 매달 10만 원까지만 인정되니, 여유 생기면 즉시 월 10만 원으로 올리세요.</li>
                    <li><b>신용 관리:</b> 당첨되어도 신용등급 낮으면 대출 거절됩니다. <b>현금서비스, 리볼빙은 절대 금지</b>입니다!</li>
                </ul>
            </div>
        </div>
        """
    return report

# 4. 리포트 출력 
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)
    st.write(f"**대상자:** {user_name} 님 | **작성일:** 2026년 3월 6일")

    st.markdown('<div class="section-title">1. 현재 : 나의 출발선 진단</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) : 주거 기반 구축기</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) : 주거 안정 및 상향기</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) : 최종 자립 및 영구 안착</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5. 든든한 조력망 (필수 사이트 주소)</div>', unsafe_allow_html=True)
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
                이 로드맵을 보다가 어려운 말이 있거나 상황이 바뀌어 계획을 수정하고 싶다면<br>
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
            <p style="color: #7F8C8D; font-size: 13px; margin-top: 10px;">위 캐릭터를 누르면 리포트가 A4 용지 규격으로 자동 분할되어 출력(저장)됩니다.</p>
        </center>
        """,
        height=180
    )