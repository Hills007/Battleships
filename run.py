from random import randint
scores = {"computer": 0, "player": 0}
class Board:
    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = board_type
        self.guesses = []
        self.ships = []

    def display(self):
        for row in self.board:
            print(" ".join(row)) 

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        if (x, y) in self.ships:
        self.board[x][y] = "*"
        return "Hit"
        else:
        return "Miss"

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
            self.board[x][y] = "@"


def random_point(size):
    return randint(0, size-1)  

def valid_coordinates(x, y, board):
    return 0 <= x < board.size and 0 <= y < board.size

def populate_board(board):
    for _ in range(board.num_ships):
    x = random_point(board.size)
    y = random_point(board.size)
    while (x, y) in board.ships:
        x = random_point(board.size)
        y = random_point(board.size)
    board.add_ship(x, y)

define make_guess(board):
