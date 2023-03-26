# Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


s = Student("Levi Ackerman", 123)
print("Single Inheritance:")
print("Name:", s.name)
print("Roll Number:", s.roll_no)


# Multilevel Inheritance
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state


class StudentWithAddress(Student, Address):
    def __init__(self, name, roll_no, city, state):
        Student.__init__(self, name, roll_no)
        Address.__init__(self, city, state)


sa = StudentWithAddress("luffy", 456, "Delhi", "DL")
print("\nMultilevel Inheritance:")
print("Name:", sa.name)
print("Roll Number:", sa.roll_no)
print("City:", sa.city)
print("State:", sa.state)


# Multiple Inheritance
class Marks:
    def __init__(self, marks):
        self.marks = marks


class StudentWithMarks(Student, Marks):
    def __init__(self, name, roll_no, marks):
        Student.__init__(self, name, roll_no)
        Marks.__init__(self, marks)


sm = StudentWithMarks("Eren Yeager", 789, 95)
print("\nMultiple Inheritance:")
print("Name:", sm.name)
print("Roll Number:", sm.roll_no)
print("Marks:", sm.marks)
print("\nAuthor: Ayush Luhar\nID NO. 21DCE052")
