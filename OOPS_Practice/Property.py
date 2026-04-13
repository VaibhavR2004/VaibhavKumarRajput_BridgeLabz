"""
@property = Decoder used a methof=d define a method as a property (it can be accessed like an attributes)
Benefits:Add addition logic when read, write, or delete attributes
Give you getter, setter and deleter method

| Type                    | Syntax    | Access                     |
| ----------------------- | --------- | -------------------------- |
| Public                  | `width`   | Anywhere                   |
| Protected (convention)  | `_width`  | Accessible but discouraged |
| Private (name mangling) | `__width` | Harder to access           |

"""
class Rectangle:
    def __init__(self,width,height):
        self.__width=width 
        self.__height=height
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self.__width=new_width
        else:
            print("Width must be greater than Zero")
    @height.setter
    def height(self, new_height):
        if new_height>0:
            self.__height=new_height
        else:
            print("Height must be greater than Zero")
rect= Rectangle(4,5)
print(rect.width)
print(rect.height)

rect.height=10
rect.width=20

print(rect.width)
print(rect.height)
