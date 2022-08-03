# Import the random module here
import random

# Create cards dictionary
cards = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

# Define a string variable 
reportScore = '{}'


# Use the random.choice() function to draw a single card name from the cards dictionary.
def getCard():
  draw = random.choice(list(cards.values()))
  return draw




# Declare declareWinner().  It has two arguments.
def declareWinner(playerOneScore, playerTwoScore):
  if playerOneScore == playerTwoScore:
    print("Its a draw!")
  elif playerTwoScore > 21:
    print("Player one won!")
  elif playerOneScore > 21:
    print("Player two won!")
  elif playerOneScore > playerTwoScore:
    print("Player one won!")
  elif playerTwoScore > playerOneScore:
    print("Player two won!")





def playHand(playerTurn):
  # Initialize the score of the current hand
  score = 0
  game_continue = True
  # Print out the playerTurn
  print()
  print(f"It is {playerTurn}'s turn")
  # Deal two cards and add the scores
  score = getCard() + getCard()
  # If the score is 21, display "Blackjack!" and return that score
  if score == 21:
    print("You hit the Blackjack!")
    return score
  elif score > 21:
    print("You've busted")
    return score
  print(f"Your current score is {score}.")
  
  
  #while True:
  while game_continue:
    print()
    if score == 21:
      print("You hit the Blackjack!")
      return score
    # if the score is bigger than 21 display "You bust!"  Return score.  
    elif score > 21:
      print("You've busted")
      return score
    # Ask if the player wants to hit or stay.  Get the user input.
    dealAgain = input('Do you want to deal again? Enter "hit" or "stay": ')
    # if they 'hit', get a card and add the score to the running total score
    # and continue the loop
    if dealAgain == "hit":
      # Deal an additional card and add it to the score
      score += getCard()
      # Report the current score using reportScore in a format() string
      print(f'Your new score is {score}')
      # return score
    # else if they 'stay' print a blank line and break out of the while loop
    elif dealAgain == "stay":
      return score
    # else if they enter neither 'hit' nor 'stay', display 'Invalid entry
    else:
      print("That is an invalid entry.")
  # return the final score of the hand  
  return score

      


def playGame():
  playerOneScore = 0
  playerTwoScore = 0
  playerOneScore = playHand("Player One")
  if playerOneScore < 22 and playerOneScore != 21:
    playerTwoScore = playHand("Player Two")
  declareWinner(playerOneScore, playerTwoScore)



def main():
  play = True
  while play:
    print()
    play = input("Do you want to play a 2-player hand of Blackjack? ")
    if play == "yes" or play == "Yes":
      playGame()
    elif play == "no" or play == "No":
      print("Goodbye!")
      play = False




main()



  
    
        
            

            

            
            
            
            
