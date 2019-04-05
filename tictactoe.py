"""
Tic tac toe game.

TODO:
get user input needs valid row/column range error testing.
display grid needs numbers for rows/columns.
"""

def generate_blank_locations(GRID_SIZE):
    locations = []
    for row in range(GRID_SIZE):
        locations.append([])
        for col in range(GRID_SIZE):
            locations[row].append("")
    return locations


def display_grid(GRID_SIZE, locations):
    grid = ""

    for row in range(GRID_SIZE):
        grid += "--" * GRID_SIZE + "-\n"

        for col in range(GRID_SIZE):
            if locations[row][col] != "":
                grid += "|{}".format(locations[row][col])
            else:
                grid += "| "
        grid += "|\n"

    grid += "--" * GRID_SIZE + "-\n"

    print(grid)


def get_user_row_column_input():
    row = int(input("Enter Row Number: "))
    column = int(input("Enter Column Number: "))
    return (row, column)

def check_user_row_column(GRID_SIZE, user_input):
    while True:
        try:
            row = user_input[0]
            column = user_input[1]
            if (row >= 1 and row <= GRID_SIZE) and (col >= 1 and col <= GRID_SIZE):
                return True
            else:
                print("*** Error - row/column not in the valid range ***")
                return False
        except:
            print("*** Game Error - row/column inputs ***")
            return False

def retrieve_row_column():
    while True:
        user_input = get_user_row_column_input()
        if check_user_row_column(GRID_SIZE, user_input):
            return user_input




if __name__ == "__main__":
    GRID_SIZE = 3

    locations = generate_blank_locations(GRID_SIZE)
    display_grid(GRID_SIZE, locations)
