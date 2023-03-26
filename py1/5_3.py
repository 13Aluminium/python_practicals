import random

# Parent class
class Employee:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def display_employee_details(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Salary: {self.salary}")

# Child class (single inheritance)
class Manager(Employee):
  def __init__(self, name, age, salary, department):
    super().__init__(name, age, salary)
    self.department = department

  def display_manager_details(self):
    super().display_employee_details()
    print(f"Department: {self.department}")

# Child class (multilevel inheritance)
class AssistantManager(Manager):
  def __init__(self, name, age, salary, department, manager):
    super().__init__(name, age, salary, department)
    self.manager = manager

  def display_assistant_manager_details(self):
    super().display_manager_details()
    print(f"Manager: {self.manager}")

# Child class (multiple inheritance)
class Director(AssistantManager, Employee):
  def __init__(self, name, age, salary, department, manager, company):
    AssistantManager.__init__(self, name, age, salary, department, manager)
    self.company = company

  def display_director_details(self):
    AssistantManager.display_assistant_manager_details(self)
    print(f"Company: {self.company}")

# List of One Piece character names
one_piece_characters = ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook", "Jinbe"]

employees = []

for name in one_piece_characters:
  # Generate a random age and salary
  age = random.randint(18, 60)
  salary = random.randint(30000, 100000)
  employees.append(Employee(name, age, salary))

manager = Manager("Shanks", 35, 80000, "Pirates")
assistant_manager = AssistantManager("Boa Hancock", 28, 75000, "Pirates", "Shanks")
director = Director("Kaido", 50, 120000, "Pirates", "Shanks", "One Piece Inc.")

# Display the employee details
print("Employee details:")
for employee in employees:
  employee.display_employee_details()

# Display the manager details
print("\nManager details:")
manager.display_manager_details()

# Display the assistant manager details
print("\nAssistant manager details:")
assistant_manager.display_assistant_manager_details()

# Display the director details
print("\nDirector details:")
director.display_director_details()
