import sqlite3, time


class Book():

    def __init__(self, bookName, bookType, author, publish):

        self.bookName = bookName
        self.bookType = bookType
        self.author = author
        self.publish = publish

    def __str__(self):

        return "\nBook Name: {}\nType: {}\nAuthor: {}\nPublish: {}".format(self.bookName, self.bookType, self.author, self.publish)


class Library():

    def __init__(self):

        self.connectAndCreate()

    def connectAndCreate(self):

        self.connectToDB = sqlite3.connect("MyBooks.db")
        self.cursor = self.connectToDB.cursor()
        self.cursor.execute("CREATE TABLE if not exists AllBooksInLibrary (BookName TEXT, BookType TEXT, BookAuthor TEXT, BookPublish INT)")
        self.connectToDB.commit()

    def cutTheConnection(self):

        self.connectToDB.close()

    def showAllBooks(self):

        query = "Select * From AllBooksInLibrary"
        self.cursor.execute(query)
        AllBooks = self.cursor.fetchall()

        if len(AllBooks) != 0:
            for f in AllBooks:
                Books = Book(f[0], f[1], f[2], f[3])
                print(Books)
        
        else:
            time.sleep(2)
            print("There is no book in library yet!\n")

    def findABook(self, whichBook):

        query = "Select * From AllBooksInLibrary where BookName = (?)"
        self.cursor.execute(query, (whichBook, ))
        TheBook = self.cursor.fetchall()

        if not TheBook:
            print("There is no book named:", whichBook)
        else:
            Found = Book(TheBook[0][0], TheBook[0][1], TheBook[0][2], TheBook[0][3])
            print(Found)

    def addABook(self, Book):

        query = "Insert into AllBooksInLibrary values (?, ?, ?, ?)"
        print("Book is adding to library..")
        time.sleep(2)
        self.cursor.execute(query, (Book.bookName, Book.bookType, Book.author, Book.publish ))
        self.connectToDB.commit()
        print("Book added succesfuly!\n")


    def deleteABook(self, whichBook):

        query = "Select * From AllBooksInLibrary where BookName = (?)"
        self.cursor.execute(query, (whichBook, ))
        TheBook = self.cursor.fetchall()

        deleteQuery = "Delete from AllBooksInLibrary where BookName = (?)"

        if not TheBook:
            print("There is no book named:", whichBook)
        else:
            print("The Book: {} is deleting..".format(whichBook))
            self.cursor.execute(deleteQuery, (whichBook, ))
            time.sleep(2)
            self.connectToDB.commit()
            print("Book deleted!\n")

    def updateThePublish(self, whichBook):

        query = "Select BookPublish From AllBooksInLibrary where BookName = (?)"
        self.cursor.execute(query, (whichBook, ))
        TheBook = self.cursor.fetchall()

        updateQuery = "Update AllBooksInLibrary set BookPublish = (?) where BookName = (?)"

        if not TheBook:
            print("There is no book named:", whichBook)
        else:
            newPublishValue = int(TheBook[0][0]) + 1
            print("Publish updating..")
            self.cursor.execute(updateQuery, (newPublishValue, whichBook, ))
            time.sleep(2)
            self.connectToDB.commit()
            print("Publish updated!\n")




