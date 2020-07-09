import tkinter as tk
from googletrans import Translator

win=tk.Tk()
win.title("Translator")



def translate():
    word=entry.get()
    translator=Translator(service_urls=['translate.google.com'])
    translation=translator.translate(word,dest="fr")
    label1=tk.Label(win,text=f"Translated to French :{translation.text}",bg="yellow")
    label1.grid(row=2,column=0)

label=tk.Label(win,text="Enter word:")
label.grid(row=0,column=0,sticky="w")

entry=tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="translate",command=translate)
button.grid(row=1,column=2)

win.mainloop()