# Static Method= A method that belong to a class ratherthan any object from that class (instance)
# usually used for general utility function

"""Instance method = Best for operation on instance of the class
Static method = Best for utility function that do need access to class"""

class Employee:

    def __init__(self,name, position):
        self.name = name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position= ["Manager","Casher","Janitor"]
        return position in valid_position
employee1=Employee("Eugene", "Manager")
employee2=Employee("Spongboob", "Cook")
employee3=Employee("Squidward", "Cashier")

print(Employee.is_valid_position("Rocket Scientist"))
# You can access that static function directly using the class you donot have to create an object for that

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())