gamesWonX = 0
gamesWonO = 0




def checkStaleMate(turns, board):
    # TODO
    staleMate = False
    if turns == 8: # in the process of completing the 9th round, if winner still not declared, game has to be a tie
        staleMate = True
    if turns == 7: # there is one cell left
        testBoard = board.copy()
        mark = "X" # It will always be Player 1's turn next
        cell = findRemainingCell(testBoard)
        row = cell[0]
        col = cell[1]
        testBoard[row][col] = mark
        staleMate = not checkWinner(turns + 1, testBoard, row, col)
    if turns == 6: # There are two cells left
        testBoard = board.copy()
        rowOptions = [-1, -1]
        colOptions = [-1, -1]
        # Find the 2 remaining unmarked cells
        for index in range(2):
            cell = findRemainingCell(testBoard)
            rowOptions[index] = cell[0]
            colOptions[index] = cell[1]
            testBoard[rowOptions[option]][colOptions[option]] = "S"
        # Remove "S" mark from those cells
        unMarkCell(testBoard, "S")

        #Test if both combinations will lead to a stalemate
        for option in range(2): 
            staleMateList = [True, True, True, True]
            mark = "O" # It will always be Player 2's turn next
            testBoard[rowOptions[option]][colOptions[option]] = mark
            staleMateList[option] = not checkWinner(turns + 1, testBoard, rowOptions[option], colOptions[option])
            # Afterwards it will be Player 1's turn
            mark = "X"
            testBoard[rowOptions[1-option]][colOptions[1-option]] = mark
            staleMateList[option + 2] = not checkWinner(turns + 2, testBoard, rowOptions[option], colOptions[option])
        
        if staleMateList[0] == True and staleMateList[1] == True:
            staleMate = True
        elif staleMateList[0] == True and staleMateList[1] == True and staleMateList[2] == True and staleMateList[3] == True:
            staleMate = True

    return staleMate



def findRemainingCell(board):
    cell = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "A":
                cell = [i, j]
                return cell

    return cell

def unMarkCell(board, tempMark):
    for i in range(3):
        for j in range(3):
            if board[i][j] == tempMark:
                board[i][i] = "A"




def checkWinner(turns, board, row, col):
    # TODO:
    if turns % 2 == 0: #Currently Player 1's turn, mark = X
        mark  = "X"
    else: #Currently Player 2's turn, mark = "O"
        mark = "O"

    # Check if last input results in a row victory
    gameWon = checkRow(board, mark, row)

    # Check if last input results in a column vicotry
    if gameWon == False:
        gameWon = checkColumn(board, mark, col)

    # Check if last input results in a diagonal vicotry
    if gameWon == False:
        gameWon = checkDiagnol(board, mark, row, col)

    global gamesWonO, gamesWonX
    if gameWon == True:
        if mark == "X":
            gamesWonX = gamesWonX + 1
        else:
            gamesWonO = gamesWonO + 1
        
    return gameWon




def checkRow(board, mark, row):
    winner = True
    for i in range(3):
        if board[row][i] != mark:
            winner = False

    return winner

def checkColumn(board, mark, col):
    winner = True
    for j in range(3):
        if board[j][col] != mark:
            winner = False
    return winner

def checkDiagnol(board, mark, row, col):
    winner = True
    if (row + col) % 2 == 0: # if true, mark is on a diaglon line
        if row == col: # Top left to bottom right
            for k in range(3):
                if board[k][k] != mark:
                    winner = False
        if winner == True:
            return winner
        
        if (row + col) == 2 or (winner == False and row == 1 and col == 1): # Bottom left to top right, and winner hasn't been declared
            winner = True
            for k in range (3):
                if board[3-1-k][k] != mark:
                    winner = False
    else:
        winner = False

    return winner










