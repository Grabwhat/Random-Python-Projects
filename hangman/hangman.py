import json
import random

def main():

    def open_json(file):
        with open(file, "r") as f:
            words = json.load(f)
        return words
    
    #Parameters
    att_left = 8
    stage_num = 0
    word = random.choice(open_json("words.json"))
    incorrect_letters = set()
    guessed_letters = set()
    
    stages = [
         """
          ____________
          |         |
          |         
          |
          |
          |
          |
          |
       ----------------- 
        """,
         """
          ____________
          |         |
          |         O
          |
          |
          |
          |
          |
       ----------------- 
        """,
         """
          ____________
          |         |
          |         O
          |         |
          |
          |
          |
          |
       ----------------- 
        """,
         """
          ____________
          |         |
          |         O
          |         |
          |         |
          |
          |
          |
       ----------------- 
        """,
         """
          ____________
          |         |
          |         O
          |       / |
          |         |
          |        
          |
          |
       ----------------- 
        """,
        """
          ____________
          |         |
          |         O
          |       / | \\
          |         |
          |        
          |
          |
       ----------------- 
        """,
        """
          ____________
          |         |
          |         O
          |       / | \\
          |         |
          |        /
          |
          |
       ----------------- 
        """,
        """
          ____________
          |         |
          |         O
          |       / | \\
          |         |
          |        / \\
          |
          |
       ----------------- 
        """,
    ]
    

    print("\nWelcome to Hangman! Guess wrong, and add part of the body!")
    print("\nGuess either a letter or the whole word!")
    print(stages[0])
    print(f"Attempts Left: {att_left}")
    print("_" * len(word))

    while True:
      guess = input("\nGuess a letter: ")

      if guess.lower() in guessed_letters:
          print("Letter already guessed!")
          continue
      elif guess.lower() in "`1234567890-=~!@#$%^&*()_+[]\}{|;':,./<>?" or guess.lower() in '"':
          print("Guess either a letter or the whole word!")
          continue
      elif guess.lower() not in word:
          display_letters = ""

          incorrect_letters.add(guess)
          guessed_letters.add(guess)
          att_left -= 1
          stage_num += 1

          if att_left == 0:
          
            print("\nYou didn't guess the word!")
            print(f"\nThe word was: {word}\n")
            
            again = input("Do you want to play again? (Y/N): ")
            if again in "yY":
                  
                att_left = 8
                stage_num = 0
                word = random.choice(open_json("words.json"))
                incorrect_letters = set()
                guessed_letters = set()

                continue
              
            elif again in "nN":
                  print("\npeace out\n")
                  break
            elif again not in "yYnN" or again == "":
                  print("Y or N: ")
                  continue

          print("Wrong!")
          print(f"\nAttempts Left: {att_left}")
          print(stages[stage_num])
          print(f"Incorrect Letters: {" ".join(incorrect_letters)}")

          for i in word:
              if i in guessed_letters:
                  display_letters += i
              else:
                  display_letters += "_"

          print(display_letters)

          continue
      
      elif guess.lower() in word:

          display_letters = ""
          guessed_letters.add(guess)

          print("Correct!")
          print(f"\nAttempts Left: {att_left}")
          print(stages[stage_num])
          print(f"Incorrect Letters: {" ".join(incorrect_letters)}")
          
          for i in word:
              if i in guessed_letters:
                  display_letters += i
              else:
                  display_letters += "_"


          print(display_letters)
          
          if display_letters == word or guess == word:
              print("\nYou got the word!\n")
              again = input("Do you want to play again? (Y/N): ")
              if again in "yY":
                  
                  att_left = 8
                  stage_num = 0
                  word = random.choice(open_json("words.json"))
                  incorrect_letters = set()
                  guessed_letters = set()

                  continue
              
              elif again in "nN":
                  print("\npeace out\n")
                  break
              elif again not in "yYnN" or again == "":
                  print("Y or N: ")
                  continue


main()