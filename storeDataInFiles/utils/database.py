"""
conserned with storing and retriving books from  a csv file
you know about the format of the file
name,author,read
"""
import sqlite3
books_file = "books.txt"


# functions

def create_book_file_initialy():
    with open(books_file,"w") as file:
        pass

def add_book(name, author):
    with open(books_file, "a") as file:
        file.write(f"{name},{author},0\n")

def get_all_books():
    with open(books_file, 'r') as file:
        # following is list of list
        lines = [line.strip().split(",") for line in file.readlines()]
    all_books = [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


    # make a dictionary with comprehension
    return all_books


def list_books():
    # print list of all books
    all_books = get_all_books()
    if len(all_books)>0:

        for i, book in enumerate(all_books):
            read = "yes" if book['read']=="1" else "no"
            print("all Books")
            print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{read}")

            print('------------------------------')
    else:
        print("you have no any book yet, add first...:)")


def list_read_books():
    all_books= get_all_books()
    readed_books = [book for book in all_books if book['read'] == "1"]
    # print("all books which are read")
    # print(readed_books)
    # print(f"allbooks: { all_books}")

    for i, book in enumerate(readed_books):
        read = "yes" if book['read']=="1" else "no"
        print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{read}")

        print('------------------------------')


def mark_book_as_read_book(book_name):
    all_books= get_all_books()
    for book in all_books:
        if book["name"] == book_name:
            book["read"] = 1
    _save_all_books(all_books)
def _save_all_books(books):
    with open(books_file,"w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(book_name):
    # for book in books:
    #     if book_name == book["name"]:
    #         books.remove(book)
    # list comprehension
    all_books= get_all_books()

    books = [book for book in all_books if book['name'] != book_name]
    _save_all_books(books)
