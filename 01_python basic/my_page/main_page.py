import streamlit as st
from scraping_data import baseball_data

st.header('2024 KBO 순위⚾️')
st.divider()
st.radio('연령대를 선택하세요', ['20대','30대','40대','50대','60대 이상'])
st.write(baseball_data())