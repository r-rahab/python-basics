# oop = object-oriented programming

# properties + functions
# class # template

# book title, author, isbn, price
class Book:
    # constructor == function
    def __init__(self, book_name, author, isbn, price):
        self.title = book_name
        self.author = author
        self.isbn = isbn
        self.price = price

    def print_details(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Price", self.price)
        print("-------------------")

    def appy_discount(self, discount):
        self.price = self.price * (1 - discount / 100)
        print("New Price is ", self.price)


b1 = Book("Two rivers", "Chinua Achebe", "ISB001", 300)
b2 = Book("Think And Grow Rich", "John Moore", "ISB002", 700)

b1.print_details()
b1.appy_discount(10)
b1.print_details()
print(b2.price)

# varibales created from a class data+functions