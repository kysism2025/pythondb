import pymysql

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

def conn_db():
    con = pymysql.connect(
                            host='localhost', \
                            port=3307, \
                            user='root', \
                            password='test1234', \
                            db='madang',  \
                            charset='utf8') # 한글처리 (charset = 'utf8')
    
def disconn_db():
    con.close()

def insert_data():
    while True:
        data1 = input("사용자 ID ==> ")
        if data1 == "":
            break
        data2 = input("사용자 이름 ==> ")
        data3 = input("사용자 주소 ==> ")
        data4 = input("사용자 전화번호 ==> ")

        cur = con.cursor()
        sql = "insert into customer values(%s, %s, %s, %s)"
        cur.execute(sql, (data1, data2, data3, data4))

def update_data(data1, data2, data3, data4):
        cur = con.cursor()
        sql = "update customer "
        if data2 != "":
            sql = sql + " set name='" + data2 + "'"
        elif data3 != "":
            sql = sql + " set address='" + data3 + "'"
        elif data4 != "":
            sql = sql + " set phone='" + data4 + "'"

        sql = sql + " where custid=" + data1
        cur.execute(sql)

def delete_data(data1):
        cur = con.cursor()
        sql = "delete from customer "
        sql = sql + "where custid=" + data1
        cur.execute(sql)   
    
def select_data():
    cur = con.cursor()
    cur.execute("select * from customer") 

    print('사용자ID    사용자이름     이메일       출생연도')
    print('------------------------------------------------')

    while True:
        row = cur.fetchone()

        if row == None:
            break
        else:
            # print (f"{row[0]}  {row[1]}  {row[2]}  {row[3]}")
            print("%d  %15s  %12s  %15s" %(row[0],row[1],row[2],row[3]))






