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

    # Get player input - mark and cell location to mark
    while True:
        inputData = gInput.enterData(gOutput.gameTurns)
        print("Input Data : " + inputData + " Has length of: " + str(len(inputData)))

        valid = gProc.validateData(inputData, gOutput.gameTurns)
        if valid != -1:
            break
        print("This is not valid")
    print("This is valid")

    









