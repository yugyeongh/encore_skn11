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
# st.write(body)

data = []

for b in body.find_all("tr"):
    rank = body.find('th').text.strip()
    team = body.find('span', id=lambda x: x and x.startswith('team_')).text.strip()

    for td in soup.find_all('td')[1:]:  # 첫 번째 td는 팀 이름이므로 제외
        value = td.text.strip()
        result.append(value)

rows = [th.get_text(strip=True) for th in body.find_all("td")]
# rows = soup.find_all("tr")[1:] # 첫 번째 tr
st.write(rows)

data = []
row_data = []
rank = 1
for row in rows:
    if row != '': 
        row_data.append(row)
    else:
        if row_data != []:
            data.append(row_data)
            row_data = []
        row_data.append(rank)
        rank += 1
st.write(data)
print(len(headers))
print(len(data))
df = pd.DataFrame(data)
st.write(df)
st.write(headers)
# df = pd.DataFrame(data, columns=headers)

# st.write(df)


st.header('2024 KBO 순위⚾️')
st.divider()
st.write(table)