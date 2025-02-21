from dotenv import load_dotenv
import os 
import urllib.request

load_dotenv()

# API 호출을 위한 변수 설정정
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

encText = urllib.parse.quote('오늘 점심') # url에서 사용할 수 없는 한글 혹은 특수 문자를 인코딩하는 함수

# ###### json #######
# url_json = 'https://openapi.naver.com/v1/search/news.json' + '?query=' + encText

# request = urllib.request.Request(url_json) # 요청으로 만들기 위해 객체 생성 # 대문자로 시작하면 보통 클래스인 경우임
# request.add_header('X-Naver-Client-ID', client_id) # 요청 헤더로, 요청에 대한 정보를 기본적으로 가짐
# request.add_header('X-Naver-Client-Secret', client_secret)

# response = urllib.request.urlopen(request) # 요청에 대한 응답 

# print(response.getcode())

# response_body = response.read()
# f = open('./naver-news-api.json','w', encoding='utf-8')
# f.write(response_body.decode('utf-8'))
# f.close()


###### xml #######
# 요청 url
url_xml = 'https://openapi.naver.com/v1/search/news.xml' + '?query=' + encText

request = urllib.request.Request(url_xml) # 요청으로 만들기 위해 객체 생성 # 대문자로 시작하면 보통 클래스인 경우임
request.add_header('X-Naver-Client-ID', client_id) # 요청 헤더로, 요청에 대한 정보를 기본적으로 가짐
request.add_header('X-Naver-Client-Secret', client_secret)

response = urllib.request.urlopen(request) # 요청에 대한 응답 

print(response.getcode()) # 응답 코드 변환

response_body = response.read() # read():응답 내용 반환
f = open('./naver-news-api.xml','w', encoding='utf-8')
f.write(response_body.decode('utf-8'))
f.close()

