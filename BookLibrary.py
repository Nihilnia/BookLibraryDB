from dbProcesses import *

Library = Library()
Library.connectAndCreate()

print("""
- - - - W E L C O M E  T O  L I B R A R Y - - - -


Options:

1) Show all the books

2) Add a new book

3) Delete a book

4) Update the publish

5) Exit


""")

while True:
    userChoice = input("What is your choice? ")

    if userChoice == "1":
        Library.showAllBooks()

    elif userChoice == "2":
        bookName = input("Book name:        ")
        bookType = input("Type of book:     ")
        bookAuthor = input("Author:         ")
        bookPublish = input("Publish:       ")

        newBook = Book(bookName, bookType, bookAuthor, bookPublish)
        Library.addABook(newBook)

    elif userChoice == "3":
        whichBook = input("Which book you wanna delete:     ")
        Library.deleteABook(whichBook)

    elif userChoice == "4":
        whichBook = input("Which book's you wanna update:     ")
        Library.updateThePublish(whichBook)

    elif userChoice == "5":
        print("See ya next time!")
        time.sleep(2)
        break

    else:
        print("There is no option like that..")
        time.sleep(2)