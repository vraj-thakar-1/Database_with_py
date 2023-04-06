from utils import  database

user_choice ="""
- "a" to add a new book to
- "l" to list all books
- "rl" to list books which are already read
- "r" to mark a book as read
- "d" to delete a book
- "q" to quit
Your choice: """

def menu():
    user_inp = input(user_choice)
    # deal with user inputs
    while user_inp!= "q":
        if user_inp == "a":
            b_name= input("enter Book name: ")
            author_name= input("enter Book authorname: ")
            database.add_book(b_name, author_name)
        elif user_inp == "l":
            database.list_books()
        elif user_inp == "r":
            read_book_name= input("enter book name: ")
            database.read_book(read_book_name)
        elif user_inp == "d":
            d_book_name= input("enter book name: ")

            database.delete_book(d_book_name)
        elif user_inp=="rl":
            database.lise_read_books()
        else :
            print("invalid input try again...")
        user_inp = input(user_choice)

menu()