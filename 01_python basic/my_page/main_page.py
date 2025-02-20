import streamlit as st
from scraping_data import baseball_data

st.header('2024 KBO 순위⚾️')
st.divider()
st.write(baseball_data())