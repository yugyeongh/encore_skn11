import streamlit as st
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=pitcher&playerOrder=era'
response = requests.get(url)
response.raise_for_status()

html = response.text
soup = bs(html, 'html.parser')
table = soup.find_all("table")[0]

# thead의 tr 추출을 통해 df의 columns 생성
header = soup.find_all("thead")[0]
headers = [th.get_text(strip=True) for th in header.find_all("span", class_="blind")]
# st.write(headers)

body = soup.find_all("tbody")[0]
rows = body.find_all('tr')

data = []
for row in rows:
    cells = row.find_all(['th', 'td'])
    row_data = []
    for cell in cells:
        row_data.append(cell.text.strip())
    data.append(row_data)

df = pd.DataFrame(data, columns=headers)
df.set_index('순위', inplace=True)


st.header('2024 KBO 순위⚾️')
st.divider()
st.write(df)