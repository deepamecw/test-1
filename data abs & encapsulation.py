class library:
    def __init__(self,books):
        self.books = books
    def list_books(self):
        print("available books")
        for books in self.books:
            print(books)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("book available")
            self.books.remove(borrow_book)
        else:
            print("book not available")

    def return_book(self,return_book):
        print("you have returned the book")
        self.books.append(return_book)
books = ["c","c++","java"]
s = library(books)
s.list_books

msg ="""
     1. display book
     2. borrow book
     3.return book
     """
while True:
    print(msg)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        s.list_books()
    elif ch == 2:
        book = input("enter the book to borrow: ")
        s.borrow_book(book)
    elif ch == 3:
        book = input("enter the book to return: ")
        s.return_book(book)
    else:
        print("thank you")
        quit
