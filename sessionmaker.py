from tkinter import messagebox

from sqlalchemy import engine, and_
from sqlalchemy.orm import sessionmaker
from DataBase import *
from main import uid

Session = sessionmaker(bind = engine)
session = Session()


uidno=uid()
print(uidno)

result = session.query(Members).filter(and_(Members.cardid == uidno, Members.status == 1))

for row in result:
    if row is not None:
        print("card found")
        break
else:
    messagebox.showerror("error", "CardID Not Found")


# c1 = Members(cardid =uidno , status = 0)
# session.add(c1)
# session.commit()


