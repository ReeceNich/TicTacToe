"""
Tic tac toe game.

TODO:
get user input needs valid row/column range error testing.
display grid needs numbers for rows/columns.
"""

def generate_blank_locations():
    locations = []
    for row in range(GRID_SIZE):
        locations.append([])
        for col in range(GRID_SIZE):
            locations[row].append("")
    return locations


def display_grid(locations):
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


def user_row_column():
    while True:
        try:
            row = int(input("Enter Row Number: "))
            column = int(input("Enter Column Number: "))
            return (row, column)
        except:
            print("*** Error with row/column inputs ***")




if __name__ == "__main__":
    GRID_SIZE = 3

    locations = generate_blank_locations()
    display_grid(locations)
