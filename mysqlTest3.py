import pymysql
from tkinter import *
from tkinter import messagebox

win, con, cur = None, None, None
strData1,strData2,strData3,strData4 = [],[],[],[]
sql = ""

def closeWin():
     print('윈도우를 종료하였습니다.')
     win.quit()

def conn_db():
    con = pymysql.connect(
                            host='localhost', \
                            port=3307, \
                            user='root', \
                            password='test1234', \
                            db='madang',  \
                            charset='utf8') # 한글처리 (charset = 'utf8')
    return con
    
def disconn_db(con):
    con.close()

def selectData():

    con = conn_db()
    cur = con.cursor()
    cur.execute("select * from customer") 

    listbox1.delete(0, END)
    listbox2.delete(0, END)
    listbox3.delete(0, END)
    listbox4.delete(0, END)

    listbox1.insert(END, "사용자ID")
    listbox2.insert(END, "사용자이름")
    listbox3.insert(END, "주소")
    listbox4.insert(END, "전화번호")
    listbox1.insert(END, "---------------------")
    listbox2.insert(END, "---------------------")
    listbox3.insert(END, "---------------------")
    listbox4.insert(END, "---------------------")

    while True:
        row = cur.fetchone()

        if row == None:
            break
        else:
            listbox1.insert(END, row[0])
            listbox2.insert(END, row[1])
            listbox3.insert(END, row[2])
            listbox4.insert(END, row[3])

    disconn_db(con)

def insertData():
        
        try:
            con = conn_db()
            cur = con.cursor()
            sql = "insert into customer values(%s, %s, %s, %s)"
            cur.execute(sql, (edit1.get(), edit2.get(), edit3.get(), edit4.get()))
            con.commit()
            disconn_db(con)

        except Exception as e:
             messagebox.showinfo("ERROR", e)
             
        else:
             messagebox.showinfo("INFO", "성공적으로 데이터를 저장하였습니다")


# con = pymysql.connect(
#                         host='localhost', \
#                         port=3307, \
#                         user='root', \
#                         password='test1234', \
#                         db='madang',  \
#                         charset='utf8') # 한글처리 (charset = 'utf8')
 
# cur = con.cursor()
# cur.execute("select * from customer") 

# print('사용자ID    사용자이름     이메일       출생연도')
# print('------------------------------------------------')

# while True:
#     row = cur.fetchone()

#     if row == None:
#         break
#     else:
#         # print (f"{row[0]}  {row[1]}  {row[2]}  {row[3]}")
#         print("%d  %15s  %12s  %15s" %(row[0],row[1],row[2],row[3]))


# for i in range(0,len(strData1)):
#     print("%s  %15s  %12s  %15s" %(strData1[i],strData2[i],strData3[i],strData4[i]))

win = Tk()
win.protocol("WM_DELETE_WINDOW", closeWin)
win.geometry("600x300")
win.title("GUI 데이터 입력")

edtFrame = Frame(win)
edtFrame.pack()
listFrame = Frame(win)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edit1 = Entry(edtFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(edtFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(edtFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(edtFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

listbox1 = Listbox(listFrame, bg='yellow')
listbox1.pack(side=LEFT) #, fill=BOTH, expand=1)
listbox2 = Listbox(listFrame, bg='yellow')
listbox2.pack(side=LEFT) #, fill=BOTH, expand=1)
listbox3 = Listbox(listFrame, bg='yellow')
listbox3.pack(side=LEFT) #, fill=BOTH, expand=1)
listbox4 = Listbox(listFrame, bg='yellow')
listbox4.pack(side=LEFT) #, fill=BOTH, expand=1)

btnInsert = Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT,padx=10,pady=10)

btnSelect = Button(edtFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT,padx=10,pady=10)

win.mainloop()

