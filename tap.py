import tkinter as tk
from tkinter import *
from tkinter import messagebox

from sqlalchemy import engine, and_
from sqlalchemy.orm import sessionmaker
from DataBase import *
from addmember import AddMember
from admin import Admin
from checkout import CheckOut
from main import *


class TapUser():
    def __init__(self, rt):
        self.root = rt
        self.root.title('tap')
        self.root.geometry("600x300")

        link = Button(self.root, text="Admin",command=self.admin,font=('calibre', 10, 'bold')).place(x=450, y=50)


        read_card_btn = Button(self.root, text='Read Card', command=self.submit, height=4, width=20,font=('calibre', 10, 'bold')).place(x=250, y=120)



    def submit(self):
        cardid = uid()
        self.root.withdraw()
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for check whether card is present or not:
        result = session.query(Members).filter(and_(Members.cardid == cardid, Members.status == 1))
        for row in result:
            if row is not None:
                checkout= CheckOut(tk.Tk())
                break
        else:
                messagebox.showerror("error","Card Id Not Found!!!")



    def admin(self):

        self.root.withdraw()

        admin= Admin(tk.Tk())