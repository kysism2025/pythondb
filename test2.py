from tkinter import *

win = Tk()
# win.title('윈도우 창 연습')
# win.geometry("400x100")
# win.resizable(width=False, height=False)

label1 = Label(win, text="This is Mysql을")
label2 = Label(win, text="열심히", font=("궁서체, 30"), fg="blue")
label3 = Label(win, text="공부중입니다.", bg="magenta", width="20", height=5)

label1.pack()
label2.pack()
label3.pack()

win.mainloop()



