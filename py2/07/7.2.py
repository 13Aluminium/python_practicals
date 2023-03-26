def remove_duplicates(lst):
    return list(set(lst))

user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(num) for num in user_list]  # Convert input to integers
new_list = remove_duplicates(user_list)

print("Original list:", user_list)
print("List with duplicates removed:", new_list)

print("21DCE052")