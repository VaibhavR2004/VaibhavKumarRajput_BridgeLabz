# super() = function used in a child class to call method from a parent class(superclass)
# Alḷow you to extext the function of the inherited methods


class Shape:
    def __init__(self, color, filled):
        self.color=color
        self.filled=filled
    
    def describe(self):
        print(f"It is {self.color} and {"filled"if self.filled else "Not Filled"}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius
    def describe(self):
        super().describe()
        print(f"It is a circle with area of {3.14*(self.radius**2)}cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color,filled)
        self.width=width
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color,filled)
        self.width=width
        self.height=height


circle=Circle("red", True,5)
square=Square("Blue",True, 5)
triangle=Triangle("Orange",False, 5,10)

print(circle.color)
print(circle.filled)
circle.describe()

print("\n")
print(square.color)
print(square.filled)
print(f"{square.width}cm")

triangle.describe()