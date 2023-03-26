def find_number_in_ordered_list(lst, num):

    if num in lst:
         print(f"{num} is in the list")
    else:
         print(f"{number} is not in the list")

ordered_list = input("Enter a list of numbers separated by spaces: ").split()

ordered_list  = [int(num) for num in ordered_list ]

number = input("Enter a number you want to find in the list:")
number = int(number)
find_number_in_ordered_list(ordered_list, number)

print("21DCE052")