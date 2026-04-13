# Nested class = Ac lass definec within aanother class
# class outer:
# class inner

"""Benefits: Aloow you to logically group class that are closely related
Encapsulates private details that aren't relevant outside of the outer class
Keep the namespace clean; reduces the possible of naming conflicts"""
class company:
    class Employee:
        def __init__(self,name,position):
            self.name =name
            self.position=position
        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self,company_name):
        self.company_name = company_name
        self.employee=[]
    
    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employee.append(new_employee)
    
    def list_employee(self):
        return[employee.get_details() for employee in self.employee]

company1 = company("Krusty Krab")
company2= company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongboob", "Cook")
company1.add_employee("Squidward", "Cashier")
# print(company.list_employee())

company2.add_employee("Sheldon","Manager")
company2.add_employee("Karen","Lead")
company2.add_employee("Sheldon","Employee")


for employee in company1.list_employee():
    print(employee)
for employee in company2.list_employee():
    print(employee)
