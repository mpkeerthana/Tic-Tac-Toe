board=["1","2","3",
       "4","5","6",
       "7","8","9"]

def display_board():
    print()
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])
    print()

def check_winner():
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c]:
            return True
    return False

player="X"

for turn in range(9):
    display_board()
    position=int(input(f"Player {player}, enter your position (1-9): "))-1

    if position<1 or position>9 or board[position-1] in ["X","O"]:
        print("Invalid position. Try again.")
        continue

    board[position-1]=player

    if check_winner():
        display_board()
        print(f"Player {player} wins!")
        break

    if player=="X":
        player="O"
    else:
        player="X"

else:
    display_board()
    print("It's a tie!")