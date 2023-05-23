from tkinter import *

root=Tk()
label=Label(root,text="Helo Python")
label.config(text="Helo Tkinter", fg='red')
label.config(bg='yellow')
label.config(font='Times 15')
label.config(text="Hellow Python i love you so much!")
label.config(wraplength='150')
label.config(justify=RIGHT)
label.pack()
root.geometry("300x250")
root.mainloop()
