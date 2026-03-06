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
            print(f'current num {num}')
            result+=board_position[num]
            if board_position[num] == ' ':
                empty_square_location = num
            print(empty_square_location)
            #print(result,len(result))
        if result.count('X') == 2 and empty_square_location >=0:
            print(f'Move is {empty_square_location}')
            return(empty_square_location)
    
    else:
        return "None Found"     

board_position = ['0','X','X','X',' ','0',' ',' ',' ']
find_must_block()
