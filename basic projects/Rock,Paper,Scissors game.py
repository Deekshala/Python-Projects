import random
while True:
    user_input=(input("rock,paper,scissors(r/p/s): ")).lower()
    letter=random.choice("rps")
    print("you chose: ",user_input)
    print("computer chose: ",letter)
    if user_input==letter:
        print("Tie")
    elif user_input=='r' and letter=='p':
        print("you win")
    elif user_input=='r'and letter=='s':
        print("you win")
    elif user_input=='p' and letter=='r':
        print("you win")
    elif user_input=='p' and letter=='s':
        print("you loose")
        break
    else:
        print("invalid letters")
