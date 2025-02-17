import streamlit as st

st.title('2025년 2월 17일')
st.divider()
st.header('오늘은 streamlit 배우는 날')
st.subheader('streamlit으로 만들어 보는 내 사이트!')
st.code('''
        a = 1234
        b = 1
        print(a+b)
        ''')

my_site = st.text_input('내가 만들고 싶은 사이트는?')
st.write(my_site)

if st.button(f'{my_site} 접속하기'):
    st.success(f'{my_site}(으)로 접속 중🚀', icon='✅')

activated = st.toggle("Activate")

st.feedback("stars")