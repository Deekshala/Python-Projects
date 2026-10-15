import random
import string
len = int(input("Enter password length: "))

uppercase=input("Include uppercase letters(y/n):")
number=input("Include numbers(y/n):")
special=input("Include special characters:")

characters=string.ascii_lowercase
if uppercase=="y":
    characters+=string.ascii_letters
if number=="y":
    characters+=string.digits
if special=="y":
    characters+=string.punctuation

passwords=""
for i in range(len):
    passwords+=random.choice(characters)

print("generated password: ",passwords)