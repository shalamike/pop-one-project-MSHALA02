# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
import random


def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    _ = '_'
    board = [[r, r, r, r, m],
             [r, r, r, r, r],
             [r, r, m, r, r],
             [r, r, r, r, r],
             [m, r, r, r, r]]


def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board


def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board


def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    to_location = []

    if s[0] == "A":
        to_location.append(0)
    elif s[0] == "B":
        to_location.append(1)
    elif s[0] == "C":
        to_location.append(2)
    elif s[0] == "D":
        to_location.append(3)
    elif s[0] == "E":
        to_location.append(4)
    else:
        raise ValueError('Invalid Location')

    if s[1] == "1":
        to_location.append(0)
    elif s[1] == "2":
        to_location.append(1)
    elif s[1] == "3":
        to_location.append(2)
    elif s[1] == "4":
        to_location.append(3)
    elif s[1] == "5":
        to_location.append(4)
    else:
        raise ValueError('Invalid Location')

    return to_location


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    location_str = ""

    if location[0] == 0:
        location_str += "A"
    elif location[0] == 1:
        location_str += "B"
    elif location[0] == 2:
        location_str += "C"
    elif location[0] == 3:
        location_str += "D"
    elif location[0] == 4:
        location_str += "E"
    else:
        raise ValueError('Invalid String')

    if location[1] >= 0 and location[1] <= 4:
        for i in range(0, 5):
            if location[1] == i and i < 5:
                location_str += str(i + 1)
                break
    return location_str


def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]


def all_locations():
    """Returns a list of all 25 locations on the board."""
    # probably going to have to use an iterative or recursive command to return all 25 locations
    every_location = []
    location = ()
    for i in range(5):
        for j in range(5):
            location = (i, j)
            every_location.append(location)

    return every_location


def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location

    adjacent = location
    if direction == "up":
        adjacent = (row - 1, column)
    elif direction == "down":
        adjacent = (row + 1, column)
    elif direction == "left":
        adjacent = (row, column - 1)
    elif direction == "right":
        adjacent = (row, column + 1)

    if adjacent in all_locations():
        adjacent = tuple(adjacent)
        return adjacent


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""

    if at(location) != "M":
        raise ValueError("Not A Musketeer")
    else:
        if adjacent_location(location, direction) in all_locations() and at(location) == "M" and at(
                adjacent_location(location, direction)) == "R":
            return True
        else:
            return False


def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    # pass # Replace with code


    if at(location) != "R":
        raise ValueError("Not Cardinal Richleau's men")
    else:
        if adjacent_location(location, direction) in all_locations() and at(location) == "R" and at(
                adjacent_location(location, direction)) == "_":
            # if at(location) == "R" and  at(adjacent_location(location,direction)) == "_" and adjacent_location(location, direction) in all_locations():
            return True
        else:
            return False


def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    # pass # Replace with code
    if at(location) == "M":
        return is_legal_move_by_musketeer(location, direction)
    elif at(location) == "R":
        return is_legal_move_by_enemy(location, direction)


def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
        You can assume that input will always be in correct range.
        You can assume that input will always be in correct range."""
    # pass # Replace with code
    all_possible_directions = ["up", "down", "left", "right"]

    can_move = False

    for possible_direction in all_possible_directions:
        if is_legal_move(location, possible_direction) == True:
            can_move = True
            break

    return can_move


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    # pass # Replace with code

    has_a_legal_move = False

    if who == "M":
        for location in all_locations():
            if at(location) == "M" and can_move_piece_at(location) == True:
                has_a_legal_move = True
                print(at(location))
                break
    else:
        for location in all_locations():
            if at(location) == "R" and can_move_piece_at(location) == True:
                has_a_legal_move = True
                print(at(location))
                break

    return has_a_legal_move


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    # pass # Replace with code
    all_possible_directions = ["up", "down", "left", "right"]

    valid_directions = []

    if can_move_piece_at(location) == True:
        for direction in all_possible_directions:
            if is_legal_move(location, direction) == True:
                valid_directions.append(direction)

    return valid_directions


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be in correct range."""
    # pass # Replace with code

    location_is_legal = False

    if location in all_locations():
        location_is_legal = True

    return location_is_legal


def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    # pass # Replace with code

    move_is_legal = False

    if adjacent_location(location, direction) in all_locations():
        move_is_legal = True

    return move_is_legal


def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    # pass # Replace with code
    all_possible_moves = []

    if has_some_legal_move_somewhere(player) == True:
        for location in all_locations():
            for direction in possible_moves_from(location):
                if at(location) == player and can_move_piece_at(location) == True:
                    all_possible_moves.append((location, direction))

    return all_possible_moves


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    # pass # Replace with code

    current_board = get_board()
    if is_legal_location(location) == True and is_legal_move(location, direction) == True and can_move_piece_at(
            location) == True:
        new_move = adjacent_location(location, direction)
        current_board[new_move[0]][new_move[1]] = at(location)
        current_board[location[0]][location[1]] = "_"

    (set_board(current_board))

    return board


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    # pass # Replace with code

    computer_move = random.choice(all_possible_moves_for(who))

    return computer_move


def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    enemy_win = False

    for row in range(5):
        board_column = []
        if board[row].count("M") == 3:
            enemy_win = True
            break
        else:
            for column in range(5):
                board_column.append(board[column][row])
                if board_column.count("M") == 3:
                    enemy_win = True

    return enemy_win
"""
now thats the last function done. Im just writing this comment as github refuses to notice any changes between this newer version that passes all tests and the previous one that failed the is_enemy_win function,
regardless of using the git add . or git add <file name> command
"""
# ---------- Communicating with the user ----------
# ----you do not need to modify code below unless you find a bug
# ----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end=" ")
        for j in range(0, 5):
            print(board[i][j] + " ", end=" ")
        print()
        ch = chr(ord(ch) + 1)
    print()


def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()


def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user


def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
        and move[0] in 'ABCDE'
        and move[1] in '12345'
        and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()


def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else:  # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)


def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else:  # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board


def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from', \
          location_to_string(location), 'to', \
          location_to_string(new_location) + ".\n")


def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
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
