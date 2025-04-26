import gameState as gS

def printBoard():
    for row in board:
        print(row)


# editable tic-tac-toe board
board = [   ["O","O","X"],
            ["A","X","A"],
            ["X","X","O"]
         ]

printBoard()

turns = 6
row = 0
col = 2

winner = gS.checkWinner(turns, board, row, col)

print("Winner value is: ", winner)
if winner == True:
    print("There is a winner")
else:
    print("No one has one")

