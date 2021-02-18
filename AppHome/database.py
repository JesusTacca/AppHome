import sqlite3
import codecs
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Database/mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    temp = codecs.open('Database/database.txt', 'r', 'utf8')
    txt = temp.read()
    temp.close()
    txt = txt.split('|')
    cursorObj = con.cursor()
    for i in txt:
        cursorObj.execute(i)
    con.commit()

def sql_insert(con):
    cursorObj = con.cursor()
    txt = ["insert into usuario(name, surname, DNI, money, email) values ('Jesus Bryan', 'Tacca Gutierrez', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Jesus Ignacio', 'Tacca Zela', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Jhon Taiwua', 'Tacca Gutierrez', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Maria Jimena', 'Tacca Gutierrez', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Jean Piere Alex', 'Tacca Gutierrez', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Liz Maribel', 'Tacca Zela', 77204628, 0.0, 'job1and2ramza@gmail.com')",
        "insert into usuario(name, surname, DNI, money, email) values ('Elsa', 'Gutierrez Huaman', 77204628, 0.0, 'job1and2ramza@gmail.com')"
    ]
    for i in txt:
        cursorObj.execute(i)
    con.commit()

con = sql_connection()
sql_table(con)