import random

board = [[1,2,3],[4,5,6],[7,8,9]]
cellsd = {
    1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1),
    9:(2,2)
    }

row_sep = "+-------+-------+-------+"
cols, rows = (3,3)

def display_board(brd):
    print(row_sep)
    for i in range(3):
        print(f"|       |       |       |\n|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |\n|       |       |       |")
        print(row_sep)
    return ""
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    

def enter_move():
    global board
    valid_flag = False
    while valid_flag == False:
        choice = int(input("Choose an empty space on the board: "))
        if choice < 0 or choice > 9:
            print("Invalid choice, please select free space.")
            valid_flag = False
        elif choice not in make_list_of_free_fields(board):
            print("Already used space, please select free space.")
            valid_flag = False
        else:
            q, r = cellsd[choice]
            board[q][r] = player
            valid_flag = True
                
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(brd):
    global board, freespaces
    freespaces = []
    for i in range(cols):
        for j in range(rows):
            if board[i][j]==player or board[i][j]==comp:
                continue
            else:
                freespaces.append(board[i][j])
    return freespaces


def victory_for(brd, sign):
    global board
    make_list_of_free_fields(brd)
    for i in range(3):
        #Checks rows, columns, l2r diag, and r2l diag
        if (brd[i][0]==brd[i][1]==brd[i][2])or\
           (brd[0][i]==brd[1][i]==brd[2][i])or\
           (brd[0][0]==brd[1][1]==brd[2][2])or\
           (brd[0][2]==brd[1][1]==brd[2][0]):
            if sign==player:
                print("Congrats, you won!!")
            else:
                print("Sorry, you lost :( ")
            return True
        else:
            return False
    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move():
    global board
    freelist = make_list_of_free_fields(board)
    random_pick = random.choice(freelist)
    q, r = cellsd[random_pick]
    board[q][r] = comp
    
    # The function draws the computer's move and updates the board.

player = "O"
comp = "X"
board[1][1] = comp


print("Computer is X's and you are O's,\n")

while True:
    print(display_board(board))
    make_list_of_free_fields(board)
    if len(freespaces)==0:
        print("No winners today, it's a tie!")
        break
    elif victory_for(board, comp):
        break
    elif victory_for(board, player):
        break
    else:
        enter_move()
        if victory_for(board,player):
            break
        draw_move()
        continue
    

