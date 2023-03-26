import datetime

name = input("What is your name? ")
age = int(input("What is your age? "))

current_year = datetime.date.today().year
year_of_hundred = current_year + 100 - age

print("Hello, " + name + "! You will turn 100 in the year " + str(year_of_hundred) + ".")
print("21DCE052")