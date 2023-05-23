import random

def display_board(board):
    print(' | | ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | | ')
    print('-----')
    print(' | | ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | | ')
    print('-----')
    print(' | | ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | | ')

def player_input():
    marker = ''
    # KEEP ASKING PLAYER 1 TO CHOOSE X or O

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, chose X or O: ').upper()
    
    # ASSIGN PLAYER 2, the opposite marker
    

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

    return (player1,player2)

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, mark):
    # WIN TIC TAC TOE?

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '
# test_board = ['#','X','O','X','O','X','O','X','O','X']

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    #  BOARD IS FULL IS WE RETURN TRUE
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))

    return position

def replay():
    choice = input("Play again? Enter Yes or No")

    return choice == "Yes"

print("Welocome to tic tac toe")

while True:

    # PLAY THE GAME
    # # SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## GMAE play
    while game_on:
        if turn == 'Player 1':

            #Show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on =False
                else:
                    turn = 'Player 2'
        else:
            #Show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on =False
                else:
                    turn = 'Player 1'

        ### PLAYER ONE TURN
    if not replay():
        break
    ### PLAYER ONE TURN








# display_board(test_board)

# player1_marker, player2_marker = player_input()
# print(player1_marker,player2_marker)

# place_marker(test_board, '$', 8)
# display_board(test_board)

display_board(test_board)
test = win_check(test_board, 'X')
print(test)