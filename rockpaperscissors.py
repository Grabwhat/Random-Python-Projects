import random
def rockpaperscissors():
    choices = {
        "rock": "paper", 
        "rock": "water",
        "rock": "air",
        
        "paper": "scissors",
        "paper": "fire",
        "paper": "sponge", 

        "scissors": "rock", 
        "scissors": "fire",
        "scissors": "water", 
        
        "fire":"air",
        "fire": "water",
        "fire": "rock",

        "water": "sponge",
        "water": "paper",
        "water": "air",

        "sponge": "fire",
        "sponge": "scissors",
        "sponge": "rock",
        
        "air": "paper",
        "air": "sponge",
        "air": "scissors"
    }

    com_choice = random.choice(list(choices))
    p_choice = input("\nRock, Paper, Scissors, Fire, Water, Air, or Sponge?\n")

    if p_choice.lower() not in choices:
        print("Invalid Choice!")
            
    print("\nRock..Paper...Scissors....Shoot!\n")
    print(f"Computer plays {com_choice.capitalize()}, you chose {p_choice.capitalize()}!\n")

    if p_choice == com_choice:  
        print("It's a tie!")
        return "tie"
        
    elif choices[p_choice] == com_choice:
        print("Computer Won!")
        return "lost"

    else:
        print("You Won!")
        return "won"
    

def win_loss(score1):
    return "\nPlayer Wins!" if score1 == 3 else "\nComputer Wins!"

def main():
    player_score = 0
    computer_score = 0

    while (player_score != 3 and computer_score != 3):
        print(f"{player_score} : {computer_score}")
        result = rockpaperscissors()
        if result == "tie":
            continue
        elif result == "lost":
            computer_score += 1
        else:
            player_score += 1

    
    print(win_loss(player_score))
    print(f"\nPlayer: {player_score} \nComputer: {computer_score}")


    
if __name__ == "__main__":
     playing = True
     
     while playing:
          main()

          again = input("\nDo you want to calculate again? (Y/N): ")
          
          while True:
               if again in "yY":
                    break
               
               elif again in "nN":
                    print("\nGoodbye!\n")
                    playing = False
                    break
               
               else:
                    print("\nInvalid input.")
                    continue