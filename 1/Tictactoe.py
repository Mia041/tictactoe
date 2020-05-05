# print a display board
def display_board(board):
    print('This is the current board')
    print(board[1]+'/'+board[2]+'/'+board[3])
    print(board[4]+'/'+board[5]+'/'+board[6])
    print(board[7]+'/'+board[8]+'/'+board[9])


#Ask player to choose marker and order to play.



def win(board):
    #check if row wins
    for i in range(1,8,3):
        if board[i]==board[i+1]==board[i+2] in 'XO' :
            return True
    #check if column wins
    for i in range(1,4):
        if board[i]==board[i+3]==board[i+6] in 'XO' :
            return True
    #check diagonal
    if board[1]==board[5]==board[9] or board[3]==board[5]==board[7]:
        return True
    return False

#set mark location
def place_marker(mark, board):
    move=input("Where would you like to place "+ mark+'?' )
    while int(move) not in range(1,10):
        print('Please enter proper value')
        move=input("Where would you like to place "+ mark+'?' )
    board[int(move)]=mark
    print(board)
    display_board(board)

#place_marker(display,1)


def full(board):
    for i in range(1,10):
        if board[i] not in 'XO':
            return False
    return True


def game_on():
    display=['#','1','2','3','4','5','6','7','8','9']
    print('Welcome to Tic Tac Toe!')
    Player_1=input("You are now Player_1. Do you want to be 'X' or 'O'?(Enter 'X' or 'O'): ").upper()
    while Player_1.upper() not in 'XO':
        Player_1=input("You are now Player_1. Do you want to be 'X' or 'O'?(Enter 'X' or 'O'): ").upper()
    if Player_1.upper()=='X':
        Player_2='O'
    else:
        Player_2='X'
    print('Player_1 is '+ Player_1.upper())
    print('Player_2 is ' + Player_2.upper())
    while not full(display):
        if Player_1=='X':
            place_marker('X', display)
            if win(display):
                print('X has won')
                break
            Player_1='O'

        elif Player_1=='O':
            place_marker('O', display)
            if win(display):
                print('O has won')
                break
            Player_1='X'
    if not win(display) :
        print('Tie game')
    play_again = input('Would you like to play again?')
    if play_again.upper() == 'YES':
        game_on()


game_on()
