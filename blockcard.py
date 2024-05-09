import tkinter as tk
from tkinter import *


class BlockCard():
    def __init__(self, rt):
        self.root = rt
        self.root.title('Block Card')
        self.root.geometry("500x300")

        block_lable = Label(self.root, text="Block Card ?", font=('calibre', 13, 'bold')).place(x=220, y=50)

        pass_label = Label(self.root, text="password:", font=('calibre', 12, 'bold')).place(x=120, y=90)
        pass_entry = Entry(self.root, font=('calibre', 13, 'bold')).place(x=215, y=90)

        ok_btn = Button(self.root, text='Submit', font=('calibre', 13, 'bold')).place(x=270, y=120)
