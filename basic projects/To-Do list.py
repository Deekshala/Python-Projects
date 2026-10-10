task=[]
print("TO-DO LIST MENU:")
print("1. Add task")
print("2. Remove task")
print("3. View task")
print("4. Exit")
while True:
    user=int(input("Enter you choice: "))
    if user==1:
        add_task=input("Enter your task: ")
        task.append(add_task)
    elif user==2:
        print(task)
        remove_task=int(input("which task do you want to remove? : "))
        task.pop(remove_task-1)
    elif user==3:
        print(task)
    elif user==4:
        print("Exit")
        break
    else:
         print("Invalid choice")
