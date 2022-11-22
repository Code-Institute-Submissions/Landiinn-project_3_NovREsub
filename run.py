from random import randint 

PORT = 8000 

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):

    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print("\n")


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print("Invalid Choice, Please select a valid option \n")
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column: ").upper()
    while column not in "ABCDEFGH":
        print("Invalid option \n")
        column = input("Enter the column: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    {create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print("Pick a location \n")
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
            print("You have picked that one already")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("You missed")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("Winner!")
            break
        print("You have " + str(turns) + " turns left\n")
        if turns == 0:
            print("You are out of turns")
    }