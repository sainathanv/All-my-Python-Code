# We are going to try out the conditional statements in Python.
# We will be using basic if, elif and else statements to understand how they work.
# Then, we will move onto the nested if statements and so on.

maths = int(input("Enter your marks in Maths: "))
physics = int(input("Enter your marks in Physics: "))
chemistry = int(input("Enter your marks in Chemistry: "))

if maths >= 90 and physics >= 90 and chemistry >= 90:
    print("You have scored an A grade in all subjects.")
elif maths >= 80 and physics >= 80 and chemistry >= 80:
    print("You have scored a B grade in all subjects.")
elif maths >= 70 and physics >= 70 and chemistry >= 70:
    print("You have scored a C grade in all subjects.")
elif maths >= 60 and physics >= 60 and chemistry >= 60:
    print("You have scored a D grade in all subjects.")
else:
        print("You have scored a F grade in all subjects.")