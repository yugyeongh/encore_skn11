import json
from dotenv import load_dotenv
import os 
import urllib.request
import mysql.connector

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

searchText = urllib.parse.quote('소나기')

url = 'https://openapi.naver.com/v1/search/book.json' + '?query=' + searchText + '&display=100'
request = urllib.request.Request(url)
request.add_header('X-Naver-CLient-ID', client_id)
request.add_header('X-Naver-CLient-Secret', client_secret)

response = urllib.request.urlopen(request)
response_body = response.read()
response_body = json.loads(response_body) #loads는 read해서 byte로 가져온 응답은 dictionary 형태로 변환해줌

# print(response_body)

book_list = response_body['items']

connection = mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='bookdb'
)

cursor = connection.cursor()

sql = 'insert into naver_book(book_title, book_image, author, publisher, isbn, book_description, pub_date) values (%s,%s,%s,%s,%s,%s,%s)'

for book_info in book_list:
    values = (book_info['title'], book_info['image'], book_info['author'], book_info['publisher'], str(book_info['isbn']), book_info['description'], book_info['pubdate'])
    cursor.execute(sql, values)

connection.commit() 

cursor.close()
connection.close()