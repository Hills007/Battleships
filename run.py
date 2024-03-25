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

def make_guess(board):
    x = int(input("Enter row number to guess: "))
    y = int(input("Enter column number to guess: "))
    if not valid_coordinates(x, y, board):
        print("Invalid coordinates. Please try again.")
        return make_guess(board)
    result = board.guess(x, y)
    print(result)
    board.display()

def play_game(computer_board, player_board):
    while len(computer_board.ships) > 0 and len(player_board.ships) > 0:
        print("Player's turn:")
        make_guess(computer_board)
        if len(computer_board.ships) == 0:
            print("Player wins!")
            scores["player"] += 1
            break
    # Computer's turn
    print("Computer's turn:")
    x = random_point(player_board.size)
    y = random_point(player_board.size)
    result = player_board.guess(x, y)
    print(f"Computer guesses: ({x}, {y}) - {result}")
    if len(player_board.ships) == 0:
        print("Computer wins!")
        scores["computer"] += 1
        break
def new_game():
    size = 5
    num_ships = 4
    scores["player"] = 0
    scores["computer"] = 0   
    print("_" * 35)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("_" * 35)
    player_name = input("Please enter your name: \n")
    print("_" * 35)

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

new_game()