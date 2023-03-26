def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))  # Output: True
print(is_prime(21))  # Output: False

print("21DCE052")