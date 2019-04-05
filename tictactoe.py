"""
Tic tac toe game.

TODO:

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

    for num in range(1, GRID_SIZE + 1):
        grid += " {}".format(num)
    grid += "\n"

    for row in range(GRID_SIZE):
        grid += "--" * GRID_SIZE + "-\n"

        for col in range(GRID_SIZE):
            if locations[row][col] != "":
                grid += "|{}".format(locations[row][col])
            else:
                grid += "| "
        grid += "| {}\n".format(row + 1)

    grid += "--" * GRID_SIZE + "-\n"

    print(grid)


""" *** INPUTS *** """

def get_user_row_column_input():
    row = input("Enter Row Number: ")
    column = input("Enter Column Number: ")
    return (row, column)

def check_user_row_column(GRID_SIZE, user_input):
    try:
        row = int(user_input[0])
        column = int(user_input[1])

        if row >= 1 and row <= GRID_SIZE:
            if column >= 1 and column <= GRID_SIZE:
                return True
        return False
    except:
        return False

def input_row_column(GRID_SIZE):
    while True:
        user_input = get_user_row_column_input()
        if check_user_row_column(GRID_SIZE, user_input):
            return user_input
        else:
            print("*** Error - row/column input incorrect. ***")




if __name__ == "__main__":
    GRID_SIZE = 3

    locations = generate_blank_locations(GRID_SIZE)
    display_grid(GRID_SIZE, locations)
    input_row_column(GRID_SIZE)
