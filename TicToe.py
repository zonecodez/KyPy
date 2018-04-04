# Specifically for the iPython Notebook environment for clearing output.
from IPython.display import clear_output

# Global variables
board = [' '] * 10
game_state = True
announce = ''

#################################################

# Note: Game will ignore the 0 index
def reset_board():
    global board,game_state
    board = [' '] * 10
    game_state = True

#################################################


def display_board():
    ''' This function prints out the board so the numpad can be used as a reference '''
    # Clear current cell output
    clear_output()
    # Print board
    print ("  "+board[7]+" |"+board[8]+" | "+board[9]+" ")
    print ("------------")
    print ("  "+board[4]+" |"+board[5]+" | "+board[6]+" ")
    print ("------------")
    print ("  "+board[1]+" |"+board[2]+" | "+board[3]+" ")

######################################################

def win_check(board, player):
    ''' Check Horizontals,Verticals, and Diagonals for a win '''
    if (board[7]  ==  board[8] ==  board[9] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[7] ==  board[4] ==  board[1] == player) or \
        (board[8] ==  board[5] ==  board[2] == player) or \
        (board[9] ==  board[6] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player) or \
        (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False


############################################################

def full_board_check(board):
    ''' Function to check if any remaining blanks are in the board '''
    if " " in board[1:]:
        return False
    else:
        return True


############################################################

#def makeMark():
 #   '''Function to allow players to choose X or O '''
  #  markX = str(input("Player1 choose your"))




##############################################################

def ask_player(mark):
    ''' Asks player where to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your: ' + mark+'. \nThe spaces are mapped to a number pad, with the bottom left being 1, the middle left being 4 and the top left being 7.'
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("\nSorry, please input a number between 1-9.")
            continue

        if choice not in range(1, 10):
            print("\nSorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("\nThat space isn't empty!")
            continue


################################################################

def player_choice(mark):
    global board, game_state, announce
    # Set game blank game announcement
    announce = ''
    # Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    # Check for player win
    if win_check(board, mark):
        clear_output()
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False

    # Show board
    clear_output()
    display_board()

    # Check for a tie
    if full_board_check(board):
        announce = "Tie!"
        game_state = False

    return game_state, announce


################################################################

def play_game():
    reset_board()
    global announce
    global count

    # Set marks
    X = 'X'
    O = 'O'

    # Set count
    count = 0
    while True:
        # Show board
        clear_output()
        if count == 0:
            display_board()


        # Player X turn
        game_state, announce = player_choice(X)
        print(announce)
        count = 1
        if game_state == False:
            break

        # Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

    # Ask player for a rematch
    rematch = input('Would you like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print("\nThanks for playing!")

################################################

play_game()
