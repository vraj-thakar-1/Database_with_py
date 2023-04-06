"""
conserned with storing and retriving books from  a csv file
you know about the format of the file
name,author,read
"""
import sqlite3


# functions

def create_book_file_initialy():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    # print(cursor.fetchall()) # return list of tupel elements
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()
    return books;


def list_books():
    # print list of all books
    all_books = get_all_books()
    if len(all_books) > 0:
        print("all Books")
        for i, book in enumerate(all_books):
            read = "yes" if book['read'] == 1 else "no"

            print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{read}")

            print('------------------------------')
    else:
        print("you have no any book yet, add first...:)")


def list_read_books():
    all_books = get_all_books()
    readed_books = [book for book in all_books if book['read'] == 1]

    for i, book in enumerate(readed_books):
        read = "yes" if book['read'] == 1 else "no"
        print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{read}")

        print('------------------------------')


def mark_book_as_read_book(book_name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_name,))
    connection.commit()
    connection.close()


def delete_book(book_name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (book_name,))
    connection.commit()
    connection.close()
