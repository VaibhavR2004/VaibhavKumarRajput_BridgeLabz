from car import Car

# object = A "bundle" of realted attributes (varibale) and methods
# Ex. phone, cup, book
# You need a class to create many objects

# clas = ((blueprint)) used to design the structure and layout of an  object

car1=Car("Mustang", 2024,"red",False)
car2=Car("Corvette",2025,"blue",True)
car3=Car("Charger",2026,"yellow",True)


# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# car1.drive()
# car1.stop()

# car3.describe()


# class variable =shared among all instances of a class
#     defined outside the constructor
#     allsow you to shared data among all objects created from that class

class student:
    class_year = 2024
    num_students =0
    def __init__(self,name,age):
        self.name = name
        self.age=age
        student.num_students+=1

student1=student("Spongeboob",30)
student2=student("Patrick",35)
student3=student("Squidward",55)
student4=student("Sandy",30)


# print(student2.name)
# print(student2.age)
# print(student2.class_year)     #this can use with student1.class_year or any object or with class name
# print(student.num_students)
# print(f"My graduting clss of {student2.class_year} has {student1.num_students} students")



# # Inheritance = Allows a class to inherit attributes and methods from another class
# help with code resulability and extensibility
# class child(Parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self ,name,age):
        self.age=age
        super().__init__(name)
class Cat(Animal):
    def speak(self):
        print("MEOW")
class Mouse(Animal):
    def speak(self):
        print("WOOF")



# Dog = Dog("Scooby",12)
# cat=Cat("Garfield")
# mouse=Mouse("Micky")


# print(Dog.name)
# print(Dog.age)
# Dog.eat()
# Dog.sleep()

# Cat1=Cat("Kitty")
# print(Cat1.name)

# cat.speak()

#multiple inhertance = inhertance from mre than one parent class
# C(A,B)

# MULTILEVEL INHERTANCE = inhertance from a parent which inherits from another parents
# C(B)<- B(A) <-A

class Animal:

    def __init__(self,name):
        self.name=name


    def eating(self):
        print(f"{self.name} is eating")
    def sleeping(self):
        print(f"{self.name} os sleeping")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class bear(Predator):
    pass

class Rabbit(Prey):
    pass
class Lion(Predator):
    pass
class Hawk(Predator):
    pass
class Fish(Predator, Prey):
    pass

lion = Lion("Shera")
fish = Fish("Nemo")
hawk=Hawk("Bagga")

lion.eating()
lion.hunt()
fish.hunt()
fish.flee()
hawk.hunt()
hawk.sleeping()