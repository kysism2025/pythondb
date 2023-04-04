from tkinter import *

win = Tk()
win.geometry("200x200")

upFrame = Frame(win)
upFrame.pack()
downFrame = Frame(win)
downFrame.pack()

editBox = Entry(upFrame,width=10,bg='green')
editBox.pack(padx=20, pady=20)

listbox = Listbox(downFrame, bg='yellow')
listbox.insert(0, "하나")
listbox.insert(1, "둘")
listbox.insert(2, "셋")
listbox.pack()

win.mainloop()  