while True:
        user=input("Enter a password:")
        if user=="":
            print("Invalid Input!")
        elif len(user)>=8:
            print("password strenght:strong")
            break
        elif len(user)>=5:
            print("password strenght:medium")
        else:
            print("password strenght:weak")