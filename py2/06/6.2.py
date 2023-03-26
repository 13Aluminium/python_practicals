def first_last_elements(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[0], lst[-1]]

input_str = input("Enter a list of numbers separated by spaces: ")
lst = [int(num) for num in input_str.split()]
result = first_last_elements(lst)
print(result)

print("21DCE052")