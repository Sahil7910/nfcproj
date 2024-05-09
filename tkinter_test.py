import tkinter as tk
from py_acr122u import nfc
from checkout import CheckOut
from login import Login


reader = nfc.Reader()
reader.connect()
uid=reader.print_data(reader.get_uid())


def name():
    reader = nfc.Reader()
    reader.connect()
    uid = reader.print_data(reader.get_uid())
    x = reader.read_binary_blocks(6, 4)

    print(x)
    f_name = bytes(x)

    return f_name

def mobile():
    reader = nfc.Reader()
    reader.connect()
    uid = reader.print_data(reader.get_uid())
    x = reader.read_binary_blocks(7, 4)

    print(x)
    mobileno = bytes(x)
    return mobileno

def Balance():
    reader = nfc.Reader()
    reader.connect()
    uid = reader.print_data(reader.get_uid())
    x = reader.read_binary_blocks(8, 4)

    print(x)
    balance = bytes(x)
    return balance

def CardID():
    reader = nfc.Reader()
    reader.connect()
    uid = reader.print_data(reader.get_uid())
    x = reader.read_binary_blocks(9, 4)

    print()
    cardid = bytes(x)
    return cardid



root = tk.Tk()
# login = Login(root)
# tap = TapUser(root)
checkout= CheckOut(root)
# admin= Admin(root)
# topup=TopUp(root)
# blockcard=BlockCard(root)
# addmember=AddMember(root)
root.mainloop()