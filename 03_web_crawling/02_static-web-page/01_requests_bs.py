# 정적 페이지 웹 스크래핑 -> requests, beautifulsoup
# 정적 페이지: 요청한 url에서 응답받은 html을 그대로 사용한 경우 (Server Side Rendering)

import requests
from bs4 import BeautifulSoup

def web_request(url):
    response = requests.get(url) # <Response [200]>
    print(response)
    print('--------------1--------------')
    print(response.status_code) #200 (응답코드)
    print('--------------2--------------')
    print(response.text) #html을 그대로 받아줌줌
    return response

# url = 'https://www.naver.com'
# response = web_request(url)

with open('../html-sample.html', 'r', encoding='utf-8') as f: # 경로, 모드, 인코딩
    html = f.read()

bs = BeautifulSoup(html, 'html.parser') # html.parser: 파이썬 내장 파서서
# print(bs)
# print(type(bs))

def test_find():
    print('-----------tag-----------')
    #find -- 작성한 태그 하나만 가져오는데 가장 먼저 오는는 태그로 가져옴옴
    tag = bs.find('li') #dictionary로 조회
    print(tag)
    print(type(tag))

    print('-----------tags-----------')
    #find_all
    tags = bs.find_all('section',{'id': 'section1'})
    print(tags)
    print(type(tags))

test_find()