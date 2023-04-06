"""
conserned with storing and retriving books from the  list
"""

books = []


# functions

def add_book(name, author):
    books.append({"name": name, 'author': author, 'read': False})

    print(books)


def list_books():
    for i, book in enumerate(books):
        print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{book['read']}")

        print('------------------------------')


def lise_read_books():
    readed_books = [book for book in books if book['read'] == True]
    for i, book in enumerate(readed_books):
        print(f"book{i}:\n name:{book['name']} \n author:{book['author']} \n read:{book['read']}")

        print('------------------------------')


def read_book(book_name):
    for book in books:
        if book["name"] == book_name:
            book["read"] = True


def delete_book(book_name):
    # for book in books:
    #     if book_name == book["name"]:
    #         books.remove(book)
    # list comprehension
    global books
    books = [book for book in books if book['name'] != book_name]
