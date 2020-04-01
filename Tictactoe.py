XO = ['#','X','O','X','O','X','O','X','O','X']
display=['#','1','2','3','4','5','6','7','8','9']
play=['_','_','_','_','_','_','_','_','_','_']
# print a display board
def display_board(board):
    print('This is the current board')
    print(board[1]+'/'+board[2]+'/'+board[3])
    print(board[4]+'/'+board[5]+'/'+board[6])
    print(board[7]+'/'+board[8]+'/'+board[9])

display_board(display)

print('_ _ _')


#Ask player to choose marker and order to play.
def player_input():
    Player_1=input("You are now Player_1. Do you want to be 'X' or 'O'?(Enter 'X' or 'O'): ").upper()
    while Player_1.upper() not in 'XO':
        Player_1=input("You are now Player_1. Do you want to be 'X' or 'O'?(Enter 'X' or 'O'): ").upper()
    if Player_1.upper()=='X':
        Player_2='O'
    else:
        Player_2='X'
    print('Player_1 is '+ Player_1.upper())
    print('Player_2 is ' + Player_2.upper())

player_input()




def win():
    column_1=[1,4,7]
    column_2=[2,5,8]
    column_3=[3,6,9]
    for i in column_1:
        if display[i]==display[i+1]==display[i+2] in 'XO' :
            return True
    for i in column_2:
        if display[i]==display[i-1]==display[i+1] in 'XO':
            return True
    for i in column_3:
        if display[i]==display[i-2]==display[i-3] in 'XO':
            return True
    for i in display:
        if display[1]==display[5]==display[9] or display[3]==display[5]==display[7]:
            return True
win()





empty='_'
#set mark location
def place_marker(mark):

    move=input("Where would you like to place your mark? "+ mark )
    while int(move) not in range(1,10):
        print('Please enter proper value')
        move=input("Where would you like to place your mark? "+ mark )
    display[int(move)]=mark
    print(display)
    display_board(display)
#place_marker(display,1)




def full(board):
    for i in range(1,10):
        if board[i] not in 'XO':
            return False
    return True

print(full(display))



def game_on():
    print('Welcome to Tic Tac Toe!')
    count=0
    global Player_1
    global Player_2
    while count<9:
        if Player_1=='X':
            place_marker(X,1)
            count+=1
            if win() is True:
                return 'One player has won'
                break
                print('Would you like to play again? ')
            Player_1='O'
        elif Player_1=='O':
            place_marker(O,1)
            if win() is True:
                return 'One player has won'
                break
                print('Would you like to play again? ')
                count+=1
                Player_1='X'

    if win() is false:
        input('Tie game.Would you like to play again?')

game_on()
while input('Tie game.Would you like to play again?')=='YES':
        '\n''\n'
        game_on()
