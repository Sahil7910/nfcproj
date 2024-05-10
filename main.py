from unittest import result

from py_acr122u import nfc



reader = nfc.Reader()
reader.connect()
uid=reader.print_data(reader.get_uid())
x = reader.read_binary_blocks(9,4)
# y = reader.read_binary_blocks(7,4)
# z = reader.read_binary_blocks(8,4)
print(uid)


# name=bytes(x)
# number=bytes(y)
# amount=bytes(z)

# print(name)



# name = 'ayes'
# number='7020169938'
# cardid='1234'
# n_bytes=bytearray(cardid, 'utf-8')
# print(type(n_bytes))

# arr = []
# iterating the value
# for value in n_bytes:
#     arr.append( int(value) )
# print(type(arr))
#
#
#
# y = reader.update_binary_blocks(9, 4, arr)





# reader.update_binary_blocks(4,4,[1,1,1,1])
# reader.authentication()
# reader.read_binary_blocks()


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
    bal = bytes(x)
    balance=int(bal)
    print(type(balance))
    return balance

def CardID():
    reader = nfc.Reader()
    reader.connect()
    uid = reader.print_data(reader.get_uid())
    x = reader.read_binary_blocks(9, 4)

    print()
    cardid = bytes(x)
    return cardid

