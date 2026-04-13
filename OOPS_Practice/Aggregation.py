# Aggregation= Represent a relationship where one object(the whole)
# contain refernces tp one or more INDEPENDENT object(the part)

class Library:
    def __init__(self,name):
        self.name = name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def list_book(self):
        return[f"{book.title} by {book.author}" for book in self.books]
class Book:
    def __init__(self, title,author):
        self.title=title
        self.author=author
library=Library("New York Public Library")

book1=Book("Harry Potter ......","J.K.Rowling")
book2=Book("The Hobbit","J.R.R.Tolkein")
book3=Book("Game of Throne","George R.R. Martin")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# print(library.name)
# # print(library.list_book())
# for book in library.list_book():
#     print(book)


# Composition= the composed object directly owns itd components, which cannot exist independently "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,make, model, horse_power, wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(horse_power)
        self.wheels= [Wheel(wheel_size)for wheel in range(4)]
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} (hp) {self.wheels[0].size}"
car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)
car3 = Car(make="BMW", model="M4 Competition", horse_power=500, wheel_size=18)


print(car1.display_car())
print(car2.display_car())
print(car3.display_car())

