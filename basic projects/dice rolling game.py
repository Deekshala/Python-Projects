import random
while True:
    user=input("roll the dice?(y/n): ")
    if user == "y":
        print(random.randint(1,10),random.randint(1,10))
    elif user == "n":
        print("Thanks for playing")
        break
    else:
        print("invalid input")