gamesPlayed = 0
gameTurns = 0

def printSeriesMetrics(p1Wins, p2Wins):
    # TODO: display the number of games played, number of games player 1 has won and number of games player 2 has won
    print("A total of " + str(gamesPlayed + 1) + " games of Tic-Tac-Toe, including this one, have been played!")
    print("Player 1 (X) has won ", p1Wins, " games.  Player 2 (O) has won ", p2Wins, " games.")


def printCurrentMetrics(gameWon, gameStaleMate, board):
    # TODO: display if the game has been won (and by who), or that the game is a draw, or that the game will continue
    # in any case, print the number of turns the the current gameBoard
    global gamesPlayed, gameTurns

    print("GAMEBOARD!!!")
    for row in board:
        print(row)
    
    print(str(gameTurns + 1) + " turns have been played!")

    if gameWon:
        gamesPlayed = gamesPlayed + 1
        print("This current game of Tic-Tac-Toe has come to an end.")
        if gameTurns % 2 == 0:  # Player 1 won the game
            print("Player 1 (X) has won the game")
        else:               # Player 2 won the game
            print("Player 2 (O) has won the game")
    elif gameStaleMate:
        gamesPlayed = gamesPlayed + 1
        print("The current game of Tic-Tac-Toe has ended in a STALEMATE - You guys are both MID!!!!!!!")

    gameTurns = gameTurns + 1

    




