from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

s = ttk.Style()
s.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2", "c3"), show='headings', height=3)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Date")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="CardID")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Amount")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('08-05-2024', '1234', '5000'))
tree.insert('', 'end', text="2", values=('07-05-2024', '4567', '2000'))

tree.pack()

win.mainloop()