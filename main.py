#0305-2026 - TJS redoing this simple game as an exercise
#0309-2026  - Completed

#inital position is empty list
board_position = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#map squares to help user visualize
board_map = [num for num in range(0,10)]
#tic tac toe has 8 rows, columns, diagnols
SQUARE_GROUPS=[[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def display_board(input):
    board = f'{input[0]} |{input[1]}|{input[2]} \n'
    board += f'{input[3]} |{input[4]}|{input[5]} \n'
    board += f'{input[6]} |{input[7]}|{input[8]} \n'
    print(board)

def validate_user_move(input):
    try:
        move = board_position[int(input)]
    except IndexError:
        print("You have typed an invalid number please use 0-8")
        return False
    except ValueError:
        print("You must use number 0-8 please")
        return False
    if move== ' ':
        return True
    else:
        print("Square occupied, please try again")
        return False

def users_turn():
    while True:
        user_current_move = input('Where do you want to move?')
        print(f'Checking square: {user_current_move}')
        if validate_user_move(user_current_move)== True:
            board_position[int(user_current_move)] = 'X'
            display_board(board_position)
            return True

def computers_turn():
    found_move = False
    # Look for 1.chance to win 2.prevent opponent win
    temp = find_win_or_block()
    if  temp != 'None Found':
        board_position[temp] = '0'
        found_move = True
    else:
        # if no WIN or BLOCK try center , corners, all others
        key_squares =[4,0,2,6,8,1,3,5,7]
        for square in key_squares:
            if board_position[square] == ' ':
                board_position[square] = '0'
                found_move = True
                break
    display_board(board_position)
    return found_move

def is_game_over():
    if board_position.count(' ')==0:
        print('Game over.Tie this time.')
        return True
    for group in SQUARE_GROUPS:
        #iterate thr. all rows, columns, diagonals [r/c/d]
        result=''
        for num in group:
            result+= board_position[num]
            # if result =XXX or 000 game over!
        if result == 'XXX':
            print('Human has won, AI will win next time, enjoy \
                your temporary victory')
            return True
        elif result == '000':
            print('Technology has won. WOOT! ')
            return True  
    return False
             
def find_win_or_block():
    ''' find square to WIN or must be played to BLOCK opponent's win '''

    for group in SQUARE_GROUPS:
        #iterate thr. all rows, columns, diagonals [r/c/d]
        result=''
        empty_square_location = -1 
        for num in group:
            result+=board_position[num]
            if board_position[num] == ' ':
                empty_square_location = num
        # result is a three character string representing a r/c/d
        # - check for chance to WIN 
        if result.count('0') == 2 and empty_square_location >=0:
            print(f'Move is {empty_square_location}')
            return(empty_square_location)
        # - check for chance to BLOCK
        elif result.count('X') == 2 and empty_square_location >=0:
            print(f'Move is {empty_square_location}')
            return(empty_square_location)
    else:
        return "None Found"     
            
#Start Game
game_over = False
play = input('Do you want to play y or n ?\n')
if play.upper() == 'Y':
    print('These are the current location mappings')
    display_board(board_map)
    while not game_over:
        if users_turn() == True:
            game_over = is_game_over()
            if not game_over:
                print('computer now moves')
        if computers_turn() == True:
            game_over = is_game_over()
            if not game_over:
                print('your move again')
        

        