import random

GAME_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
print(GAME_BOARD)
ships_amount = {1: 3, 2: 2, 4: 1}

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

def generate_ship():

    x = random.randint(0, 6)
    y = random.randint(0, 6)

    if got_interruption(x, y) == True:
        return False
    else:
        GAME_BOARD[x][y] = "O" 
        return True



def got_interruption(x, y):

    interrupted = False 

    for i in range(x - 1, x + 2):

        for j in range(y - 1, y + 2):

            if i == x and j == y:
                if ship_exists(i, j):
                    interrupted = True
                else:
                    continue

            elif 0 <= i <= 6 and 0 <= j <= 6:
                if ship_exists(i, j):
                    interrupted = True

    return interrupted


def ship_exists(x_cord, y_cord):
    if GAME_BOARD[x_cord][y_cord] == "O":
        return True
    else: 
        return False

#for elem in ships_amount.items():
#    for i in range(elem[0]):
#        generate_ship(elem[1])

count = 0
while count != 4:
    if generate_ship() == True:
        count += 1
    

# game loop
while True:

    display_interface(board=GAME_BOARD)
    hit_coordinate = input("Enter a coordinate in 'letter/digit' form: ")
    make_hit(hit_coordinate)