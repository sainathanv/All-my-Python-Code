# Let us generate OTP using random and string modules in Python. 
# This OTP will be a 6-digit number.

import random
import string

def otp_agent(length):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def main():
    length = 6
    secure_otp = otp_agent(length)
    
    print("\nYour secure OTP is:", secure_otp)
main()