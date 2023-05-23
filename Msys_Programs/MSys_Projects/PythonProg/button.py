import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def say_hi():
    print("HELLO!")

button = tk.Button(frame,text="CLICK ME",fg="red",command=say_hi)


button.pack(side=tk.LEFT)
root.mainloop()
