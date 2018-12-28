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


def test_all_locations():
    # Replace with tests
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]
    pass

def test_adjacent_location():
    """
    with pytest.raises(ValueError):
        adjacent_location((4,4), down)
        adjacent_location((4,4), right)
        adjacent_location((0,0), up)
        adjacent_location((0,0),left)
    """
    assert adjacent_location((1,1), down) == (2,1)
    assert adjacent_location((3,3), left) == (3,2)
    assert adjacent_location((4,4), up) == (3,4)
    assert adjacent_location((2,2), right) == (2,3)
    # Replace with tests
    pass
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((1,3),down) == True
    assert is_legal_move_by_musketeer((0,3), left) == False
    set_board(board2)
    assert is_legal_move_by_musketeer((2, 2), up) == True
    assert is_legal_move_by_musketeer((0,3), left) == False
    set_board(board3)
    assert is_legal_move_by_musketeer((0,4), left) == False
    assert is_legal_move_by_musketeer((4, 4), down) == False

    # Replace with tests
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1,2), left) == True
    assert is_legal_move_by_enemy((2,1), right) == False
    set_board(board2)
    assert is_legal_move_by_enemy((0,1), left) == True
    assert is_legal_move_by_enemy((2,3), down) == False
    set_board(board3)
    assert is_legal_move_by_enemy((0,0), right) == True
    assert is_legal_move_by_enemy((0,0), left) == False
    set_board(board4)
    assert is_legal_move_by_enemy((0,0), right) == False
    assert is_legal_move_by_enemy((0,0), down) == False

    # Replace with tests
    pass

def test_is_legal_move():
    # Replace with tests
    #pass
    set_board(board1)
    assert is_legal_move_by_enemy((4,3), right) == True
    assert is_legal_move_by_musketeer((1,3),left) == True
    assert is_legal_move_by_enemy((2,3), up) == False
    assert is_legal_move_by_musketeer((2,2), down) == False
    set_board(board2)
    assert is_legal_move_by_enemy((2,3), right ) == True
    assert is_legal_move_by_musketeer((2,2), right) == True
    assert is_legal_move_by_enemy((1,2), down ) == False
    assert is_legal_move_by_musketeer((4,4), up) == False

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
    assert has_some_legal_move_somewhere(M) == True
    assert has_some_legal_move_somewhere(R) == True
    set_board(board3)
    assert has_some_legal_move_somewhere(M) == False
    assert has_some_legal_move_somewhere(R) == True
    set_board(board4)
    assert has_some_legal_move_somewhere(M) == True
    assert has_some_legal_move_somewhere(R) == False
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,2)) == [left, right, up]
    assert possible_moves_from((3,1)) == [left, right, down]
    assert possible_moves_from((4,3)) == [left, right, up]
    assert possible_moves_from((1,3)) == [left, down]
    set_board(board2)
    assert possible_moves_from((4,0)) == [right, up]
    assert possible_moves_from((4,4)) == []
    assert possible_moves_from((0,1)) == [left, right, down]
    set_board(board3)
    assert possible_moves_from((0,4)) == []
    assert possible_moves_from((2,2)) == []
    assert possible_moves_from((4,4)) == []
    set_board(board4)
    assert possible_moves_from((0,0)) ==[]


    """
    skeleton code for testy possibel moves
    
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

def test_all_possible_moves_for():
    set_board(board1)
    assert all_possible_moves_for(M) == [((1,3), left), ((1,3), down), ((2,2), left), ((2,2), up), ((2,2), right)]
    assert all_possible_moves_for(R) == [((1,2), left), ((1,2), up), ((2,1), left), ((2,1), up), ((2,3), down), ((2,3), right), ((3,1), left), ((3,1), right), ((3,1), down), ((4,3), left), ((4,3), right), ((4,3), up)]
    set_board(board3)
    assert all_possible_moves_for(M) == []
    assert all_possible_moves_for(R) == [((0,0), right), ((0,0), down), ((0,2), left), ((0,2), down), ((0,2), right), ((2,4), up), ((2,4), right), ((2,4), down), ((4,0), up), ((4,0), right), ((4,2), left), ((4,2), up), ((4,2), right)]
    set_board(board4)
    assert all_possible_moves_for(M) == [((0,1), left), ((1,0), up)]
    # Replace with tests
    #pass
    
def test_make_move():
    set_board(board1)
    assert make_move((2,2), up) == [ [_, _, _, M, _],
                                     [_, _, M, M, _],
                                     [_, R, _, R, _],
                                     [_, R, _, _, _],
                                     [_, _, _, R, _]]

    assert make_move((4,3), left) ==[ [_, _, _, M, _],
                                      [_, _, R, M, _],
                                      [_, R, M, R, _],
                                      [_, R, _, _, _],
                                      [_, _, R, _, _] ]

    assert  make_move((2,3), right) == [ [_, _, _, M, _],
                                         [_, _, R, M, _],
                                         [_, R, M, _, R],
                                         [_, R, _, _, _],
                                         [_, _, _, R, _] ]
    # Replace with tests
    pass
    
def test_choose_computer_move():
    if choose_users_side() == R:
        assert choose_computer_move(M) == True
    elif choose_users_side() == M:
        assert choose_computer_move(R) == True
    # Replace with tests; should work for both 'M' and 'R'
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

#will need to complete for monday


