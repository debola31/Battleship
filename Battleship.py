import random

board = []
ship_row =[]
ship_col = []
ship_status = [False,False]
limit = 5
dimension = 5

for x in range(dimension):
    board.append(["O"] * dimension)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

for i in range(2):
    ship_row.append(random_row(board))
    ship_col.append(random_col(board))

if ship_row[0] == ship_row[1] and ship_col[0] == ship_col[1]:
    ship_row[1] = random.choice(range(0,ship_row[0]) + range(ship_row[0]+ 1,dimension))
    ship_col[1] = random.choice(range(0,ship_col[0]) + range(ship_col[0]+ 1,dimension))
    

for turn in range(limit):
    print ('Turn', turn + 1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if ship_status[0] == False and ship_status[1] == False:
        if guess_row == ship_row[0] and guess_col == ship_col[0]:
            board[guess_row][guess_col] = "X"
            print ("Congratulations! You sunk a battleship!")
            ship_status[0] = True
            if ship_status[0] == True and ship_status[1] == True:
                print ('Game Won')
                break
        elif guess_row == ship_row[1] and guess_col == ship_col[1]:
            board[guess_row][guess_col] = "X"
            print ("Congratulations! You sunk a battleship!")
            ship_status[1] = True
            if ship_status[0] == True and ship_status[1] == True:
                print ('Game Won')
                break
        elif guess_row not in range(dimension) or guess_col not in range(dimension):
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

    elif ship_status[0] == True and ship_status[1] == False:
        if guess_row == ship_row[1] and guess_col == ship_col[1]:
            board[guess_row][guess_col] = "X"
            print ("Congratulations! You sunk a battleship!")
            ship_status[1] = True
            if ship_status[0] == True and ship_status[1] == True:
                print ('Game Won')
                break
        elif guess_row not in range(dimension) or guess_col not in range(dimension):
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

    elif ship_status[0] == False and ship_status[1] == True:
        if guess_row == ship_row[0] and guess_col == ship_col[0]:
            board[guess_row][guess_col] = "X"
            print ("Congratulations! You sunk a battleship!")
            ship_status[1] = True
            if ship_status[0] == True and ship_status[1] == True:
                print ('Game Won')
                break
        elif guess_row not in range(dimension) or guess_col not in range(dimension):
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

