# Password Validator

crct_password = "sairam123"

while True:
    password = input("Enter the password: ")
    if password == crct_password:
        print("Password is correct. Access granted.")
        break
    else:
        print("Incorrect password. Try again.")