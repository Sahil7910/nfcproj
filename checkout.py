import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from blockcard import BlockCard
from tkinter import messagebox

from sqlalchemy import engine, and_
from sqlalchemy.orm import sessionmaker
from DataBase import *
from topup import TopUp
from main import *


class CheckOut():
    def __init__(self,rt):
        self.root=rt
        self.root.title('CheckOut')
        self.root.geometry("500x500")

        cname=name()
        mobileno=mobile()
        amount=Balance()
        cardid=uid()


        self.cname = tk.StringVar()
        self.mobile = tk.StringVar()
        self.amount = tk.StringVar()
        self.cardid = tk.StringVar()

        self.amount2= StringVar()

        self.cname.set(cname)
        self.mobile.set(mobileno)
        self.amount.set(amount)
        self.cardid.set(cardid)
        date= datetime.date.today()


        card_label = Label(self.root, text="Card:", font=('calibre', 13, 'bold')).place(x=135, y=50)
        card_entry = Entry(self.root,  state=DISABLED ,textvariable = self.cardid, font=('calibre', 13, 'bold')).place(x=190, y=50)

        name_label = Label(self.root, text="Name:", font=('calibre', 13, 'bold')).place(x=130, y=90)
        name_entry = Entry(self.root, state=DISABLED , textvariable = self.cname, font=('calibre', 13, 'bold')).place(x=190, y=90)

        mobile_label = Label(self.root, text="Mobile:", font=('calibre', 13, 'bold')).place(x=125, y=129)
        mobile_entry = Entry(self.root, state=DISABLED,textvariable = self.mobile, font=('calibre', 13, 'bold')).place(x=190, y=129)

        balance_label = Label(self.root, text="Balance:", font=('calibre', 13, 'bold')).place(x=115, y=170)
        balance_entry = Entry(self.root, state=DISABLED,textvariable = self.amount, font=('calibre', 13, 'bold')).place(x=190, y=170)

        amount_label = Label(self.root, text="Enter Amount:", font=('calibre', 13, 'bold')).place(x=70, y=210)
        amount_entry = Entry(self.root,textvariable=self.amount2, font=('calibre', 13, 'bold')).place(x=190, y=210)

        checkout_btn = Button(self.root, text='Check Out',command=self.onClick,font=('calibre', 13, 'bold')).place(x=310, y=250)



        tree = ttk.Treeview(self.root, column=("c1", "c2", "c3"), show='headings', height=3)
        tree.column("# 1", anchor=CENTER,minwidth=0, width=120, stretch=NO)
        tree.heading("# 1", text="Date")
        tree.column("# 2", anchor=CENTER,minwidth=0, width=120, stretch=NO)
        tree.heading("# 2", text="CardID")
        tree.column("# 3", anchor=CENTER,minwidth=0, width=120, stretch=NO)
        tree.heading("# 3", text="Amount")

        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=(date, cardid, amount))
        tree.insert('', 'end', text="2", values=('07-05-2024', '4567', '2000'))

        tree.place(x=70, y=310)

        topup_btn = Button(self.root, text='Top Up', command=self.top, font=('calibre', 13, 'bold')).place(x=100, y=420)

        block_btn = Button(self.root, text='Block', command=self.block, font=('calibre', 13, 'bold')).place(x=230, y=420)

        back_btn = Button(self.root, text='Back',  font=('calibre', 13, 'bold')).place(x=350, y=420)




    def onClick(self):
        amount= self.amount.get()
        amount2=self.amount2.get()

        res= int(amount) - int(amount2)

        a = "success"
        b = amount2 +" "+"debited"
        c = "Remaining Balance"
        d = str(res)

        tk.messagebox.showinfo("Success", a + " " + "\n" + b + "\n" + c+ " "+ "\n"+ d)

    def top(self):
        self.root.withdraw()
        topup=TopUp(tk.Tk())

    def block(self):
        self.root.withdraw()
        blockcard = BlockCard(tk.Tk())


