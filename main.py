

from py_acr122u import nfc

reader = nfc.Reader()
reader.connect()
uidno = reader.get_uid()

print(uidno)

def uid():
    reader = nfc.Reader()
    reader.connect()
    x=reader.get_uid()
    uidno = ''.join(map(str, x))
    return uidno

# x = reader.read_binary_blocks(9,4)
# y = reader.read_binary_blocks(7,4)
# z = reader.read_binary_blocks(8,4)


# arr = []
# # iterating the value
# for value in x:
#     arr.append( str(value) )
# print(arr)


# name=bytes(x)
# number=bytes(y)
# amount=bytes(z)

# print(name)



# name = 'ayes'
# number='7020169938'
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
    x = reader.read_binary_blocks(6, 4)

    f_name = bytes(x)
    return f_name

def mobile():
    reader = nfc.Reader()
    reader.connect()
    x = reader.read_binary_blocks(7, 4)

    print(x)
    mobileno = bytes(x)
    return mobileno

def Balance():
    reader = nfc.Reader()
    reader.connect()

    x = reader.read_binary_blocks(8, 4)

    bal = bytes(x)
    balance=int(bal)
    return balance
    # else:


# def CardID():
#     reader = nfc.Reader()
#     reader.connect()
#     uid = reader.print_data(reader.get_uid())
#     x = reader.read_binary_blocks(9, 4)
#
#     print()
#     cardid = bytes(x)
#     return cardid

