GAME_BOARD = [["X", "X", "X", "X", "X", "X", "X"] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 3, "D": 4, "E": 5, "F": 6}
print(GAME_BOARD)

def display_interface(board):
    print("   A B C D E F G")
    print("  --------------")

    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row = row + board[i][j] + " "

        print(f"{i + 1}| {row}")

display_interface(GAME_BOARD)