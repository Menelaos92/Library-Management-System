import sqlite3

##################################################################################################
# This class contains methods as a connective link between front end (tkinter GUI) and sqlite database.
##################################################################################################

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookTB (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookTB VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_all():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookTB")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookTB WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM bookTB WHERE id=?', (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('UPDATE bookTB SET title=?, author=?, year=?, isbn=? WHERE id=?', (title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
# print(search(author='Roger Miron'))
print(view_all())
