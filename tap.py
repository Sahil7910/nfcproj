import tkinter as tk
from tkinter import *

from addmember import AddMember
from admin import Admin
from checkout import CheckOut


class TapUser():
    def __init__(self, rt):
        self.root = rt
        self.root.title('tap')
        self.root.geometry("600x300")

        link = Button(self.root, text="Admin",command=self.admin,font=('calibre', 10, 'bold')).place(x=450, y=50)


        read_card_btn = Button(self.root, text='Read Card', command=self.submit, height=4, width=20,font=('calibre', 10, 'bold')).place(x=250, y=120)



    def submit(self):

        self.root.withdraw()

        checkout= CheckOut(tk.Tk())

    def admin(self):

        self.root.withdraw()

        admin= Admin(tk.Tk())