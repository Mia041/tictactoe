ls = ['#','X','O','X','O','X','O','X','O','X']
def display_board():

    print(ls[1]+ls[2]+ls[3]+'\n'+ls[4]+ls[5]+ls[6]+'\n'+ls[7]+ls[8]+ls[9])

display_board()





def player_input():
    tic=input("Do you want to be 'X' or 'O'?(Enter 'X' or 'O'):")
    while tic not in'XOxo':
        tic=input("Do you want to be 'X' or 'O'?(Enter 'X' or 'O'):")
    print('Excellent, you are now'+ tic.upper())

    tac=input('Do you want to go first?')
    while tac!='yes':
           tac=input('Do you want to go first?')
    print('Excellent! You are now Player1')

player_input()


def place_marker():
    player_input1=input("Where would you like to place your marker X?")
    ls[]='X'
    display_board()

place_marker()
