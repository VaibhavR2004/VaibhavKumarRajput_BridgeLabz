# Abstract class: A class that cannot be instantiated don its own: Meant to be subclassed.
# They cab contain abstract method, which are declared but have no implementation.
# Abstract class benefits:
# 1.Prevents instantiation of the class itself
#2. Requires childern to use inherited abstract methods
#for the abstarct class function are conpulsary to def in the child class otherwise rase an error
from abc import ABC, abstractmethod

class Vehicle:
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the Car")

    def stop(self):
        print("You stop the car")



class Motorcycle(Vehicle):
    def go(self):
        print("You ride the Bike")

    def stop(self):
        print("You stop the Bike")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        print("You anchor the boat")


car=Car()
car.go()
car.stop()

boat=Boat()
boat.go()
boat.stop()
