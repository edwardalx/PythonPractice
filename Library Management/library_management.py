class Book:
    def __init__(self, title, author,_is_checked_out = 0 ):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def __str__(self):
        return(f"{self.title} by {self.author}")
    def check_a_book(self):
        if self._is_checked_out == 0:
             self._is_checked_out = 1
             return True
        return False
    def return_book(self):
        if self._is_checked_out == 1:
              self._is_checked_out = 0
              return True
        return False

class Library:
    def __init__(self):
        self._books = []
        
     

    def add_book(self,newbook):
        if  isinstance(newbook,Book):
            self._books.append(newbook)
            return
        
    
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.check_a_book():
                    print(f"{title} is checked out")
                    return
                print(f"{title} is not available")
                return
        
            
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned")
                    return
                print(f"{title} was not checked out")
                return
            
    def list_available_books(self):
        for book in self._books:
            if  book._is_checked_out == 0:
                print(book)
          
    

# myBook = Book("The Beast","edward")
# lib = Library()
# print(myBook)
# lib.add_book(myBook)
# lib.list_available_books()
# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))

# library = Library()
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")

# library.add_book(book1)
# library.add_book(book2)

# library.list_available_books()  # Should list both books

# library.check_out_book("1984")  # Should check out "1984"
# library.check_out_book("1984")  # Should say "1984 is not available"

# library.return_book("1984")  # Should return "1984"
# library.return_book("1984")  # Should say "1984 was not checked out"

# library.list_available_books()  # Should list both books again