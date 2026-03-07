# We have to check whether the number is divisible by 3 or 5.

num = int(input("Enter any number: "))

def check_divisibility(num):
	if (num % 3 == 0 and num % 5 == 0):
		return "FizzBuzz"
	elif (num % 3 == 0 and num % 5 != 0):
		return "Fizz"
	elif (num % 3 != 0 and num % 5 == 0):
		return "Buzz"
	else:
		return num


print(check_divisibility(num))