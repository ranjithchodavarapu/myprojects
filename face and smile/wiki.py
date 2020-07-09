import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win=Tk()
win.title("Wikipedia")

def search():
    search=entry.get()
    answer=wikipedia.summary(search)
    showinfo("wikipedia Answer",answer)

label=Label(win,text="wikipedia search:")
label.grid(row=0,column=0)

entry=Entry(win)
entry.grid(row=1,column=0)

button=Button(win,text="translate",command=search)
button.grid(row=1,column=2)

win.mainloop()
