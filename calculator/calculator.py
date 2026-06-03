def calculator():
        calculate = input("\nEnter what you want to calculate: ")

        try:
            if -2**31 <= eval(calculate) <= 2**31 - 1:
                print(eval(calculate)) 
            else:
                print("Not in 32-integer bit.")
        
        except:
             print("Error Calculating. Please input again.")

if __name__ == "__main__":
     calculating = True
     
     while calculating:
          calculator()

          again = input("\nDo you want to calculate again? (Y/N): ")
          
          while True:
               if again in "yY":
                    break
               
               elif again in "nN":
                    print("\nGoodbye!\n")
                    calculating = False
                    break
               
               else:
                    print("\nInvalid input.")
                    continue