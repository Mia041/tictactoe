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


def win():
    column_1=[1,4,7]
    column_2=[2,5,8]
    column_3=[3,6,9]
    for i in column_1:
        if display[i]==display[i+1]==display[i+2] in 'XO' :
            print('X has won')
    for i in column_2:
        if display[i]==display[i-1]==display[i+1] in 'XO':
            print('X has won')
    for i in column_3:
        if display[i]==display[i-2]==display[i-3] in 'XO':
            print('X has won')
win()




empty='_'
#set mark location
def place_marker(board, value):
    move=input("Where would you like to place your mark X?")
    while int(move) not in range(1,10):
        print('Please enter proper value')
        move=input("Where would you like to place your mark X?")
    if display[int(move)] in 'XO':
        print('This place is full, please choose another position')
    elif display[int(move)] in range(9):
        display[int(move)]='X'
    print(display)
    display_board(display)

#place_marker(display,1)
#print(display)


def place_marker_again():
    while range(10) in display[1:]:
        place_marker(display,1)



#game on
while range(10) in display():
    place_marker(display,1)
    win()
    print(display)
