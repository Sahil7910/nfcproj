import tkinter as tk
from tkinter import *

from checkout import CheckOut


class AddMember():
    def __init__(self, rt):
        self.root = rt
        self.root.title('Add Member')
        self.root.geometry("500x300")

        name_label = Label(self.root, text="Name:", font=('calibre', 13, 'bold')).place(x=135, y=50)
        name_entry = Entry(self.root, font=('calibre', 13, 'bold')).place(x=190, y=50)

        mobile_label = Label(self.root, text="Mobile:", font=('calibre', 13, 'bold')).place(x=130, y=90)
        mobile_entry = Entry(self.root, font=('calibre', 13, 'bold')).place(x=190, y=90)

        card_label = Label(self.root, text="CardID:", font=('calibre', 13, 'bold')).place(x=125, y=129)
        card_entry = Entry(self.root, state=DISABLED, font=('calibre', 13, 'bold')).place(x=190, y=129)

        tap_btn = Button(self.root, text='Tap Card',font=('calibre', 12, 'bold')).place(x=169, y=170)

        ok_btn=  Button(self.root, text='ok', command=self.submit, font=('calibre', 12, 'bold')).place(x=290, y=170)


    def submit(self):

        self.root.withdraw()

        checkout= CheckOut(tk.Tk())