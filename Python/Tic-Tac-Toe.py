'''
# This program will allow two players to play Tic-Tac-Toe on a 3x3 grid with each space defined
# by rows A, B, C and columns 1, 2, 3 as shown:
#
#    1  2  3
# A    |  |
#    ---------
# B    |  |
#    ---------
# C    |  |
#
# Players enter a position (e.g. A1) and the program alternately places X's or O's
#
# Win condition is 3 in a row either vertically, horizontally, or diagonally
'''


'''
Set up the environment and global variables
'''

# import functions to be used
from IPython.display import clear_output


# First set up the dictionary that will hold the values and place blanks in the spaces
# so that it prints correctly. This would probably be easier using a list but demoing
# dictionary use here
my_board = {'A': {'1': '   ','2': '   ','3': '   '},
            'B': {'1': '   ','2': '   ','3': '   '},
            'C': {'1': '   ','2': '   ','3': '   '}}

play_game = True       # for at the end, if want to play again
continue_game = True   # for within the loop of playing the game

# player default values
player = ''
upnext = ''

nplays = 0        # set initial number of plays to zero, used for checking win/tie conditions

def clearboard():
    ''' Function to clear the board for new game '''
    #global my_board, play_game, nplays
    my_board = {'A': {'1': '   ','2': '   ','3': '   '},
            'B': {'1': '   ','2': '   ','3': '   '},
            'C': {'1': '   ','2': '   ','3': '   '}}
    nplays = 0
    return my_board,nplays

def printboard(my_board):
    ''' Print the board to the screen '''
    clear_output()
    row1 = 'A '+str(my_board['A']['1'])+'|'+str(my_board['A']['2'])+'|'+str(my_board['A']['3']+'\n')
    row2 = 'B '+str(my_board['B']['1'])+'|'+str(my_board['B']['2'])+'|'+str(my_board['B']['3']+'\n')
    row3 = 'C '+str(my_board['C']['1'])+'|'+str(my_board['C']['2'])+'|'+str(my_board['C']['3']+'\n')
    top =     '    1   2   3 \n'
    divider = '  -----------\n'

    print(top,row1,divider,row2,divider,row3)

def start():
    '''
    Start the game
    Returns a tuple with (Player 1, Player 2) choice of X and O
    '''
    print('Welcome to Tic-Tac-Toe!')

    player = ''

    while player != 'X' and player != 'O':
        player = input('Will X or O go first? ').upper()
        if player != 'X' and player != 'O':
            print('Enter X or O please')

    print('Here is your starting board:')

    if player == 'X':
        return ('X', 'O')
    elif player == 'O':
        return ('O', 'X')

def getplay(my_board,nplays,upnext,player):
    '''Get the next play'''

    #Define the sets of acceptable row and column values:
    rowvals = set(['A', 'B', 'C'])
    colvals = set(['1','2','3'])

    # Read play & check validity
    print('It is', player,'\'s turn')

    while True:
        play = input('Enter your play: ')
        row = play[0].upper()  # Row values must be A, a, B, b, or C, c
        col = play[1]          # Column values must be 1, 2 or 3

        if row not in rowvals and col not in colvals:
            # Check for correct format
            print('Please enter in the correct format, e.g. A1 or a1')
            continue

        elif my_board[row][col] != '   ':
            # Check to make sure play is not on top of another play
            print('That is already on the board. Enter another choice, ',player)
            continue

        else:
            # Play is valid
            my_board[row][col] = ' '+player+' '  # assign the player's symbol to the board
            nplays += 1                          # update the number of plays
            # print('You have entered ', play)     # for debugging
            # player,upnext = upnext,player        # swap player and upnext symbols
            break

    return my_board,nplays,upnext,player

def checkwin(my_board, player, nplays):
    '''Check to see if the play wins'''

    # print('there have been ',nplays,' plays')  #for debugging

    if nplays < 5:      # Cannot win in less than 5 moves; no further checking needed
        return True     # game has not ended, continue_game = True

    elif(             # Check to see if the play wins
        #Horizontal Checks: (values in a given key are identical)
        (my_board['A']['1'] == my_board['A']['2'] == my_board['A']['3'] == ' '+player+' ') or  \
        (my_board['B']['1'] == my_board['B']['2'] == my_board['B']['3'] == ' '+player+' ') or  \
        (my_board['C']['1'] == my_board['C']['2'] == my_board['C']['3'] == ' '+player+' ') or  \
                                                                                               \
        #Vertical Checks: (values in all the keys, same index are identical)
        (my_board['A']['1'] == my_board['B']['1'] == my_board['C']['1'] == ' '+player+' ') or  \
        (my_board['A']['2'] == my_board['B']['2'] == my_board['C']['2'] == ' '+player+' ') or  \
        (my_board['A']['3'] == my_board['B']['3'] == my_board['C']['3'] == ' '+player+' ') or  \
                                                                                               \
        #Diagonal Checks:
        (my_board['A']['1'] == my_board['B']['2'] == my_board['C']['3'] == ' '+player+' ') or  \
        (my_board['A']['3'] == my_board['B']['2'] == my_board['C']['1'] == ' '+player+' ')):

        print(player, ' won!')
        return False     # game has ended, continue_game = False

    elif (nplays == 9):   #if didn't win and it's the 9th play, the board is full and it's a tie
        print('It\'s a tie!')
        return False     # game has ended, continue_game = False

    else:               # >= 5 plays but < 9 plays and did not win, game has not ended
        return True    # game has not ended, continue_game = True


def playagain():
    '''Check if want to play again'''

    answer = input('Would you like to play again? (y/n) ').lower()

    if answer == 'y':
        return True
    else:
        print('Thanks for playing!')
        return False


# Call the functions to play the game
while play_game == True:
    # set up the board
    my_board,nplays = clearboard()

    # ask for player symbol choice to start the game
    player, upnext = start()

    print('Great! Here is your starting board:')
    printboard(my_board)

    #print(player, 'is up and', upnext, 'is next')
    continue_game = True

    while continue_game:
        my_board,nplays,upnext,player = getplay(my_board, nplays, upnext, player) # get the current player's play & check to see if the play is valid
        printboard(my_board)                             # print the board with the new play marked
        continue_game = checkwin(my_board,player,nplays) # check to see if the win condition has been met
        player,upnext = upnext,player                    # swap player and upnext symbols

    play_game = playagain()             # ask if they want to play again
