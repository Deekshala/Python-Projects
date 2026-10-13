import random
score=[0]
score2=[0]
print("Player 1's turn")
while True:
    for i in range(5):
        user_input=input("\nRoll the dice(y/n):")
        if user_input=='y':
            num=random.randint(1,10)
            score.append(num)
            print("you rolled:",num)
        elif user_input=='n':
            print("Thanks for playing!!")
            break
        else:
            print("Invalid output!")
    print("You have used all 5 rolls!")
    print("\nyou scored points:",sum(score))
    print(f"\ncurrent scores: player1:",sum(score),"Player2:",sum(score2))
    print("\nPlayer 2's turn")
    while True:
        for i in range(5):
            user_input2=input("\nRoll the dice(y/n):")
            if user_input2=='y':
                num2=random.randint(1,10)
                score2.append(num2)
                print("you rolled:",num2)
            elif user_input2=='n':
                print("\nThanks for playing!!")
                break
            else:
                print("Invalid output!")
        print("You have used all 5 rolls!")
        print("\nyou scored points:",sum(score2))
        print("\ncurrent scores:player1:",sum(score),"Player2:",sum(score2))

        if sum(score)==sum(score2):
            print("Tie! Try Again")
        elif sum(score)>sum(score2):
            print("Player 1 won!")
        elif sum(score)<sum(score2):
            print("Player 2 won!")