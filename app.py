import streamlit as st

# 1. 앱 기본 설정
st.set_page_config(page_title="인천자립 주거로드맵", page_icon="🏠", layout="centered")

# CSS 스타일링 (보고서 가독성 극대화)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #2C3E50; font-weight: bold; text-align: center; margin-bottom: 0px;}
    .sub-title { font-size: 1.1rem; color: #7F8C8D; text-align: center; margin-bottom: 20px;}
    .report-title { font-size: 1.8rem; color: #1A5276; font-weight: bold; border-bottom: 3px solid #1A5276; padding-bottom: 10px; margin-top: 40px;}
    .section-header { font-size: 1.4rem; color: #2E86C1; font-weight: bold; margin-top: 30px; margin-bottom: 10px;}
    .report-box { background-color: #F8F9F9; padding: 20px; border-radius: 8px; border: 1px solid #D5D8DC; margin-bottom: 15px;}
    .highlight-blue { background-color: #EBF5FB; padding: 15px; border-left: 5px solid #3498DB; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
    .highlight-red { background-color: #FDEDEC; padding: 15px; border-left: 5px solid #E74C3C; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
    </style>
""",