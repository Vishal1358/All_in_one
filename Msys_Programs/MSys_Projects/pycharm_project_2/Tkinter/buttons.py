from tkinter import *

root=Tk()


def callback():
    label.config(text='You clicked me!',fg="red",bg="yellow")


label=Label(root,text="Hello Python")
label.pack()
button=Button(root,text='Click Here', command=callback)
button['state']='disabled'
button['state']='normal'
button.pack()

root.geometry("300x300")
root.mainloop()