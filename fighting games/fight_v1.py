import random
class Main:
        def fight():
            
            playerhp = 100
            bosshp = 100

            print("\nFight The Boss!\n")
            print("Your HP: 100")
            print("Boss HP: 100\n")

            while playerhp > 0 and bosshp > 0:
                  
                  playerdmg = random.randint(4, 10) 
                  bossdmg = random.randint(3, 11)
                  playerheal = random.randint(3, 15)
                  bossheal = random.randint(2, 13)
                  bossmove = random.randint(1, 4)
                
                  decision = input("Attack or Heal? ")
    
                  if decision == "Attack" or decision == "attack":
                    print(f"\nYou dealt {playerdmg} damage!")
                    if bossmove in range(1, 4):
                        print(f"Boss dealt {bossdmg} damage to you!\n")
                        playerhp -= bossdmg
                    elif bosshp != 100 and bossmove == 4:
                        print(f"Boss Healed {bossheal} HP!\n")
                        bosshp += bossheal
                    else:
                        print(f"Boss dealt {bossdmg} damage to you!\n")
                        playerhp -= bossdmg

                    bosshp -= playerdmg
                    
                    print(f"Your HP: {playerhp}")
                    print(f"Boss HP: {bosshp}\n")


                  elif decision == "Heal" or decision == "heal":
                    if playerhp != 100:
                        print(f"\nYou healed {playerheal} HP!")
                        if bossmove in range(1, 4):
                            print(f"Boss dealt {bossdmg} damage to you!\n")
                            playerhp -= bossdmg
                        elif bosshp != 100 and bossmove == 4:
                            print(f"Boss Healed {bossheal} HP!\n")
                            bosshp += bossheal
                        else:
                            print(f"Boss dealt {bossdmg} damage to you!\n")
                            playerhp -= bossdmg
                    else:
                        print("\nYou cannot heal anymore!\n")
                        
                    print(f"Your HP: {playerhp}")
                    print(f"Boss HP: {bosshp}\n")

            if playerhp <= 0 and bosshp <= 0:
                print("You both lost! (or you both won)")
            elif playerhp <= 0:
                print("You Lost! Your death will not be in vain.")
            else:
                print("You Won! You will be remembered as a hero.")

        fight()