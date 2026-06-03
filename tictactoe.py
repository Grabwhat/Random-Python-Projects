# UNFINISHED - WORK IN PROGRESS ******************

import turtle
import random

# Create 2 Turtles
player1 = turtle.Turtle()
player2 = turtle.Turtle()


# Define function to draw a board
def newBoard():
  board = [0] * 9
  print(board)
  


# Define functions to draw an X
def drawX(turtle):
  pass


# Define functions to draw an O
def drawO(turtle):
  pass

def drawposition(position, player):
    """
    Determines if player1 or player2 was passed in as parameter, assign player_code accordingly.
    Takes the player's turtle to its respective position on the board.
    Draws either X or O according to the player's assigned shape.
    :param position:
    :param player:
    :return: None
    """

    # *** COMPLETE CODE BELOW ***

    # Conditional Branch to take player to the respective square
    # if position == 1:
    #   player.goto(___,___)
    # elif position == 2:
    #   ...
      
    # if player == player1:
    #   board[position] = "X"
    # elif player == player2:
    #   board[position] = "O"




if __name__ == "__main__":
    # Draw a new board and declare what shape each player is
    newBoard()
    print("Player 1 is X, Player 2 is O")

    # Simulate a coin flip by using random.randint() 
    # 0 means player1 means first, 1 means player2 goes first 
    coin_flip = random.randint(0, 1)

    # Start the game loop
    gameloop = True
    while gameloop == True:
	
      # if it is player1's turn:
      # ask what position they want to cast and call drawposition()
      if coin_flip == 0:
        place = input("Choose a number from 0-9 according to the board: ")
        drawposition(place,"X")
      else:
         pass
        
      # elif it is player2's turn:
      # ask what position they want to cast and call drawposition()