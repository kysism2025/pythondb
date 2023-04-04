from tkinter import *
from tkinter import messagebox

win = Tk()

def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    win.quit()
    win.destroy()    


mainMenu = Menu(win)
win.config(menu=mainMenu)

fileMenu1=Menu(mainMenu,  tearoff=0, selectcolor="red")
fileMenu1.add_command(label="열기", command=func_open)
mainMenu.add_separator()
fileMenu1.add_command(label="종료", command=func_exit)
mainMenu.add_cascade(label="파일", menu=fileMenu1)

win.mainloop()    