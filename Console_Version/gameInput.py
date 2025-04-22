

def newGame(gamesPlayed):
    # TODO: Welcome Player if new game has started and prompt to begin
    # Welcome Both players to the game
    if gamesPlayed == 0:
        print("\nWelcome to Tic-Tac-Toe!!!!!! \nPlayer 1 is \"X\", Player 2 is \"O\"! ")
        print("Type \"G\" then press \"Enter\" when you are ready to play!")

        key = ""

        while key != "G":
            key = input(": ")
            if key != "G":
                print("Invalid input, please enter the character \"G\"")

        print("Alright, lets start the game!!!")
    else:
        print("The previous game has been completed. \nif you like to play again press \"G\"")
        print("If you would like to quit the game, press \"Q\"")
        
        key = " "
        while key != "G" and key != "Q":
            key = input(": ")
            if key == "G":
                print("Alright, we will start another game!!")
            elif key == "Q":
                print("Alright, thanks for playing!!")
                exit(0)
            else:
                print("Invalid input, please enter \"G\" to play again or \"Q\" to quit playing")
    

def enterData(turns):
    #accepted = False
    if turns % 2 == 0:
        print("Player 1's turn, please enter your mark - \"X\", and cell location e.g \"X 2 1\"")
        playerInput = input(": ")
    else:
        print("Player 2's turn, please enter your mark - \"O\", and cell location e.g \"O 2 1\"")
        playerInput = input(": ")

    return playerInput


"""

    while accepted == False:
        print("Please Enter you Mark - \"X\" for Player 1 and \"O\" for Player 2, and cell location (1 to 3 inclusive)")
        playerInput = input(":")
        if len(playerInput) != 5:
            # Error messge
            print("Input data should be 5 characters in length, including spaces")
            pass
        elif playerInput[1] != " " or playerInput[3] != " ":
            #Error messgge
            print("Character at index 1 and index 3 should be spaces")
            pass
        else:
            accepted = True
            return playerInput
"""


