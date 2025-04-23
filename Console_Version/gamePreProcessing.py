rows, cols = (3, 3)

board = [["A" for i in range(cols)] for j in range(rows)]


def parseData(playerInput):
    # TODO: Parse mark, row and col value from input string and store data in a list
    if len(playerInput) != 5:
        # Error messge
        print("Input data should be 5 characters in length, including spaces")
        return [-1, -1, -1]
    elif playerInput[1] != " " or playerInput[3] != " ":
        #Error messgge
        print("Character at index 1 and index 3 should be spaces")
        return [-1, -1, -1]

    mark = playerInput[0]

    ## If entry for row or column value is not an integer make rowValue and/or colValue equal to -1
    try:
        rowValue = int(playerInput[2])
    except ValueError as e:
        print(e)
        rowValue = -1

    try:
        colValue = int(playerInput[4])
    except ValueError as e:
        print(e)
        colValue = -1
    
    values = [mark, rowValue, colValue]
    return values

def validateData(playerInput, turn_number):
    # TODO: # Check if Player Mark is correct and cell location is valid
    data = parseData(playerInput)

    
    if data[1] == -1 or data[2] == -1:
        return -1

    
    # Validate the Player Mark
    mark = data[0]
    if turn_number % 2 == 0: #if it is Player 1's turn, mark should be "X"
        if mark != "X":
            print("It is Player 1's turn, for input to be valid, the mark must be \"X\"")
            return -1
    else: # if it is Player 2's turn, mark should be "O"
        if mark != "O":
            print("It is Player 0's turn, for input to be value, the mark must be \"O\"")
            return -1
        
    # Validate the row and column Part A
    rowValue = data[1]
    colValue = data[2]

    if rowValue < 1 or rowValue > 3:
        print("The row input value must be between 1 and 3 inclusive.")
        return -1

    if colValue < 1 or colValue > 3:
        print("The column input value must be between 1 and 3 inclusive")
        return -1
    
    # Validate the row and column Part B
    if board[rowValue][colValue] == "A": # Location has not yet been filled
        board[rowValue][colValue] = mark
        print("Entry has been added to the board")
    else: # Location has been filled
        print("Position has already been filled, pick a different one!!!")
        return -1

    
    

    
