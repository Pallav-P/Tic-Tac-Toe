#FuriousXcaliber
#7-26-2021
#I realize that checking for valid input in the ask_move() section will probably be better than checking with additional if statements in the write() section, but for now Ill keep it as it is. 
from main import new_game



if __name__ == "__main__": 
    print("This file is not supposed to be run. Please run the main file.")
    x = input("\n\nPress Enter to continue...")


def display_board(board):
    for row in board:
        for col in row:
            print(col, end = '')
        print('')
    print('')

def create_board():
    return [
        [" 1 ", " 2 ", " 3 "],
        [" 4 ", " 5 ", " 6 "],
        [" 7 ", " 8 ", " 9 "]
        ]

def write(board, play, loc):
    if loc <= 0:
        x = int(input("Enter a correct location: "))
        write(board, play, x)
    
    elif (loc <= 3):
        if(board[0][loc-1] == ' X ' or board[0][loc-1] == ' O '):
            x = int(input("Enter a correct location: "))
            write(board, play, x)
        else:
            board[0][loc-1] = play

    elif ( loc <= 6):
        if(board[1][loc-1 - 3] == ' X ' or board[1][loc-1 - 3] == ' O '):
            x = int(input("Enter a correct location: "))
            write(board, play, x)
        else:
            board[1][loc-1 - 3] = play

    elif ( loc <= 9):
        if(board[2][loc-1 - 6] == ' X ' or board[2][loc-1 - 6] == ' O '):
            x = int(input("Enter a correct location: "))
            write(board, play, x)
        else:
            board[2][loc-1 -6] = play
        
    else:
        x = int(input("Enter a correct location: "))
        write(board, play, x)

def ask_move(player):
    loc = int(input(" Player{}Enter the number where you want to put your mark: ".format(player)))
    return loc


def turn(move):
    if(move % 2 == 1):
        return ' X ', move + 1
    else:
        return ' O ', move + 1


def game(board, move = 1, win = False):
    while win ==False and move <= 9:
        player, move = turn(move)
        play = ask_move(player)
        write(board, player, play)
        display_board(board)
        if move > 5:
            win = check_victory(board) #check for victory after x(first player) could have player 3 moves | Prior to which checking is useless
    if win == False and move == 10:
        print("It was a draw")
    else:
        print("Player{}has won the game".format(player))
    print('')
    new_game()        
       

def check_victory(board):
    for x in range(0,3):
        if (board[0][x] == board[1][x] == board[2][x]):
            return True
        elif (board[x][0] == board[x][1] == board[x][2]):
            return True
        elif (board[0][0] == board[1][1] == board[2][2]):
            return True
        elif (board[2][0] == board[1][1] == board[0][2]):
            return True
    return False

def introduction():
    print('''


                        Created by Pallav Pant




To play the game just enter the number in the location of your choice and press enter.



    ''')

