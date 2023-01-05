class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name

class Exam(Student):
    def __init__(self, rollNumber, name, *marks):
        super().__init__(rollNumber, name)
        self.marks = marks

class Result(Exam):
    def __init__(self, rollNumber, name, *marks):
        super().__init__(rollNumber, name, marks)
        self.totalMarks = sum(marks)

# Example usage:
student = Result(1, "John", 85, 75, 95, 90, 80, 70)
print(f"Total marks for student {student.name}: {student.totalMarks}")
