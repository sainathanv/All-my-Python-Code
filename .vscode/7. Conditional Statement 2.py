# Now let us focus on nested if, elif and else statements.

maths = int(input("Enter your marks in Maths: "))
science = int(input("Enter your marks in Science: "))

cutoff = (maths + science) / 2

# let us say the cutoff is 50, then we can use nested if statements to check the marks.

if maths >= 35:
    if science >= 35:
        if cutoff >= 50:
            print("You have passed the exam.")
        else:
            print("You have failed the exam.")
    else:
        print("You have failed the exam.")
else:
    print("You have failed the exam.")      # Like this, something! Don't see the matter.... See the logic and the control flow!