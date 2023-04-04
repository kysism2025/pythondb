from tkinter import *
from tkinter import messagebox

def clickButton():
    name = txt.get()
    messagebox.showinfo("이름", name, anchor=NW)

win = Tk()

win.geometry("200x200")


lbl = Label(win, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(win)
txt.grid(row=0, column=1)

button1 = Button(win, text="press here", fg="red", bg="yellow", command=clickButton)
button1.grid(row=1, column=1)

win.mainloop()