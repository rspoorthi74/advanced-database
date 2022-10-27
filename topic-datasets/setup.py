import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("Travel_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('shirts')")
cursor.execute("insert into list (description) values ('tshirts')")
cursor.execute("insert into list (description) values ('pants')")
cursor.execute("insert into list (description) values ('shorts with pockets')")
cursor.execute("insert into list (description) values ('toiletries')")

connection.commit()
connection.close()

print("done.")