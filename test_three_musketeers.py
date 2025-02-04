import pytest
from three_musketeers import *
import random

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '_'
is_adjacent = (1,1)

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

#this board is a backup of the original one to be used after the make move tests as they will manipulate the original places on the board
board1a =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, R, _, M, _],
            [_, _, R, _, _],
            [_, R, M, R, _],
            [_, _, _, _, _],
            [R, _, _, _, M] ]

# board with no possible musketeer moves AND musketeer victory
board3 =  [ [R, _, R, _, M],
            [_, _, _, _, _],
            [_, _, M, _, R],
            [_, _, _, _, _],
            [R, _, R, _, M] ]

#board with no possible cardinal richleau moves
board4 =  [ [R, M, _, _, _],
            [M, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, M] ]

# boards with Cardinal Richlaeus victory
board5 =  [ [R, M, _, _, _],
            [_, M, _, _, _],
            [_, M, _, R, _],
            [_, _, _, _, _],
            [_, _, _, _, _] ]

board6 = [ [M, M, M, _, _],
           [R, _, _, _, _],
           [_, _, _, _, _],
           [_, _, R, _, _],
           [_, _, _, _, R] ]

board7 = [ [R, _, _, _, _],
           [M, _, M, _, M],
           [_, _, _, R, _],
           [_, _, _, _, _],
           [_, _, _, _, R] ]

board8 = [ [R, M, _, _, _],
           [_, _, _, R, _],
           [_, M, R, _, _],
           [_, M, _, _, _],
           [_, _, _, _, _] ]

#musketeers victory
board9 = [ [_, _, M, _, _],
           [M, _, _, _, R],
           [_, _, _, R, _],
           [R, _, R, _, _],
           [_, _, R, _, M] ]




def test_create_board():
    #eventually add at least two more test cases
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at ((2,1)) == R
    assert at ((2,2)) == M


def test_set_board():
    #eventually add some board2 and at least 3 tests with it
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at ((0,0)) == _
    assert at ((1,2)) == R
    assert at ((4,4)) == M



def test_get_board():
    # eventually add at least one more test with another board
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()
    set_board(board3)
    assert board3 == get_board()
    set_board(board4)
    assert board4 == get_board()


def test_string_to_location():
    ##eventually add at least one more exception test and two more
    ##test with correct inputs
    set_board(board1)
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('A0')
        string_to_location('F1')
    assert string_to_location('A1') == [0,0]
    assert string_to_location('B2') == [1,1]
    assert string_to_location('C4') == [2,3]


def test_location_to_string():
    ## Replace with tests
    ## Replace with tests
    with pytest.raises(ValueError):
        location_to_string((5,5))
        location_to_string((7,1))
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((2,3)) == 'C4'
    assert location_to_string((4,4)) == 'E5'

def test_at():
    # Replace with tests
    assert at((0,3)) == get_board()[0][3]
    assert at((4,0)) == get_board()[4][0]
    assert at((3,1)) == get_board()[3][1]
    #testing with strings
    set_board(board1)
    assert at((0,3)) == "M"
    assert at((4,0)) == "_"
    assert at((3,1)) == "R"


def test_all_locations():
    # Replace with tests
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]
    pass

def test_adjacent_location():

    assert adjacent_location((1,1), down) == (2,1)
    assert adjacent_location((3,3), left) == (3,2)
    assert adjacent_location((4,4), up) == (3,4)
    assert adjacent_location((2,2), right) == (2,3)
    # Replace with tests
    pass
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0), left)
        is_legal_move_by_musketeer((4,1), right)
    assert is_legal_move_by_musketeer((1,3),down) == True
    assert is_legal_move_by_musketeer((0,3), left) == False
    set_board(board2)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((4,3), down)
        is_legal_move_by_musketeer((3,4), up)
    assert is_legal_move_by_musketeer((2, 2), up) == True
    assert is_legal_move_by_musketeer((0,3), left) == False
    set_board(board3)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,3), left)
        is_legal_move_by_musketeer((2,1), right)
    assert is_legal_move_by_musketeer((0,4), left) == False
    assert is_legal_move_by_musketeer((4, 4), down) == False

    # Replace with tests
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,3), right)
        is_legal_move_by_enemy((4,4), left)
    assert is_legal_move_by_enemy((1,2), left) == True
    assert is_legal_move_by_enemy((2,1), right) == False
    set_board(board2)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((1,1), right)
        is_legal_move_by_enemy((2,2), down)
    assert is_legal_move_by_enemy((0,1), right) == True
    assert is_legal_move_by_enemy((2,3), left) == False
    set_board(board4)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((2,2), right)
        is_legal_move_by_enemy((4,4), down)
    assert is_legal_move_by_enemy((0,0), right) == False
    assert is_legal_move_by_enemy((0,0), down) == False

    # Replace with tests
    pass

def test_is_legal_move():

    set_board(board1)
    assert is_legal_move((4,3), right) == True
    assert is_legal_move((1,3),left) == True
    assert is_legal_move((2,3), up) == False
    assert is_legal_move((2,2), down) == False

    set_board(board2)
    assert is_legal_move((2,3), right ) == True
    assert is_legal_move((2,2), right) == True
    assert is_legal_move((1,2), down ) == False
    assert is_legal_move((4,4), up) == False




def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((4,3)) == True
    assert can_move_piece_at((3,1)) == True
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((0,3)) == False
    # Replace with tests
    set_board(board3)
    assert can_move_piece_at((0,4)) == False
    assert can_move_piece_at((2,2)) == False
    assert can_move_piece_at((4,4)) == False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere("M") == True
    assert has_some_legal_move_somewhere("R") == True
    set_board(board3)
    assert has_some_legal_move_somewhere("M") == False
    assert has_some_legal_move_somewhere("R") == True
    set_board(board4)
    assert has_some_legal_move_somewhere("M") == True
    assert has_some_legal_move_somewhere("R") == False
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,2)).sort() == [left, right, up].sort()
    assert possible_moves_from((3,1)).sort() == [left, right, down].sort()
    assert possible_moves_from((4,3)).sort() == [left, right, up].sort()
    assert possible_moves_from((1,3)).sort() == [left, down].sort()
    set_board(board2)
    assert possible_moves_from((4,0)).sort() == [right, up].sort()
    assert possible_moves_from((4,4)).sort() == [].sort()
    assert possible_moves_from((0,1)).sort() == [left, right, down].sort()
    set_board(board3)
    assert possible_moves_from((0,4)).sort() == [].sort()
    assert possible_moves_from((2,2)).sort() == [].sort()
    assert possible_moves_from((4,4)).sort() == [].sort()
    set_board(board4)
    assert possible_moves_from((0,0)).sort() ==[].sort()


    """
    skeleton code for testing possible moves
    
    assert possible_moves_from(())
    """

    # Replace with tests
    #pass

def test_is_legal_location():
    # Replace with tests
    # this test just sees if the person or computer who is playing is selecting a valid location from the board.
    # as it is just testing whether the location is valid, there is no need to set a board for this function
    assert is_legal_location((2,2)) == True
    assert is_legal_location((1,3)) == True
    assert is_legal_location((4,4)) == True
    assert is_legal_location((0,0)) == True
    assert is_legal_location((5,1)) == False
    assert is_legal_location((-2,7)) == False
    assert is_legal_location((3,-7)) == False
    assert is_legal_location((2,6)) == False

#    pass

def test_is_within_board():
    # Replace with tests
    # this just tests if the player who is moving a given piece will still remain within the board
    set_board(board1)
    assert is_within_board((1,2), left) == True
    assert is_within_board((4,3), left) == True
    assert is_within_board((0,3), up) == False
    assert is_within_board((4,3), down) == False
    set_board(board3)
    assert is_within_board((0,0), right) == True
    assert is_within_board((0,0), down) == True
    assert is_within_board((0,0), up) == False
    assert is_within_board((4,4), left) == True
    assert is_within_board((4,4), up) == True
    assert is_within_board((4,4), down) == False
    assert is_within_board((4, 4), right) == False

    #pass

def test_all_possible_moves_for1():
    # Replace with tests
    #pass
    set_board(board1)
    assert set(all_possible_moves_for(M)) == set([((1, 3), left), ((1, 3), down), ((2, 2), left), ((2, 2), up), ((2, 2), right)])
    assert set(all_possible_moves_for(R)) == set([((1, 2), left), ((1, 2), up), ((2, 1), left), ((2, 1), up), ((2, 3), down), ((2, 3), right), ((3, 1), left), ((3, 1), right), ((3, 1), down), ((4, 3), left), ((4, 3), right), ((4, 3), up)])
    set_board(board3)
    assert set(all_possible_moves_for(M)) == set([])
    assert set(all_possible_moves_for(R)) == set([((0,0), down),((0,0), right), ((0,2), left),((0,2), down), ((0,2), right), ((2,4), up), ((2,4), left), ((2,4), down), ((4,0), up), ((4,0), right), ((4,2), left), ((4,2), up), ((4,2), right)])
    set_board(board4)
    assert all_possible_moves_for(M) == [((0,1), left), ((1,0), up)]


def test_make_move():

    set_board(board1a)
    make_move((2,2), up)
    assert board1a == [ [_, _, _, M, _],
                        [_, _, M, M, _],
                        [_, R, _, R, _],
                        [_, R, _, _, _],
                        [_, _, _, R, _] ]

    make_move((4, 3), left)
    assert board1a == [ [_, _, _, M, _],
                        [_, _, M, M, _],
                        [_, R, _, R, _],
                        [_, R, _, _, _],
                        [_, _, R, _, _] ]

    make_move((2, 3), right)
    assert board1a == [ [_, _, _, M, _],
                        [_, _, M, M, _],
                        [_, R, _, _, R],
                        [_, R, _, _, _],
                        [_, _, R, _, _] ]






    # Replace with tests
    #pass

def test_choose_computer_move():
    set_board(board2)
    assert make_move(choose_computer_move(M)[0], choose_computer_move(M)[1]) != board2

    set_board(board1)
    assert make_move(choose_computer_move(M)[0], choose_computer_move(M)[1]) != board1
    pass

def test_is_enemy_win():
    set_board(board3)
    assert is_enemy_win() == False
    set_board(board5)
    assert is_enemy_win() == True
    set_board(board6)
    assert is_enemy_win() == True
    set_board(board7)
    assert is_enemy_win() == True
    set_board(board8)
    assert is_enemy_win() == True
    set_board(board9)
    assert is_enemy_win() == False
    # Replace with tests
    pass

"""
now thats the last function done. Im just writing this comment as github refuses to notice any changes between this newer version that passes all tests and the previous one that failed the is_enemy_win function,
regardless of using the git add . or git add <file name> command
"""


