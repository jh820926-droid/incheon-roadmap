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
    
    /* 카드 박스 디자인 */
    .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #EAECEE; margin-bottom: 20px; line-height: 1.8;}
    
    /* 내부 서브 박스 (실전 행동 지침 등 가독성 높이기용) */
    .action-box { background-color: #F8F9F9; padding: 18px; border-radius: 8px; margin-top: 15px; margin-bottom: 15px; border-left: 4px solid #3498DB;}
    
    /* 꿀팁 박스 디자인 */
    .tip-box { background-color: #FEF9E7; padding: 20px; border-radius: 8px; border-left: 5px solid #F1C40F; margin-top: 15px; color: #4D5656; font-size: 1rem; line-height: 1.7;}
    
    .step-list { margin-left: 10px; margin-bottom: 5px; margin-top: 5px; }
    
    /* 🖨️ PDF 전체 화면 인쇄를 위한 마법의 CSS */
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

# 3. 분석 알고리즘 (현재 진단 - 가독성 개선)
def analyze_current(assets, now_house, now_sub):
    report = ""
    # 청약 피드백
    if "아니요" in now_sub:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏦 청약 통장, 왜 지금 당장 만들어야 할까요?</h4>
            지금 청약 통장이 없거나 잠시 쉬고 계시군요! 청약 통장은 단순한 적금이 아니라, 나중에 LH 아파트나 내 집 마련을 할 때 꼭 필요한 <b>'무적의 입장권'</b>과 같답니다.<br>
            <div class='action-box'>
                <b>📌 당장 내일 해보면 좋은 일</b>
                <ul class='step-list'>
                    <li>신분증을 챙겨 은행에 가서 <b>'청년주택드림청약통장'</b>을 만들어 달라고 하세요. (일반 통장보다 이자가 훨씬 높아요!)</li>
                    <li>매월 2만 원씩이라도 자동이체를 걸어두세요. 당장 돈이 없어도 '납입 횟수'가 나중에 엄청난 가산점(최대 6점)이 된답니다.</li>
                </ul>
            </div>
        </div>
        """
    else:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏦 청약 통장 유지, 100점 만점에 200점이에요!</h4>
            연체 없이 꾸준히 납입하는 습관이 나중에 아파트에 들어갈 때 가장 강력한 무기(가산점)가 될 거예요. 정말 훌륭하게 잘하고 계세요!<br>
            <div class='action-box'>
                <b>📌 꼭 기억해야 할 실전 지침</b>
                <ul class='step-list'>
                    <li>혹시라도 급하게 목돈이 필요해져도 <b>절대 통장을 해지하지 마세요!</b></li>
                    <li>대신 은행에서 <b>'청약예금 담보대출'</b>을 받으세요. 통장 점수는 살려두고 내 돈의 90%까지 아주 싼 이자로 빌릴 수 있답니다.</li>
                </ul>
            </div>
        </div>
        """

    # 주거 피드백
    if "소년소녀가정" in now_house:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏠 현재 주거: 소년소녀가정 전세임대</h4>
            만 20세까지 전세 이자가 '전액 면제'되는 최고의 혜택을 받고 계시네요. 주거비 걱정 없이 온전히 나에게만 집중할 수 있는 소중한 시기랍니다.<br>
            <div class='tip-box'>
                <b>💡 멘토의 다정한 실전 꿀팁</b><br>
                만 22세 이후부터는 조금씩 임대료(이자)를 내야 해요. 주거비가 0원인 지금, 나중에 낼 이자나 독립 자금을 위해 매월 10만 원씩은 없는 돈이라 생각하고 꼭 저축해 두는 것을 추천해요! (도배나 장판이 낡았다면 LH 지원금 혜택도 꼭 챙기세요.)
            </div>
        </div>
        """
    elif "자립준비청년" in now_house:
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏠 현재 주거: 자립준비청년 임대주택</h4>
            보호 종료 후 5년 동안 임대료 50% 할인 혜택을 받으며 주거 안정을 이루셨군요! 아주 현명한 선택이에요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 다정한 실전 꿀팁 (전환보증금)</b><br>
                5년이 지나면 할인이 끝나서 월세가 오를 거예요. 이때를 대비해 LH의 <b>'전환보증금 제도'</b>를 꼭 활용해 보세요! 여유 자금({assets}만 원 등)을 보증금으로 추가 납부하면 연 6~7% 이율로 계산해서 매월 내는 월세를 치킨 한 마리 값으로 뚝 떨어뜨릴 수 있답니다!
            </div>
        </div>
        """
    elif "무상거주" in now_house:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏠 현재 주거: 무상거주 (시설/지인 등)</h4>
            고정적으로 나가는 집세(월세 등)가 없는 지금이 바로 <b>'종잣돈을 모을 수 있는 절대적인 골든타임'</b>이에요!<br>
            <div class='tip-box'>
                <b>💡 멘토의 다정한 실전 꿀팁</b><br>
                자립정착금 등 큰돈은 절대 기분 따라 쓰지 말고 '청년도약계좌'에 단단히 묶어두세요. 그리고 급하게 나갈 이유가 없다면, 여러분이 가진 <b>'자립준비청년 1순위 자격'</b>을 아껴두었다가 나중에 진짜 좋은 LH 임대주택이 나왔을 때 무기로 사용하세요!
            </div>
        </div>
        """
    elif "일반 민간 임대" in now_house:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏠 현재 주거: 일반 민간 임대 (월세/전세)</h4>
            훌륭하게 독립하셨지만, 매달 나가는 비싼 월세와 전세사기 위험은 자산을 모으는 데 큰 방해가 될 수 있어요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 다정한 실전 꿀팁</b><br>
                여러분에게는 일반 청년들보다 훨씬 적은 돈(보증금 100만 원 선)으로 좋은 집에 갈 수 있는 <b>'LH 자립준비청년 1순위 전형'</b>이라는 막강한 방패가 있어요! 아까운 내 돈이 월세로 사라지지 않도록, 담당자와 함께 LH 주택으로 이사 갈 방법을 지금 긍정적으로 검토해 보세요.
            </div>
        </div>
        """
    elif "주거취약계층" in now_house:
        report += """
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">🏠 현재 주거: 고시원 등 주거취약계층</h4>
            지금 지내는 곳이 많이 답답하시죠? 무엇보다 여러분의 일상에서는 '안전하고 따뜻한 잠자리'가 가장 중요해요.<br>
            <div class='tip-box'>
                <b>💡 멘토의 다정한 실전 꿀팁</b><br>
                혼자 버티지 마세요. <b>'주거취약계층 주거상향 지원사업'</b>을 통해 보증금, 이사비, 필수 가전제품까지 모두 지원받으며 쾌적한 공공임대주택으로 이사할 수 있어요! 이 글을 보셨다면 편하게 멘토에게 연락해서 꼭 도움을 받아보세요.
            </div>
        </div>
        """
    return report

# 4. 분석 알고리즘 (미래 로드맵 - 가독성 및 디자인 강화)
def generate_future(age, fam, house, sub_status=True):
    report = f"""
    <div class='card-box' style='background-color:#EBF5FB; border-left: 6px solid #2980B9;'>
        <b style='font-size:1.1rem;'>👨‍👩‍👧‍👦 목표 가구 구성:</b> {fam}<br>
        <b style='font-size:1.1rem;'>🏡 목표 주거 전형:</b> {house}
    </div>
    """
    
    if not sub_status:
        report += """
        <div class='action-box' style='border-left-color: #E74C3C;'>
            <b style='color:#C0392B;'>⚠️ 앗, 청약 납입을 잠시 쉬시려고요?</b><br>
            경제적으로 힘들 땐 멈출 수 있지만, 청약 통장의 생명력이 멈추면 나중에 아파트 경쟁에서 순위가 밀릴 수 있어요. 여유가 생기는 순간 꼭 월 2만 원씩이라도 다시 이어나가 보기를 다정하게 권유해 드려요!
        </div>
        """

    if "전세임대" in house:
        title = f"🔎 {age}세 맞춤 전세임대 공략법"
        desc = "내가 살고 싶은 동네의 맘에 드는 집을 직접 찾아오면, LH가 집주인과 대신 전세계약을 맺고 저렴하게 빌려주는 아주 자유로운 제도랍니다."
            
        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">{title}</h4>
            <p>{desc}</p>
            <div class='action-box'>
                <b>📌 이것만은 꼭 준비하세요!</b>
                <ul class='step-list'>
                    <li><b>공고 확인:</b> 주로 <b>1~2월 연초</b>에 모집이 쏟아지니 LH청약플러스를 꼭 확인하세요.</li>
                    <li><b>비용 준비:</b> 수도권 기준 약 1.2~1.5억을 지원해주니, 내 돈은 그 금액의 <b>5%</b>만 준비하면 돼요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 권리분석(안전한 집 찾기) 비밀 무기</b><br>
                부동산에 가서 이것저것 보지 말고 딱 이렇게 당당하게 말씀하세요!<br>
                <i>"사장님, 저 LH 전세임대 구하는데요, <b>부채비율 90% 이하로 권리분석 무조건 통과할 수 있는 깨끗한 집</b>만 보여주세요!"</i><br>
                (※ 집주인 빚과 내 보증금을 합친 돈이 집값의 90%를 넘으면 LH가 계약을 안 해줍니다.)
            </div>
        </div>
        """
        
    elif "매입임대" in house:
        title = f"🔎 {age}세 맞춤 매입임대 공략법"
        desc = "LH가 도심 곳곳의 튼튼한 빌라나 오피스텔을 통째로 사들여서 시세보다 훨씬 싸게 빌려주는 제도예요. 집주인이 '국가'라 전세사기 걱정이 0%랍니다!"

        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">{title}</h4>
            <p>{desc}</p>
            <div class='action-box'>
                <b>📌 이것만은 꼭 준비하세요!</b>
                <ul class='step-list'>
                    <li><b>공고 확인:</b> <b>3, 6, 9, 12월 분기별</b>로 정기 공고가 크게 올라와요.</li>
                    <li><b>초기 비용 절약:</b> 냉장고, 세탁기 등 풀옵션이 갖춰진 곳이 많아 이사 비용을 아끼기 좋아요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 '관심지역 알림'과 '줍줍' 비밀 무기</b><br>
                당첨자가 포기해서 남는 빈집 공고(수시모집)가 매주 금요일 오후에 조용히 올라옵니다.<br>
                👉 <b>스마트폰 'LH청약플러스' 앱 마이페이지에서 [관심지역 알림]을 '인천'으로 켜두세요!</b> 알람이 울리면 남들보다 빠르게 빈집을 낚아챌 수 있는 최고의 비법이에요.
            </div>
        </div>
        """
        
    elif "건설임대" in house:
        title = f"🔎 {age}세 맞춤 아파트(건설임대) 공략법"
        desc = "새로 지어지는 대단지 아파트에 입주할 기회예요. 경비실, 헬스장 등 생활 인프라가 훌륭하고 소득 요건만 유지하면 최장 30년까지 이사 안 가고 살 수 있어요."

        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">{title}</h4>
            <p>{desc}</p>
            <div class='action-box'>
                <b>📌 면적 제한 (매우 중요!)</b>
                <ul class='step-list'>
                    <li>1인 가구는 전용면적 <b>40㎡ 이하</b>만 지원할 수 있어요. 평수가 크다고 무작정 지원하면 서류에서 100% 탈락하니 꼭 {fam} 기준에 맞는 평수를 선택하세요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 '배점표' 만점받기 비밀 무기</b><br>
                치열한 아파트 경쟁에서 이기려면 딱 두 가지만 관리하세요!<br>
                1. <b>인천 연속 거주 기간:</b> 이사 갈 일이 없다면 전입신고는 타 지역으로 옮기지 마세요.<br>
                2. <b>청약 납입 횟수:</b> 통장에 돈이 많은 것보다 <b>'연체 없이 60회(5년) 이상 꾸준히 냈는지'</b>가 가장 중요해요!
            </div>
        </div>
        """
        
    elif "통합공공" in house:
        title = f"🔎 {age}세 맞춤 통합공공임대 공략법"
        desc = "2026년 최신 주거복지의 끝판왕 제도예요. 내 월급이 오르더라도 쫓겨나지 않고 소득에 맞춰 임대료만 내며 30년 동안 마음 편히 살 수 있어요."

        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">{title}</h4>
            <p>{desc}</p>
            <div class='action-box'>
                <b>📌 이것만은 꼭 준비하세요!</b>
                <ul class='step-list'>
                    <li><b>평형의 자유:</b> {fam}의 인원수에 맞춰 최대 84㎡(약 34평형) 아파트까지 당당하게 지원할 수 있어요.</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 신도시 청약 비밀 무기</b><br>
                검단신도시나 계양신도시 같은 쾌적한 새 동네에서 신규 아파트 공고가 쏟아질 거예요. 특히 맞벌이나 다자녀 가정이 될수록 가산점을 듬뿍 받으니, 마이홈포털에서 공고를 꾸준히 모니터링하는 걸 추천해요!
            </div>
        </div>
        """
        
    elif "분양" in house:
        title = f"🔎 {age}세 공공분양(뉴홈) 내 집 마련 공략법"
        desc = "로드맵의 멋진 종착지네요! 주변 아파트 시세의 70% 수준으로 새 아파트를 분양받아 나만의 온전한 집을 가질 수 있는 기회예요."

        report += f"""
        <div class='card-box'>
            <h4 style="color:#2C3E50; margin-top:0;">{title}</h4>
            <p>{desc}</p>
            <div class='action-box'>
                <b>📌 특별공급(특공) 필수 공략!</b>
                <ul class='step-list'>
                    <li>일반 경쟁은 너무 치열해요. 전체 물량의 70%를 차지하는 <b>'생애최초, 신혼부부, 다자녀 특공'</b>이라는 덜 막히는 문을 집중적으로 두드리세요!</li>
                </ul>
            </div>
            <div class='tip-box'>
                <b>💡 멘토의 DSR 신용관리와 대출 비밀 무기</b><br>
                1. <b>월 10만 원 납입:</b> 분양 당첨은 청약 통장에 <b>'월 최대 10만 원씩 누적된 총 금액'</b>으로 뽑아요. 여유가 생기면 무조건 납입금을 10만 원으로 올려두세요.<br>
                2. <b>신용점수 철통 방어:</b> 당첨 후 집값의 80%를 빌려주는 싼 대출(모기지)을 받으려면 신용점수가 필수예요. <b>잦은 현금서비스나 카드론</b>은 절대 금물입니다!
            </div>
        </div>
        """
    return report

# 5. 리포트 출력 및 PDF 버튼
if submit_btn:
    st.markdown('<div class="report-header">📑 나만을 위한 맞춤형 30년 주거 로드맵</div>', unsafe_allow_html=True)

    # 섹션 1 (현재)
    st.markdown(f'<div class="section-title">1. 현재 ({current_age}세) : 나의 출발선 튼튼하게 다지기</div>', unsafe_allow_html=True)
    st.markdown(analyze_current(assets, now_house, now_sub), unsafe_allow_html=True)
    
    # 섹션 2 (10년 후)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">2. 10년 후 ({current_age+10}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+10, fam_10, house_10, sub_10), unsafe_allow_html=True)

    # 섹션 3 (20년 후)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">3. 20년 후 ({current_age+20}세) 주거 계획 및 실전 꿀팁</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+20, fam_20, house_20, sub_20), unsafe_allow_html=True)

    # 섹션 4 (30년 후)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">4. 30년 후 ({current_age+30}세) 영구적인 주거 자립 달성</div>', unsafe_allow_html=True)
    st.markdown(generate_future(current_age+30, fam_30, house_30, sub_30), unsafe_allow_html=True)
    
    # 섹션 5 (도움망 및 연락처)
    st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">5. 든든한 주거복지 정보망 및 멘토의 편지</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class='card-box'>
        <b>1️⃣ LH 청약플러스 (<a href="https://apply.lh.or.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">바로가기👆</a>)</b><br>
        실제 집 공고를 보고 신청하는 곳! 스마트폰에 앱을 깔고 '관심지역 알림'을 꼭 켜두세요.<br><br>
        <b>2️⃣ 마이홈 포털 (<a href="https://www.myhome.go.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">바로가기👆</a>)</b><br>
        '자가진단' 메뉴를 누르면 내 나이와 소득에 딱 맞는 제도를 알아서 찾아줍니다.<br><br>
        <b>3️⃣ 자립정보ON (<a href="https://jaripon.ncrc.or.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">바로가기👆</a>)</b><br>
        자립준비청년들만을 위한 주거, 금융, 취업 정보가 가득한 전용 포털입니다.<br><br>
        <b>4️⃣ 주택도시기금 (<a href="https://nhuf.molit.go.kr/" target="_blank" style="color:#2980B9; text-decoration:none;">바로가기👆</a>)</b><br>
        이자가 아주 저렴한 나라의 대출 상품(버팀목, 디딤돌 등)을 알아볼 수 있는 공식 창구입니다.
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='card-box' style="background-color: #E8F8F5; border: 2px solid #1ABC9C; text-align: center;">
            <h3 style="color: #16A085; margin-bottom: 15px;">언제든 편하게 연락 주세요! 📞</h3>
            <p style="color: #34495E; font-size: 1.15rem; margin-bottom: 0px; line-height: 1.8;">
                사람마다 처한 상황이 다르고, 세워둔 계획은 살면서 언제든 변할 수 있어요.<br>
                이 로드맵을 보다가 어려운 말이 있거나, 내 상황에 맞게 계획을 조금 수정하고 싶다면 <b>절대 혼자 고민하지 마세요.</b><br>
                당신의 든든한 내 편이 되어 언제든 함께 길을 찾아 줄게요.
            </p>
            <hr style="border: 1px dashed #1ABC9C; width: 60%; margin: 25px auto;">
            <div style="font-size: 1.3rem; font-weight: bold; color: #2C3E50;">
                👤 담당 김정현(070-7663-1153)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 귀여운 캐릭터 PDF 인쇄 버튼
    st.markdown("---")
    components.html(
        """
        <center>
            <a href="#" onclick="window.parent.print(); return false;" title="눌러서 리포트를 저장하세요!">
                <img src="https://media.giphy.com/media/ic06p9J076137681I3/giphy.gif" width="100px" style="border-radius:50%; box-shadow:0 4px 6px rgba(0,0,0,0.1); cursor:pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            </a>
        </center>
        """,
        height=150
    )