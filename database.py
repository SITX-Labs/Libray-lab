import os
import sqlite3
from turtle import position
import database





outpath = os.path.join(os.getcwd(), 'data')


connection = sqlite3.connect("data/db.sqlite3",check_same_thread=False) 
cursor = connection.cursor() 

# profiles table
cursor.execute("create table if not exists students(name TEXT,group_name TEXT,phone_number TEXT,number_SB TEXT,date_sb TEXT,read_ticket_name TEXT,read_ticket_date TEXT)")
cursor.execute("create table if not exists books (name_of_the_book TEXT, count_books INT INT NOT NULL, author_book TEXT,years_create TEXT)")
cursor.execute("create table if not exists branches(name TEXT)")
cursor.execute("create table if not exists style(name TEXT)")
cursor.execute("create table if not exists groups(name TEXT)")
cursor.execute("create table if not exists workers(name TEXT,position TEXT)")



def writeNewWorker(name,position):
    res = cursor.execute("SELECT * FROM workers where name =?",[name]).fetchone()
    if res is None:
        cursor.execute("INSERT OR IGNORE INTO workers(name,position) VALUES (?,?)",[name,position])
        connection.commit()
        return("Информации о Вас не обнаружено в Базе Данных работников, создаю новую запись")

    else:
        cursor.execute("update workers set position = ? where name = ?", [position,name]) 
        connection.commit()
        return("Информация о Вас уже есть в Базе Данных, перезаписываю")  

def writeNewStyle(style):
    res = cursor.execute("SELECT * FROM style where name =?",[style]).fetchone()
    if res is None:
        cursor.execute("INSERT OR IGNORE INTO style(name) VALUES (?)",[style,])
        connection.commit()
        return("Информации о данном стиле не обнаружено в Базе Данных стилей, создаю новую запись")
        
    else:
        return("Информация о таком стиле уже есть в Базе Данных")  


def writeBooks(name_of_the_book,number_of_books,book_author, book_year_created):
    res = cursor.execute("SELECT * FROM books where name_book =?",[name_of_the_book]).fetchone()
    if res is None:
        cursor.execute("INSERT OR IGNORE INTO books(name_book,count_books,author_book,years_create) VALUES (?,?,?,?)",[name_of_the_book,number_of_books,book_author, book_year_created])
        connection.commit()
        return("Такой книги нет в Базе Данных, создаю новую запись")

    else:    
        return("Такая книга уже есть в Базе Данных")
