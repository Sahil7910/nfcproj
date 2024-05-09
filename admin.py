import tkinter as tk
from tkinter import *

from addmember import AddMember
from blockcard import BlockCard


class Admin():
    def __init__(self, rt):
        self.root = rt
        self.root.title('Admin')
        self.root.geometry("500x300")



        Add_member_btn = Button(self.root, text='Add Member', command=self.addmember, height=2, width=20,font=('calibre', 10, 'bold')).place(x=169, y=100)
        Block_card_btn=  Button(self.root, text='Block Card', command=self.block ,height=2, width=20,font=('calibre', 10, 'bold')).place(x=169, y=180)


    def addmember(self):

        self.root.withdraw()

        addmember=AddMember(tk.Tk())

    def block(self):
        self.root.withdraw()
        blockcard = BlockCard(tk.Tk())