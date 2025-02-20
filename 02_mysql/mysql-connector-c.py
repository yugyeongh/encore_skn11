import mysql.connector

connection = mysql.connector.connect( # connection 객체
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor()

sql = "insert into tbl_menu(menu_name, menu_price, category_code, orderable_status) values (%s, %s, %s, %s)"  # %s는 placeholder 
values = ('쌀국수', 12000, 4, 'Y')

cursor.execute(sql, values)

print(f'{cursor.rowcount}개의 행을 삽입하였습니다.')
# transaction 처리 때문에 한 개의 행이 삽입되었다고 떴음에도 실제로 값이 저장되진 않음
# insert 명령을 수행하긴 했는데 cursor와 connection을 close함 -> 중간에 작업이 중지가 된 것 -> 즉, 데이터베이스스에 반영하지 않고 cursor와 connection이 끊어짐
# 그래서 cud 작업을 한 후에는 작업 commit을 꼭 해야 반영이 됨
# auto--increment로 인해 메뉴코드의 121,122차례가 실행이 됨 근데 commit을 안해서 db에는 반영이 안 됨 그래도 121,122를 비워놓고 메뉴코드를 만듦

connection.commit()

cursor.close()
connection.close()