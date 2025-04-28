import gameState as gS

def printBoard(board):
    for row in board:
        print(row)


# editable tic-tac-toe board
board1 = [   ["O","X","O"],
             ["O","X","X"], # Completed board and stalemate
             ["X","O","X"]
         ]

board2 = [   ["X","O","X"],
             ["X","O","O"], # 8/9 -> stalemate
             ["O","X","A"]
         ]


board3 = [   ["X","X","O"],
             ["O","X","X"], # 8/9 -> Player 1 will win, game keeps going
             ["O","O","A"]
         ]

board4 = [   ["O","X","X"],
             ["O","X","X"], # 7/9 -> Player 1 will win, game keeps going
             ["O","A","A"]
         ]

board5 = [   ["X","X","O"],
             ["O","O","X"], # 7/9 -> Stalemate no matter what
             ["X","A","A"]
         ]



turns = 6
row = 0
col = 0

gameBoard = board5
printBoard(gameBoard)
winner = gS.checkWinner(turns, gameBoard, row, col)

print("Winner value is: ", winner)
if winner == True:
    print("There is a winner")
else:
    print("No one has one")

staleMate = gS.checkStaleMate(turns, gameBoard)
print("Stalemate value is: ", staleMate)
if staleMate == True:
    print("This is a stalemate")
else:
    print("The game keeps going")

