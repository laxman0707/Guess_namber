#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
easy_level_turns=10
hard_level_turns=5

def checkanswer(guess,answer,turns):
  if guess>answer:
    print("Too high")
    return turns-1
  elif guess<answer:
    print("too low")
    return turns-1
  else:
    print(f"you got it the correct answer and the answer is{answer}")
def setdifficulty():
  level=input("choose a diificulty easy or hard:")
  if level=="easy":
    return easy_level_turns
  elif level=="hard":
    return hard_level_turns
  else:
    return 'inavlid_guess'
    
def game():
    print("welcome to the guessing name")
    print("iam thinking a number between 1 and 100")
    answer=random.randint(1,100)
    print(answer)
    turns=setdifficulty()
    #if turns=="easy" or turns=="hard":
    print(f"you have{turns} attempts remaining to gguess number")
    guess=0
    while guess!=answer:
       guess=int(input("Make a guess:"))
       turns=checkanswer(guess,answer,turns)
       if turns==0:
          print("yours turns over you loose")
          return
       elif guess!=answer:
          print("Guess again.")
  #else:
    #print("Invalid guess")

      
game()


