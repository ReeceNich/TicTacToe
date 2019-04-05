from tictactoe import *

def test_generate_blank_locations_three():
    GRID_SIZE = 3
    locations = generate_blank_locations(GRID_SIZE)
    test_locations = [["", "", ""], ["", "", ""], ["", "", ""]]

    assert locations == test_locations, "Blank grids do not match on GRID_SIZE=3 !"

def test_generate_blank_locations_five():
    GRID_SIZE = 5
    locations = generate_blank_locations(GRID_SIZE)
    test_locations = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]

    assert locations == test_locations, "Blank grids do not match on GRID_SIZE=5 !"



def test_check_user_row_column_normal():
    GRID_SIZE = 3
    user_input = (1, 2)
    check = check_user_row_column(GRID_SIZE, user_input)

    assert check == True, "Check user row, normal data expected true."

def test_check_user_row_column_boundary():
    GRID_SIZE = 3
    user_input = (1, 3)
    check = check_user_row_column(GRID_SIZE, user_input)

    assert check == True, "Check user row, boundary data expected true."

def test_check_user_row_column_erroneous():
    GRID_SIZE = 3
    user_input = ("cheese", 2)
    check = check_user_row_column(GRID_SIZE, user_input)

    assert check == False, "Check user row, errorneous data expected error."




if __name__ == "__main__":
    test_generate_blank_locations_three()
    test_generate_blank_locations_five()

    test_check_user_row_column_normal()
    test_check_user_row_column_boundary()
    test_check_user_row_column_erroneous()
