def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))
print("Max is :",maximum(a, b, c))