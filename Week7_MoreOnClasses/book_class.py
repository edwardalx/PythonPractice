class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    def __del__(self):
        return f"Deleting {self.title}"
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    # def __eq__(self, other):
    #     return  (self.title == other.title and
    #             self.author == other.author and
    #             self.year == other.year)
    

my_book1 = Book("1984", "George Orwell", 1949)
my_book2 = Book("1984", "George Orwell", 1949)
print(my_book1 == my_book2)
print(my_book1.year + my_book2.year)