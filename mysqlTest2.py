import pymysql

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = pymysql.connect(
                        host='localhost', \
                        port=3307, \
                        user='root', \
                        password='test1234', \
                        db='madang',  \
                        charset='utf8') # 한글처리 (charset = 'utf8')
 
cur = con.cursor()
 
while True:
    data1 = input("사용자 ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 주소 ==> ")
    data4 = input("사용자 전화번호 ==> ")

    sql = "insert into customer values(%s, %s, %s, %s)"
    cur.execute(sql, (data1, data2, data3, data4))
    
 
# rows = cur.fetchall()
# print(rows)     # 전체 rows

con.commit()
con.close()