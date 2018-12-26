import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'
is_adjacent = (1,1)

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, R, _, M, _],
            [_, _, R, _, _],
            [_, R, M, R, _],
            [_, _, _, _, _],
            [R, _, _, _, M] ]

# board with no possible musketeer moves
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
    assert at((3, 1)) == get_board()[3][1]


def test_all_locations():
    # Replace with tests
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]
    pass

def test_adjacent_location():
    with pytest.raises(ValueError):
        adjacent_location((4,4), "down")
        adjacent_location((4,4), "right")
        adjacent_location((0,0), "up")
        adjacent_location((0,0), "left")
    assert adjacent_location((1,1), "down") == (0,1)
    assert adjacent_location((3,3), "left") == (3,2)
    assert adjacent_location((4,4), "up") == (3,4)
    # Replace with tests
    pass
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((1,3),"down") == True
    assert is_legal_move_by_musketeer((0,3), "left") == False
    set_board(board2)
    assert is_legal_move_by_musketeer((2, 2), "up") == True
    assert is_legal_move_by_musketeer((0,3), "left") == False
    set_board(board3)
    assert is_legal_move_by_musketeer((0,4), "left") == False
    assert is_legal_move_by_musketeer((4, 4), "down") == False

    # Replace with tests
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1,2), "left") == True
    assert is_legal_move_by_enemy((2,1), "right") == False
    set_board(board2)
    assert is_legal_move_by_enemy((0,1), "left") == True
    assert is_legal_move_by_enemy((2,3), "down") == False
    set_board(board3)
    assert is_legal_move_by_enemy((0,0), "right") == True
    assert is_legal_move_by_enemy((0,0), "left") == False
    set_board(board4)
    assert is_legal_move_by_enemy((0,0), "right") == False
    assert is_legal_move_by_enemy((0,0), "down") == False

    # Replace with tests
    pass

def test_is_legal_move():
    # Replace with tests
    #pass
    set_board(board1)
    assert is_legal_move_by_enemy((4,3), "right") == True
    assert is_legal_move_by_musketeer((1,3),"left") == True
    assert is_legal_move_by_enemy((2,3), "up") == False
    assert is_legal_move_by_musketeer((2,2), "down") == False
    set_board(board2)
    assert is_legal_move_by_enemy((2,3), "right" ) == True
    assert is_legal_move_by_musketeer((2,2), "right") == True
    assert is_legal_move_by_enemy((1,2), "down" ) == False
    assert is_legal_move_by_musketeer((4,4), "up") == False

"""
Skeleton code for test legal move
    assert is_legal_move_by_enemy((), ) == True
    assert is_legal_move_by_musketeer((), ) == True
    assert is_legal_move_by_enemy((), ) == False
    assert is_legal_move_by_musketeer((), ) == False

"""

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((4,3)) == True
    assert can_move_piece_at((3,1)) == True
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((0,3)) == False
    # Replace with tests
    pass

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
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
    assert possible_moves_from((2,2)) == ["left","right","up"]
    # Replace with tests
    pass

def test_is_legal_location():
    # Replace with tests
    pass

def test_is_within_board():
    # Replace with tests
    pass

def test_all_possible_moves_for():
    # Replace with tests
    pass
    
def test_make_move():
    # Replace with tests
    pass
    
def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'
    pass

def test_is_enemy_win():
    # Replace with tests
    pass

#will need to complete for monday


