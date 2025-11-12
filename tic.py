import random
# The board list (Index 0 is ignored)
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def display_board(board):
    # --- YOUR CODE GOES HERE ---
    print("Welcome to TIC TAC TOE")
    # 1. Print the top row (indices 7, 8, 9)
    print(board[1],"|",board[2],"|",board[3])
    print("---------")
    print(board[4],"|",board[5],"|",board[6])
    print("---------")
    print(board[7],"|",board[8],"|",board[9])

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Horizontal Top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # Horizontal Middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or # Horizontal Bottom
            
            (board[1] == mark and board[4] == mark and board[7] == mark) or # Vertical Left
            (board[2] == mark and board[5] == mark and board[8] == mark) or # Vertical Middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or # Vertical Right
            
            (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal Top-Left to Bottom-Right
            (board[3] == mark and board[5] == mark and board[7] == mark)    # Diagonal Top-Right to Bottom-Left
           )
def draw_check(board):
    if not win_check(board, "X") and not win_check(board, "O"):
        if not (" " in board):
            return True
        else:
            retur 
def play_game():
    user=random.randint(1,2)
    #USER INPUT
    while True:
        player_mark="X" if user==1 else "O"
        print(f"PLAYER{user} ({player_mark}) : Enter your move (1-9): ")
        try:
            move = int(input())
            if move in range(1,10):
                if board[move]==" ":
                    board[move] = player_mark
                    display_board(board)
                    if win_check(board,player_mark):
                        print(f"CONGRATS! PLAYER {user} ({player_mark}) YOU WON THE MATCH ")
                        break
                    elif draw_check(board):
                        print("OH DEAR! \nIT'S A DRAW")
                        break
                    else:
                        user=2 if user==1 else 1
                        continue
                else: 
                    print("Invalid Move! Place is occupied")
                    continue
            else:
                print("Invalid move! use only numbers from range (1-9)")
                continue
        except:
            print("Invalid move! use only numbers from range (1-9)")
            continue
if __name__=="__main__":
    play_game()