import tkinter as tk
from tkinter import *


class TopUp():
    def __init__(self, rt):
        self.root = rt
        self.root.title('Top Up')
        self.root.geometry("500x300")

        amount_lable = Label(self.root, text="Amount:", font=('calibre', 13, 'bold')).place(x=135, y=50)
        amount_entry = Entry(self.root, font=('calibre', 13, 'bold')).place(x=210, y=50)

        password_lable = Label(self.root, text="Password:", font=('calibre', 13, 'bold')).place(x=118, y=80)
        password_entry = Entry(self.root, font=('calibre', 13, 'bold')).place(x=210, y=80)

        ok_btn = Button(self.root, text='OK', font=('calibre', 13, 'bold')).place(x=350, y=120)