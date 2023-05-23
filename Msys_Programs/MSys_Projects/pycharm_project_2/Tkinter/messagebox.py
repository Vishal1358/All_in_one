from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
def callback():
    mbox= messagebox.askquestion("Delete","Are You Sure", icon='warning')
    if mbox=='yes':
        print("Deleted")
    else:
        print("Not Deleted")
def callback2():
    messagebox.showinfo("Success","Well Done")
    print("You Clicked OK!")
button1= ttk.Button(root, text="Delete",command=callback).grid(row=0, column=0,pady=25,padx=50)
button2= ttk.Button(root, text="Info",command=callback2).grid(row=0, column=1)

root.geometry("350x250")
root.mainloop()