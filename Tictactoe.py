board = ['#','X','O','X','O','X','O','X','O','X']
# print a display board
def display_board(board):

    print(board[1]+board[2]+board[3]+'\n'+board[4]+board[5]+board[6]+'\n'+board[7]+board[8]+board[9])

display_board(board)




#Ask player to choose marker and order to play.
def player_input():
    tic=input("You are now Player_1. Do you want to choose 'X' or 'O'?(Enter 'X' or 'O'):")
    while tic.upper() != 'X' or 'O':
        tic=input("You are now Player_1. Do you want to choose 'X' or 'O'?(Enter 'X' or 'O'):")
    if tic=='X':
        tac=='O'
    else:
        tac=='X'
    print('Player_1 is '+ tic.upper())
    print('Player_2 is' + tac.upper())

player_input()



#set marker location
def place_marker(board, value):
    move=int(input("Where would you like to place your marker X?"))
    board[int(move)]='X'
    display_board()

place_marker()



def input1(eg):
    return display_board(board[int(eg)])
