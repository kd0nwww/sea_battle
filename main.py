GAME_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
print(GAME_BOARD)

def display_interface(board):
    print("   A B C D E F G")
    print("  --------------")

    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row = row + board[i][j] + " "

        print(f"{i + 1}| {row}")

def make_hit(cord):
    x = int(cord[1]) - 1
    y = LETTERS_TO_NUMBERS[cord[0]]
    GAME_BOARD[x][y] = "X"

while True:
    display_interface(board=GAME_BOARD)
    hit_coordinate = input("Enter a coordinate in 'letter/digit' form: ")
    make_hit(hit_coordinate)