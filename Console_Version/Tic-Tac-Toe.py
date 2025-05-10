import gameInput as gInput
import gameOutput as gOutput
import gamePreProcessing as gProc
import gameState as gState


## Initialize gameData
gOutput.gamesPlayed = 0
gOutput.gameTurns = 0

play = True

while play:
    # Start a new game

    key = gInput.newGame(gOutput.gamesPlayed)

    if key == "Q":
        play = False
        break

    done = False

    while not done:
        # Get player input - mark and cell location to mark, then enter into board
        while True:
            inputData = gInput.enterData(gOutput.gameTurns)

            valid = gProc.validateData(inputData, gOutput.gameTurns)
            if valid != -1:
                break


        # Check state of the game
        gameWon = gState.checkWinner(gOutput.gameTurns, gProc.board, gProc.rowUpdate, gProc.colUpdate)
        gameTie = gState.checkStaleMate(gOutput.gameTurns, gProc.board)

        # Display game state
        gOutput.printCurrentMetrics(gameWon, gameTie, gProc.board)
        

        if gameWon == True or gameTie == True:
            done = True 
            gOutput.printSeriesMetrics(gState.gamesWonX, gState.gamesWonO)
            ## Reset gameboard
            gProc.board = board = [[" " for i in range(3)] for j in range(3)]
            # Reset number of turns
            gOutput.gameTurns = 0
















