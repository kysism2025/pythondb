from tkinter import *
from tkinter.simpledialog import *

win = Tk()

win.geometry("400x100")
label1 = Label(win, text="입력된 값")
# label1.pack(side=LEFT)
label1.grid(row=0, column=1)

# txt1 = Entry(win)
# # txt1.pack(side=RIGHT)
# txt1.grid(row=0, column=2)


val = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)
label1.configure(text=str(val))

win.mainloop()