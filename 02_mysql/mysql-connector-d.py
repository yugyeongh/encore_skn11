import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

# menucode가 100번 이상인 메뉴 삭제하기
cursor = connection.cursor()

sql = "delete from tbl_menu where menu_code >= 100"
# value = (100,) # 요소가 하나일때는 꼬옥 ,를 붙여줘야함 그래야 튜플로 인식함

cursor.execute(sql)
# print(f'{cursor.rowcount}개의 행을 삭제제하였습니다.')

connection.commit()

cursor.close()
connection.close()