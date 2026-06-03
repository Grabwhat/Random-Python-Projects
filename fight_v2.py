import random
class Main:
        def fight():
            classes  = [
                #[class, HP, damage, heal]
                ["Berserker", 110, (10, 17), (4, 10)],
                ["Archer", 90, (5, 25), (5, 14)],
                ["Mage", 80, (15, 18), (6, 16)],
                ["Tank", 130, (4, 12), (6, 13)],
                ["Healer", 120, (4, 14), (11, 21)],
                ["Chad", 1000, (40, 100), (50, 100)]
                        ]
            
            character = input("Choose your character:\n " \
            "\n1. Berserker: HP 110, Damage 10 - 17, Heal 4 - 10\n " \
            "\n2. Archer: HP 90, Damage 5 - 25, Heal 5 - 14\n " \
            "\n3. Mage: HP 80, Damage 15 - 18, Heal 6 - 16\n " \
            "\n4. Tank: HP 130, Damage 4 - 12, Heal 6 - 13\n " \
            "\n5. Healer: HP 120, Damage 4 - 14, Heal 11 - 21\n" \
            "\n6. Chad: HP 1000, Damage 40 - 100, Heal 50 - 100\n" \
            "\nWhich one will you choose? (1-6) ")

            ogplayerhp = classes[int(character)-1][1]
            ogbosshp = ogplayerhp + 15

            playerhp = classes[int(character)-1][1]
            bosshp = playerhp + 15

            stats = classes[int(character)-1]
            dmg = stats[2]
            heal = stats[3]

            print(f"\nYou are now a {stats[0]}.")
            print("Fight The Boss!\n")
            print(f"Your HP: {playerhp}")
            print(f"Boss HP: {bosshp}\n")

            while playerhp > 0 and bosshp > 0:
                  
                  playerdmg = random.randint(dmg[0], dmg[1]) 
                  bossdmg = random.randint(dmg[0]-3, dmg[1]+1)
                  playerheal = random.randint(heal[0], heal[1])
                  bossheal = random.randint(heal[0]+3, heal[1]+1)
                  bossmove = random.randint(1, 4)
                
                  decision = input("Attack or Heal? ")
    
                  if decision == "Attack" or decision == "attack":
                    print(f"\nYou dealt {playerdmg} damage!")
                    if bossmove in range(1, 4):
                        print(f"Boss dealt {bossdmg} damage to you!\n")
                        playerhp -= bossdmg
                    elif bosshp != ogbosshp and bossmove == 4:
                        print(f"Boss Healed {bossheal} HP!\n")
                        bosshp += bossheal
                    else:
                        print(f"Boss dealt {bossdmg} damage to you!\n")
                        playerhp -= bossdmg

                    bosshp -= playerdmg
                    
                    print(f"Your HP: {playerhp}")
                    print(f"Boss HP: {bosshp}\n")


                  elif decision == "Heal" or decision == "heal":
                    if playerhp != ogbosshp:
                        print(f"\nYou healed {playerheal} HP!")
                        if bossmove in range(1, 4):
                            print(f"Boss dealt {bossdmg} damage to you!\n")
                            playerhp -= bossdmg
                        elif bosshp != ogbosshp and bossmove == 4:
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
                print(f"You Lost, {stats[0]}! Your death will not be in vain.")
            else:
                print(f"You Won, {stats[0]}! You will be remembered as a hero.")

        fight()