print("player 0's turn")
board=[" "for i in range(10)]
def display_board():
        print(f"{board[1]} | {board[2]} | {board[3]}")
        print("--+--+--")
        print(f"{board[4]} | {board[5]} | {board[6]}")
        print("--+--+--")
        print(f"{board[7]} | {board[8]} | {board[9]}")

user=int(input("enter row(0-2): "))
user2=int(input("enter column(0-2): "))
position=user*3+user2
if board[position]==" ":
    board[position]="o"
    display_board()


def display_board():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--+--+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+--+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")

print("player x's turn")
x_user=int(input("enter row(0-2): "))
x_user2=int(input("enter column(0-2): "))
position2=x_user*3+x_user2
if board[position2]==" ":
    board[position2]="x"
    display_board()