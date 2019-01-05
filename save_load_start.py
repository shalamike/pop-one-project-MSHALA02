import random
import json
from three_musketeers import *


def save(): # this function saves the board in its current state so user can continue game at a later time

    current_board = get_board()
    """
    these next two lines writes the board onto a text file as a filehandle,
    so that the file will open as a nested list (which the board is) rather than a string.
    """
    with open("currentgame.txt", "w") as filehandle:
        json.dump(current_board, filehandle)

        print("game successfully saved")

    #this functin creates a save file as a text file using json.dump

def load(): # this function loads the game so that the user can continue a previously running game

    """
    these next two lines opens the board as a file handle. as previously stated in the save function,
    this is to ensure that the board opens up as a nested list.
    """

    with open ("currentgame.txt", "r") as filehandle:
        current_board = json.load(filehandle)
    """
    the following lines where mostly copied (apeart from the set board function) from the start() function on the main three_musketeers.py file.
    this is to ensure that the game will run from the user once they load their current game. 
    """
    set_board(current_board)
    print_board()
    users_side = choose_users_side()

    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

