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

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at ((2,1)) == R
    assert at ((2,2)) == M
    ##eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at ((0,0)) == _
    assert at ((1,2)) == R
    assert at ((4,4)) == M
    #eventually add some board2 and at least 3 tests with it


def test_get_board():
    set_board(board1)
    set_board(board2)
    assert board1 == get_board()
    assert board2 == get_board()
    #eventually add at least one more test with another board


def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == [0,0]
    assert string_to_location('B2') == [1,1]
    assert string_to_location('C4') == [2,3]
    ##eventually add at least one more exception test and two more
    ##test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((5,5))
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((2,3)) == 'C4'
    assert location_to_string((4,4)) == 'E5'
    ## Replace with tests
    ## Replace with tests

def test_at():
    # Replace with tests
    pass


def test_all_locations():
    # Replace with tests
    pass

def test_adjacent_location():
    adjacent =  adjacent_location() - is_adjacent == (0,0)
    assert adjacent == (0,0)
    # Replace with tests
    pass
    
def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer() == True
    # Replace with tests
    pass
    
def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy() == True
    # Replace with tests
    pass

def test_is_legal_move():
    # Replace with tests
    pass

def test_can_move_piece_at():
    # Replace with tests
    pass

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
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


