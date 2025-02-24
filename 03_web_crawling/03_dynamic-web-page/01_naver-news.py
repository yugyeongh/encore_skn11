# 동적 페이지 웹 스크래핑 <- selenium
# 동적 페이지: 요청한 url에서 응답받은 html 안의 js를 실행해 html을 새로 만든 경우 (Client Side Rendering)

# Selenium
# - 인증을 요구하는 특정 웹 페이지의 데이터 스크랩
# - 무한 댓글 스크랩
# - 브라우저용 매크로로써 사용 가능

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 입력과 관련된 라이브러리
from selenium.webdriver.common.by import By # 요소를 선택하기 위해 사용되는 라이브러리로 조회 방식을 지정함
import time

# 1. 크롬 실행
path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

# 2. 특정 url 접근
# driver.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=삿포로+여행')
driver.get('https://naver.com')
time.sleep(1)

# 3. 검색 처리
search_box = driver.find_element(By.ID, 'query') # input 박스 요소에 접근
search_box.send_keys('한화 이글스')
search_box.send_keys(Keys.RETURN)

# #lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a
# //*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a -> xpath는 selenium에서 원하는 요소를 찾는 역할을 함

# 뉴스 탭 이동동
news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
news_btn.click()
time.sleep(1)


# 4. 스크롤 처리
for _ in range(5): # 1초씩 쉬어가면서 5번 스크롤롤
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    time.sleep(1) # 1초 쉬는 코드를 작성하지 않으면 제대로 코드가 작동 안 할 수 있음

# 5. 특정 요소에 접근
news_contents_elems = driver.find_elements(By.CSS_SELECTOR, '.news_contents')
print(len(news_contents_elems))

for news_contents_elem in news_contents_elems:
    # print(news_contents_elem)
    # print(type(news_contents_elems))
    a_tag = news_contents_elem.find_element(By.CSS_SELECTOR, 'a.news_tit')
    title = a_tag.text
    href = a_tag.get_attribute('href')
    print(title, '|', href)

driver.quit()


