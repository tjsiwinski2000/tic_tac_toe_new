#0305-2026 - TJS redoing this simple game as an exercise
# - need to rename find_must_block -> find_two_in_row (which_side)
# - - a. find_best_move find_two_in_row('0'),find_two_in_row('X')
# - - b. did anyone win or no moves left

board_position = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
board_map = [num for num in range(0,10)]
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
    # look for two in a row that muct be BLCOKED
    temp = find_must_block()
    if  temp != 'None Found':
        board_position[temp] = '0'
        found_move = True
    else:
        # if nothing to block try center , corners, all others
        key_squares =[4,0,2,6,8,1,3,5,7]
        for square in key_squares:
            if board_position[square] == ' ':
                board_position[square] = '0'
                found_move = True
                break
    display_board(board_position)
    return found_move

        
def find_must_block():
    ''' tic tac toe has 8 rows, columns, diagnols
    find square that must be played to block opponent 
    '''
    square_groups= [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],\
                    [0,4,8],[2,4,6]]
    for group in square_groups:
        print(f"group is {group}")
        result=''
        empty_square_location = -1 
        for num in group:
            # print(f'current num {num}')
            result+=board_position[num]
            if board_position[num] == ' ':
                empty_square_location = num
            # print(empty_square_location)
            #print(result,len(result))
        if result.count('X') == 2 and empty_square_location >=0:
            print(f'Move is {empty_square_location}')
            return(empty_square_location)
    
    else:
        return "None Found"     
            
#Start Game
play = input('Do you want to play y or n ?\n')
if play.upper() == 'Y':
    print('These are the current location mappings')
    display_board(board_map)
    while True:
        if users_turn() == True:
            print('computer now moves')
        if computers_turn() == True:
            print('your move again')
        

        