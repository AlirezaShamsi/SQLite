import sqlite3 as db
from time import sleep
def create_database():
    conn = db.connect('database.db')
    conn.close()
    print("OK - Database is created.")
    print("******************************************")
    print("##########################################")
    print("******************************************")
def create_table():
    conn = db.connect('database.db')
    cur = conn.cursor()
    cur.execute("create table contact (id integer primary key autoincrement, fullname text, phone text)")
    conn.close()
    print("OK - table is created now.")
    print("******************************************")
    print("##########################################")
    print("******************************************")
def insert_table():
    conn = db.connect('database.db')
    cur = conn.cursor()
    full_name = input("Enter Full name: ")
    phone = input("Enter phone number: ")
    cur.execute("insert into contact(fullname, phone) values('{}', '{}')".format(full_name,phone))
    conn.commit()
    conn.close()
    print("OK - Contact is inserted successfully. ")
    print("-----------------------------------------")
def show_contact():
    conn = db.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from contact")
    contact = cur.fetchall()
    conn.close()
    print(contact)
    print("-----------------------------------------")
def edit_contact():
    conn = db.connect('database.db')
    cur = conn.cursor()
    c_id = int(input("Enter an id for edit contact: "))
    fullname = input("Enter full name : ")
    phone = input("Enter phone number : ")
    cur.execute("update contact set fullname = '{1}' , phone = '{2}' where id ={0}".format(c_id, fullname, phone))
    conn.commit()
    conn.close()
    print("OK - Contact is updated successfully. ")
    print("-----------------------------------------")
def delete_contact():
    conn = db.connect('database.db')
    cur = conn.cursor()
    c_id = int(input("Enter an id for edit contact: "))
    cur.execute("delete from contact where id = {0}".format(c_id))
    conn.commit()
    conn.close()
    print("OK - Contact is deleted successfully. ")
    print("-----------------------------------------")
while True:
    print("For first time you must create database(1) and tabale(2)")
    print("1.Create database")
    print("2.Create table")
    print("3.Insert contact")
    print("4.Edit contact")
    print("5.Delete contact")
    print("6.Show contact")
    print("7.Exit")
    options = int(input("Select 1 - 7 :"))
    if options == 7:
        print("Have a nice day ;)")
        sleep(2)
        break
    if options == 1:
        create_database()
    if options == 2:
        create_table()
    if options == 3:
        insert_table()
    if options == 4:
        edit_contact()
    if options == 5:
        delete_contact()
    if options == 6:
        show_contact()