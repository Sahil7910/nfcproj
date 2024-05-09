import tkinter as tk
from tkinter import *

from tap import TapUser


class Login:
    def __init__(self, rt):

        self.root = rt
        self.root.title('Login')
        self.root.geometry("600x300")

        # menubar = Menu(root)
        #
        # file = Menu(menubar, tearoff=0)
        # menubar.add_cascade(label='File', menu=file)
        # file.add_command(label='New File', command=None)
        # file.add_command(label='Open...', command=None)
        # file.add_command(label='Save', command=None)
        # file.add_separator()
        # file.add_command(label='Exit', command=root.destroy)

        # edit = Menu(menubar, tearoff=1)
        # menubar.add_cascade(label='Edit', menu=edit)
        # edit.add_command(label='cut')

        self.name = StringVar()
        self.password = StringVar()

        name_label = Label(self.root, text="username:", font=('calibre', 10, 'bold')).place(x=200, y=50)

        name_entry = Entry(self.root, textvariable=self.name, font=('calibre', 10, 'bold')).place(x=280, y=50)

        pass_label = Label(self.root, text="password:", font=('calibre', 10, 'bold')).place(x=205, y=80)

        pass_entry = Entry(self.root, textvariable=self.password, font=('calibre', 10, 'bold')).place(x=280, y=80)

        sub_btn = Button(self.root, text='Submit', command=self.submit).place(x=320, y=120)





    def submit(self):

        userid= self.name.get()
        password=self.password.get()

        print("userid is: "+ userid)
        print("password is: "+ password)

        self.root.withdraw()


        tap = TapUser(tk.Tk())

