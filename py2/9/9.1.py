import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


my_circle = Circle(5)

area = my_circle.area()
perimeter = my_circle.perimeter()

print("Radius:", my_circle.radius)
print("Area:", area)
print("Perimeter:", perimeter)

print("21DCE052")