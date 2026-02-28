# Let us define a function which takes another function as an argument and calls it
def call_function(func):
    print("Calling the function...")
    func()
    print("Function called.")

# Now let us define a simple function to be passed as an argument
def say_sairam():
    print("Sairam Everybody!")

# Let us call the function with the say_sairam function as an argument
call_function(say_sairam)