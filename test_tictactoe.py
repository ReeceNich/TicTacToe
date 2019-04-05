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


if __name__ == "__main__":
    test_generate_blank_locations_three()
    test_generate_blank_locations_five()
