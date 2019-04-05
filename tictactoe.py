"""
Tic tac toe game.
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



if __name__ == "__main__":
    GRID_SIZE = 3
    
    locations = generate_blank_locations()
    display_grid(locations)
