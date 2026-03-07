# Sum of all even numbers between 1 to 100

sum = 0
range_val = int(input("Enter the range: "))
for i in range(1, range_val+1):
    if i % 2 == 0:
        sum+=i
print("The sum of all even numbers between 1 to 100 is: ", sum)