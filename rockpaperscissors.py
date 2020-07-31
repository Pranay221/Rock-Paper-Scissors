from random import *
from tkinter import *

#choice section
def userChoiceRock():
    userChoice = "rock"
    turn(userChoice)
    userImage.configure(image = rockImage)

def userChoicePaper():
    userChoice = "paper"
    turn(userChoice)
    userImage.configure(image = paperImage)

def userChoiceScissors():
    userChoice = "scissors"
    turn(userChoice)
    userImage.configure(image = scissorsImage)

#gameplay setion
def turn(userChoice):
    opponent = ['rock', 'paper', 'scissors']
    opponentChoice = opponent[randint(0,2)]

    if(opponentChoice == 'rock'):
        opponentImage.configure(image = rockImage)
    elif(opponentChoice == 'paper'):
        opponentImage.configure(image = paperImage)
    else:
        opponentImage.configure(image = scissorsImage)

    if(opponentChoice == userChoice):
        turnResult.configure(text = "It's a draw.", fg = "gray")
        compare.configure(text = "=")
    elif((opponentChoice == 'rock' and userChoice == 'scissors') or (opponentChoice == 'paper' and userChoice == 'rock') or (opponentChoice == 'scissors' and userChoice == 'paper')):
        turnResult.configure(text = "You are defeated!", fg = "red")
        compare.configure(text="<")
    else:
        turnResult.configure(text = "You win!", fg = "green")
        compare.configure(text = ">")

#main program
root = Tk()
root.title("Rock-Paper-Scissors by Pranay")
rockButton = Button(root, width = 20, text = "ROCK!", justify = CENTER, command = userChoiceRock, activebackground = 'black', activeforeground = 'white')
paperButton = Button(root, width = 20, text = "PAPER!", justify = CENTER, command = userChoicePaper, activebackground = 'black', activeforeground = 'white')
scissorsButton = Button(root, width = 20, text = "SCISSORS!", justify = CENTER, command = userChoiceScissors, activebackground = 'black', activeforeground = 'white')

#images
rockImage = PhotoImage(file = "rps/rock.gif")
paperImage = PhotoImage(file = "rps/paper.gif")
scissorsImage = PhotoImage(file = "rps/scissors.gif")
userImage = Label(image = rockImage)
userImage.image = rockImage
compare = Label(root, justify = CENTER, font = ("Helvetica", 30) )
opponentImage = Label(image = paperImage)
opponentImage.image = paperImage
turnResult = Label(root, width = 20, justify = CENTER, font = ("Helvetica", 20) )

#Tk GUI grid
rockButton.grid(row = 2, column = 1)
paperButton.grid(row = 2, column = 2)
scissorsButton.grid(row = 2, column = 3)
userImage.grid(row = 3, column = 1)
compare.grid(row = 3, column = 2)
opponentImage.grid(row = 3, column = 3)
turnResult.grid(row = 4, column = 2)

#mainloop
root.mainloop()
