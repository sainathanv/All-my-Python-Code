# Fibonacci Filter which filter

num = int(input("Enter the limit = "))

def fibonacci_evens(num):
    x_0 = 0
    x_1 = 1
    for i in range(0, num):
        x = x_0 + x_1
        x_0 = x_1
        x_1 = x
        if x % 2==0:
            print(x)

fibonacci_evens(num)