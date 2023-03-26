def fibonacci(n):

    fib_list = [1, 1] 
    if n == 1:
        return [1]
    elif n == 2:
        return fib_list
    else:
        for i in range(2, n):
            fib_num = fib_list[i-1] + fib_list[i-2]
            fib_list.append(fib_num)
        return fib_list

n = int(input("How many Fibonacci numbers do you want to generate? "))

fib_numbers = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fib_numbers}")
print("21DCE052")