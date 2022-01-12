#FuriousXcaliber
#7-26-2021

import my_func

def main():
    my_board = my_func.create_board()
    my_func.display_board(my_board)
    my_func.game(my_board)




def new_game():
    y_or_n = input("Do you want to play Tic-Tac-Toe? y/n: ")

    if y_or_n == 'y' or y_or_n == 'Y':
        main()
    elif(y_or_n == 'n' or y_or_n == 'N'):
        print("Thank You")
    else:
        print("Please enter a valid argument.")
        new_game()


if __name__ == "__main__":
    my_func.introduction()
    new_game()
