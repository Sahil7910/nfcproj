import tkinter as tk

from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from sqlalchemy import engine, and_
from sqlalchemy.orm import sessionmaker
from DataBase import *
from tap import TapUser


class Login:
    def __init__(self, rt):

        self.root = rt
        self.root.title('Login')
        self.root.geometry("600x300")



        self.name = StringVar()
        self.password = StringVar()


        name_label = Label(self.root, text="username:", font=('calibre', 10, 'bold')).place(x=200, y=50)

        name_entry = Entry(self.root, textvariable=self.name, font=('calibre', 10, 'bold')).place(x=280, y=50)

        pass_label = Label(self.root, text="password:", font=('calibre', 10, 'bold')).place(x=205, y=80)

        pass_entry = Entry(self.root,show='*', textvariable=self.password, font=('calibre', 10, 'bold')).place(x=280, y=80)

        check = Checkbutton(self.root, text='show password',command=self.show).place(x=280, y=100)
        sub_btn = Button(self.root, text='Submit', command=self.submit).place(x=320, y=140)

    def show(self):

        if self.root.pass_entry.cget('show') == '*':
            self.root.pass_entry.config(show='')
        else:
            self.root.pass_entry.config(show='*')

    def submit(self):

        userid= self.name.get()
        password=self.password.get()

        # print("userid is: "+ userid)
        # print("password is: "+ password)

        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Users).filter(and_(Users.name == userid, Users.password == password))
        for row in result:

                if userid == row.name and password == row.password:
                    tap = TapUser(tk.Tk())
                    self.root.withdraw()
                    break
        else:
                messagebox.showerror("Login Failed", "Invalid username or password")






