from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print_line(True)
    print_row(board[0])
    print_line(True)
    print_row(board[1])
    print_line(True)
    print_row(board[2])
    print_line(False)

def print_blank():
    print("|       |       |       |")

def print_line(blank):
    print("+-------+-------+-------+")
    if blank:
        print_blank()

def print_row(row):
    print("|   " + row[0] +"   |   " + row[1] + "   |   " + row[2] + "   |")
    print_blank()

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid = False
    while not valid:
        try:
            move = int(input("Enter your move: "))
        except KeyboardInterrupt:
            break
        except:
            print("You must enter a number.")

        if move < 1 or move > 9:
            print("Enter a number 1 through 9.")
        elif not is_valid_move(board, move):
            print("You must choose a free space.") 
        else:
            valid = True

    coords = get_coords(move)
    board[coords[0]][coords[1]] = 'O'
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for column in range(3):
            space = board[row][column]
            if space != 'O' and space != 'X':
                free_fields.append((row, column,))

    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    victory = False
    winners =[[1,2,3], [4,5,6], [7,8,9],
               [1,4,7], [2,5,8], [3,6,9],
               [1,5,9], [3,5,7],]
    
    for group in winners:
        did_win = []
        for number in group:
            coords = get_coords(number)
            did_win.append(board[coords[0]][coords[1]])
        if did_win == [sign, sign, sign]:
            victory = True
            break

    if victory:
        print(sign, "Wins!")
    elif len(make_list_of_free_fields(board)) == 0:
        print("Draw!")
        victory = True 

    return victory        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid = False
    while not valid:
        move = randrange(1,10)    
        valid = is_valid_move(board, move)
    
    coords = get_coords(move)
    board[coords[0]][coords[1]] = 'X'

def is_valid_move(board, number):
    free_fields = make_list_of_free_fields(board)
    space = get_coords(number)

    return space in free_fields

def get_coords(number):
    if number < 4:
        row = 0
    elif number < 7:
        row = 1
    else:
        row = 2
    
    column = number - (3 * row) - 1

    space = (row, column,)

    return space

board = [['1', '2', '3'],['4', 'X', '6'],['7', '8', '9']]
exit = False

while exit == False:
    display_board(board)
    enter_move(board)
    exit = victory_for(board, 'O')
    if exit:
        break
    draw_move(board)
    exit = victory_for(board, 'X')
display_board(board)
