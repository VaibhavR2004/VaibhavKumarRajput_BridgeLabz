"""Magic Method = Dunder method (double underscore) __init__, __str__,__eq__
They are automatic called by many of Python's built-in operations.
They allow developer to define or customizs the behavior of objects"""

class Book:
    def __init__(self,title, author, num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
    
    def __str__(self):    #string representation of the object
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title==other.title and self.author== other.author
    
    def __lt__(self,other):
        return self.num_pages<other.num_pages
    def __gt__(self,other):
        return self.num_pages>other.num_pages
    
    def __add__(self, other):
        return self.num_pages+other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key=='num_pages':
            return self.num_pages
        else:
            return f"Key {key} not found"


book1=Book("Harry Potter ......","J.K.Rowling",310)
book2=Book("The Hobbit","J.R.R.Tolkein",500)
book3=Book("Game of Throne","George R.R. Martin",999)

# print(book1)
# print(book2)

# print(book1==book2)
# print(book1<book2)
# print(book1>book2)
# print(book1+book2)

# print("George" in book3)
print(book1['title'])   #in case we want the title of the book 1 than use getitem
print(book1['author'])
print(book1['num_pages'])
print(book1['Capters'])
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Overloading + operator
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"


# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# result = v1 + v2   # Calls __add__()

# print(result)


# OTHER DUNDER METHOS
# __add__() → +
# __sub__() → -
# __mul__() → *
# __truediv__() → /
# __eq__() → ==