XO = ['#','X','O','X','O','X','O','X','O','X']
display=['0','1','2','3','4','5','6','7','8','9']
play=['_','_','_','_','_','_','_','_','_','_']
# print a display board
def display_board(board):
    print('This is the display board')
    print(board[1]+'/'+board[2]+'/'+board[3])
    print(board[4]+'/'+board[5]+'/'+board[6])
    print(board[7]+'/'+board[8]+'/'+board[9])

display_board(display)

print('_ _ _')

#display player board
def play_board(board):
    print('This is the current board')
    print(board[1]+'/'+board[2]+'/'+board[3])
    print(board[4]+'/'+board[5]+'/'+board[6])
    print(board[7]+'/'+board[8]+'/'+board[9])

play_board(play)





empty='_'
#set marker location
def place_marker(board, value):
    move=int(input("Where would you like to place your marker X?"))
    while move<1 or move>9:
        print('Please enter proper value')
        move=int(input("Where would you like to place your marker X?"))
    if play[move] is empty:
        play[move]='X'
        display[move]='X'
    print(play)
    display_board(play)

place_marker(play,1)
print(play)


def win()
    if display[1][2][3]='X'
    print('X has won')
