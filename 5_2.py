import random

class Employee:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

class Company:
  def __init__(self, name, employees):
    self.name = name
    self.employees = employees

  def raise_salaries(self, percentage):
    for employee in self.employees:
      employee.salary *= 1 + percentage/100

# List of One Piece character names
one_piece_characters = ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook", "Jinbe"]

employees = []

for name in one_piece_characters:
  # Generate a random age and salary
  age = random.randint(18, 60)
  salary = random.randint(30000, 100000)
  employees.append(Employee(name, age, salary))

company = Company("One Piece Inc.", employees)

# Display the employee details before the salary raise
print("Before salary raise:")
for employee in employees:
  print(f"{employee.name}: {employee.salary}")

# Raise the salaries by 4%
company.raise_salaries(4)

# Display the employee details after the salary raise
print("\nAfter salary raise:")
for employee in employees:
  print(f"{employee.name}: {employee.salary}")
