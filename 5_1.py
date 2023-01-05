import random

class Employee:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def display_employee_details(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Salary: {self.salary}")

# List of One Piece character names
one_piece_characters = ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook", "Jinbe"]

employees = []

for name in one_piece_characters:
  # Generate a random age and salary
  age = random.randint(18, 60)
  salary = random.randint(30000, 100000)
  employees.append(Employee(name, age, salary))

# Display the employee details
for employee in employees:
  employee.display_employee_details()
