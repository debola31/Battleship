from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

limit = 4

for turn in range(limit):
    print ('Turn', turn + 1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    elif guess_row not in range(6) or guess_col not in range(6):
        print ("Oops, that's not even in the ocean.")
        if turn == limit - 1:
            print ('Game Over')
    elif(board[guess_row][guess_col] == "X"):
        print ("You guessed that one already.")
        if turn == limit - 1:
            print ('Game Over')
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        if turn == limit - 1:
            print ('Game Over')
        
    if not turn == limit - 1:
        print_board(board)
