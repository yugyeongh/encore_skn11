import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

# 1번 메뉴를 여러분의 점심 메뉴로 메뉴명과 가격을 수정
cursor = connection.cursor()
sql = "update tbl_menu set menu_name=%s, menu_price=%s where menu_code=%s"
values = ('구내식당', 7500, 1)

cursor.execute(sql, values)

print(f'{cursor.rowcount}개의 행을 수정하였습니다.')

connection.commit()

cursor.close()
connection.close()