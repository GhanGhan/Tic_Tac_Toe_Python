gamesPlayed = 1
turnNumber = 0
playerInput = ""


def newGame():
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
    

def enterData():
    # TODO: Allow player to enter a string that contains the mark and cell location they would like to pick
    pass


