class Emp:
    def __init__(self, name,salary):
        self.name=name
        self.salary=salary
    def displayEmployee(self):
        print("Name: ", self.name ,"Salary: ", self.salary)


emp1=Emp("Raj", 20000)
emp2=Emp("Mayur" , 50000)
emp1.displayEmployee()
emp2.displayEmployee()
print("\nAuthor: Ayush Luhar\nID NO. 21DCE052")
