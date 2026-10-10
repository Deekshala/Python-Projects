sum=0
print("question 1: what is the capital of france?")
print("a)Paris")
print("b) London")
print("c) Rome")
user=input("your answer: ")
if user=='a':
        print("Correct!")
        sum=+1
elif user=='b' or user=='c':
    print("Wrong answer!")
else:
    print("Invalid option")

print("question 2: what is the largest planet in our solar system?")
print("a)Earth")
print("b) Jupiter")
print("c) Mars")

user2=input("your answer: ")
if user2=='b':
        print("Correct!")
        sum=sum+1
elif user=='a' or user=='c':
    print("wrong answer!")
else:
    print("Invalid option")


print("your final score:",sum)
