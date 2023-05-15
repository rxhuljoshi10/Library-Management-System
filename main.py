import os
import sys
import csv
datafile = 'library.csv'
fieldnames = ['bid','title','author']

class Book:
    def __init__(self,bid, title, author):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = "available"

class Library:
    def __init__(self):
        self.books = []
        
    def addbook(self):
        os.system("cls")
        print("\tEnter Book Details\n")
        bid = input("Enter Book ID : ")
        title = input("Title : ")
        author = input("Author : ")

        book = Book(bid,title,author)
        self.books.append(book)

        print("\nSuccesfully saved the Book details..!!")

    def displaybooks(self):
        print("\tList of Books\n")
        for b in self.books:
            print(f"{b.bid} \t {b.title} \t {b.author}")

    def update(self,book):
        print()
        line()
        print(" 1 : BOOK ID")
        print(" 2 : BOOK TITLE")
        print(" 3 : BOOK AUTHOR")
        print(" 4 : Cancel")
        line()
        choice = int(input("Choose what to update : "))
        line()
        if choice == 1:
            book.bid = input("Enter Book ID : ")
        elif choice == 2:
            book.title = input("Enter Book Title : ")
        elif choice == 3:
            book.author = input("Enter Book Author : ")
        else:
            main()

        print("\nSuccessfully Updated...")

    def removebook(self,book):
        choice = input("\nYou sure you want to remove this book from library? (Y/N) : ")
        if choice == 'n' or choice == "N":
            main()
        
        print(f"\nBook with ID : '{book.bid}' removed from library")
        self.books.remove(book)

    def searchbook(self,val):
        flag = 0
        for book in self.books:
            if book.title.lower() == val.lower() or book.bid == val:
                flag = 1
                break
        
        if flag:
            print(f"\n{book.bid} \t {book.title} \t {book.author}")
            return book
        else:
            print("\nCan't find particular Book..!!")
            return False

    def load_datafile(self):
        with open(datafile, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book(row['bid'], row['title'], row['author'])
                self.books.append(book)

    def save_books(self):
        with open(datafile,'w',newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    'bid': book.bid,
                    'title': book.title,
                    'author': book.author,
                })

lib = Library()

def line():
    for i in range(34):
        print("-",end="")
    print("")

def pressEnter():
    input("\nPress 'ENTER' to continue ..!!")

def getval():
    val = input("Enter Book Title or Book ID : ")
    return val

def main():
    while 1:
        os.system("cls")
        line()
        print("*** LIBRARY MANAGEMENT SYSTEM ***")
        line()
        print("\t1 : Add Book")
        print("\t2 : Display Book")
        print("\t3 : Update Book")
        print("\t4 : Delete Book")
        print("\t5 : Search Book")
        print("\t6 : Exit")
        
        line()
        choice = input("Enter Choice : ")
        os.system("cls")

        if choice == '1':
            lib.addbook()
            
        elif choice == '2':
            lib.displaybooks()

        elif choice == '3':
            val=getval()
            book = lib.searchbook(val)
            if book:
                lib.update(book)

        elif choice == '4':
            val = getval()
            book = lib.searchbook(val)
            if book:
                lib.removebook(book)

        elif choice == '5':
            val = getval()
            lib.searchbook(val)

        elif choice == '6':
            sys.exit(1)
        
        else:
            continue

        lib.save_books()
        pressEnter()

if os.path.exists(datafile):
    lib.load_datafile()
main()