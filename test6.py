from tkinter import *

win = Tk()

mainMenu = Menu(win)
win.config(menu=mainMenu)


fileMenu1=Menu(mainMenu,  tearoff=0, selectcolor="red")
fileMenu1.add_command(label="열기")
mainMenu.add_separator()
fileMenu1.add_command(label="종료")
mainMenu.add_cascade(label="파일", menu=fileMenu1)

fileMenu12=Menu(fileMenu1,  tearoff=0, selectcolor="green")
fileMenu12.add_command(label="메뉴2-1")
mainMenu.add_separator()
fileMenu12.add_command(label="메뉴2-2")
fileMenu1.add_cascade(label="상위 메뉴 2", menu=fileMenu12)

win.mainloop()    