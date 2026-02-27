# Let us start defining functions. A Simple greeting function.

def greet(name):
    return f"Sairam {name}! Welcome to SSSIHL."

# Example usage:
name = input("Enter your name: ")
greeting_message = greet(name)
print("\n",greeting_message)