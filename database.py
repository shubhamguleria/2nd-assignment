#Question1
'''
import sqlite3
conn=sqlite3.connect("BB.db")
curs=conn.cursor()
book="Create table Book(bookId int(5) primary key,titleId int(5),location char(20),genre char(20));"
title="Create table Titles(titleId int(5),ISBN int(13),publisherId char(10),publicationYear int(4),foreign key(titleId) references Book(titleId));"
publisher="Create table Publishers(publisherId char(10),name char(10),streetAddress char(10),suiteNo int(3),zipCodeId int(6),foreign key(publisherId) references Titles(publisherId));"
code="Create table ZipCodes(zipCodeId int(6),city char(10),state char(10),zipCode int(6),foreign key(zipCode) references Publishers(zipCodeId));"
authortitle="Create table AuthorsTitles(authorTitleId char(5),authorId char(7),titleId int(5),foreign key(titleId) references Titles(titleId));"
author="Create table Authors(authorId char(7) primary key,fname char(10),mname char(10),lname char(10),foreign key(authorId) references AuthorsTitles(authorId));"
curs.execute(book)
curs.execute(title)
curs.execute(publisher)
curs.execute(code)
curs.execute(authortitle)
curs.execute(author)
print("All the tables are created")
'''
#Question2
'''
import sqlite3
conn=sqlite3.connect("BB.db")
cur=conn.cursor()
book='insert into Book values(01,11,"Himachal","Action");'
cur.execute(book)
book='insert into Book values(02,12,"Delhi","Horror");'
cur.execute(book)
book='insert into Book values(03,13,"Mumbai","Thrill");'
cur.execute(book)
title='insert into Titles values(001,111,"pb1",1994);'
cur.execute(title)
title='insert into Titles values(002,112,"pb2",1995);'
cur.execute(title)
title='insert into Titles values(003,113,"pb3",1996);'
cur.execute(title)
publisher='insert into Publishers values("pb4","Anoop Katoch","Chandigarh",22,123000);'
cur.execute(publisher)
publisher='insert into Publishers values("pb5","Appy Thakur","Amritsar",33,124000);'
cur.execute(publisher)
code='insert into ZipCodes values(121212,"Batala","Punjab",176061);'
cur.execute(code)
code='insert into ZipCodes values(131313,"Palampur","Himachal Pradesh",176062);'
cur.execute(code)
code='insert into ZipCodes values(141414,"Filmy Stan","Delhi",770052);'
cur.execute(code)
authortitle='insert into AuthorsTitles values("a","xyz",12345);'
cur.execute(authortitle)
authortitle='insert into AuthorsTitles values("b","zyx",54321);'
cur.execute(authortitle)
author='insert into Authors values("zyx","Anoop","Chand","Katoch");'
cur.execute(author)
conn.commit()
print("All values are inserted")

'''
#Question3
'''
import sqlite3
conn=sqlite3.connect("DB.db")
cur=conn.cursor()
print("Original values of the table Book")
table="select * from Book;"
cur.execute(table)
for i in cur.fetchall():
    print(i)
print("After updating the location for bookId 03")
table='update Book set location = "Mysore" where bookId = 03;'
cur.execute(table)
print("After updating values of the table Book")
table="select * from Book;"
cur.execute(table)
for i in cur.fetchall():
    print(i)
print("Original values of the table Authors")
table="select * from Authors;"
cur.execute(table)
for i in cur.fetchall():
    print(i)
table='update Authors set fname = "Harley" where authorId="xyz"'
cur.execute(table)
print("after updating values of the table Authors")
table="select * from Authors;"
cur.execute(table)
for i in cur.fetchall():
    print(i)

print("Values updated")

'''
