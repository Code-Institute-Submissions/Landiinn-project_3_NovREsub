from random import randint

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

GUESS_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

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
        ship_row, ship_column = randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column = "X"]


def get_ship_location():
    row = input("Enter the row of the ship: ")
    while row not in "12345678":
        print("Unvalid Choice, Please select a valid option")
        row = input("Enter the row: ")
        column = input("Enter the column: ")
    return int(row) -1, letters_to_numbers[column]

    