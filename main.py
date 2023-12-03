import random

GAME_BOARD = [[" ", " ", " ", " ", " ", " ", " "] for x in range(7)]
LETTERS_TO_NUMBERS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
print(GAME_BOARD)
ships_amount = {1: 3, 2: 2}

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
    
def generate_big_ship(x_cord, y_cord, length):
    directions = []
    created_big_ship = True

    if not got_interruption(x_cord, y_cord):
        if x_cord + length <= 7:
            directions.append("down")
        if y_cord + length <= 7:
            directions.append("right")
        if x_cord - length >= -1:
            directions.append("up")
        if y_cord - length >= -1:
            directions.append("left")
    else: 
        return False

    choice = random.choice(directions)
    
    if choice == "left":
        count = y_cord
        for i in range(length):
            GAME_BOARD[x_cord][count - 1] = "O"
            count -= 1
    if choice == "right":
        count = y_cord
        for i in range(length):
            GAME_BOARD[x_cord][count + 1] = "O"
            count += 1  
    if choice == "up":
        count = x_cord
        for i in range(length):
            GAME_BOARD[count - 1][y_cord] = "O"
            count -= 1   
    if choice == "down":
        count = x_cord
        for i in range(length):
            GAME_BOARD[count - 1][y_cord] = "O"
            count += 1   

    return created_big_ship


#for elem in ships_amount.items():
#    for i in range(elem[0]):
#        generate_ship(elem[1])

#count = 0
#while count != 4:
#    if generate_ship() == True:
#        count += 1

#c = 0
#while c != 1:
#    x = random.randint(0, 6)
#    y = random.randint(0, 6)
#    if generate_big_ship(x, y, 3) != False:
#        c += 1
    
for elem in ships_amount.items():
    c = 0
    while c != elem[0]:
        if generate_big_ship(random.randint(0,6), random.randint(0,6), elem[1]):
            c += 1

cou = 0
while cou != 4:
    if generate_ship():
        cou += 1

# game loop
while True:

    display_interface(board=GAME_BOARD)
    hit_coordinate = input("Enter a coordinate in 'letter/digit' form: ")
    make_hit(hit_coordinate)


