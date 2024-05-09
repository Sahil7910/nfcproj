import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

text = tk.StringVar()
name='sahil'
text.set(name)
textBox = tk.Entry(root, textvariable=text).place(x=10,y=5)



root.mainloop()