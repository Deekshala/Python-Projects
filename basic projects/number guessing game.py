import random
while True:
    user_input = int(input("enter your guess(between 1 and 10): "))
    computer_choice = random.randint(1,10)
    if user_input == computer_choice:
        print("you guessed correctly!!")
    elif user_input > computer_choice:
        print("too high!!")
    elif user_input < computer_choice:
        print("too low!!")
        break
    else:
        print("invalid input")