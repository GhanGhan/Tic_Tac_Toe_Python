import gamePlay

# Welcome Both players to the game
print("\nWelcome to Tic-Tac-Toe!!!!!! \nPlayer 1 is \"X\", Player 2 is \"O\"! ")
print("Type \"G\" then press \"Enter\" when you are ready to play!")

key = ""

while key != "G":
    key = input(": ")
    if key != "G":
        print("Invalid input, please enter the character \"G\"")

print("Alright, lets start the game!!!")
gamePlay.showGrid()

