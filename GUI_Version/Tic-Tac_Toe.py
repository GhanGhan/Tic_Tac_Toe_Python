import tkinter as tkr

# Create game (root) window
game = tkr.Tk()
game.geometry("500x500")
game.title('Tic-Tac-Toe')
button = tkr.Button(game, text='Welcome to Tic-Tac-Toe! \nPlayer 1 is "X", Player 2 is "O".\nClick this button when you are ready to play!!', 
                   width = 35, height= 4)
button.pack()

game.mainloop()