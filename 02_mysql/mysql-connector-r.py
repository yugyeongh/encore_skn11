import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor() # cursor 객체를 통해 쿼리가 동작하고, 이 조회 결과를 가져와야함
cursor.execute("select menu_code, menu_name, menu_price from tbl_menu")
result = cursor.fetchall() # 결과를 조회해와서 result로 받음

# print(result) # 리스트의 형태로 가져오고, 각 row는 튜플로 가져옴

for row in result: # row = 한 행의 결과
    print('menucode: ', row[0], '/', 'menucode: ',row[1], '/', 'menuprice: ', row[2])

cursor.close()
connection.close()