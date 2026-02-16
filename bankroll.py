print("\033[1;38;2;0;0;255m-------      \033[0m"*4)
print("\033[38;2;255;0;0m|START |     |agra |      |tripura |    |jail  |\033[0m")
print("\033[1;38;2;0;0;255m-------      \033[0m"*4)
print("\033[1;38;2;0;255;0m|   ara     |",end="        ")
print("              |     goa   |")

print()
print("|  jaipur   |",end="        ")
print("              |    delhi  |")
print()
print("| sitamarhi |",end="        ")
print("              |    fine   |\033[0m")
print("\033[1;38;2;0;0;255m-------       \033[0m"*4)
print("\033[38;2;255;0;0m|end   |     |kaimur  |     |usa  |      |bank  |\033[0m")
print("\033[1;38;2;0;0;255m-------       \033[0m"*4)

# user1=input("enter your name: ")
# user2=input("enter second name: ")
            
import random

amount = 500
amount2 = 500
i = 0

while i < 4:

    print("\033[1;38;2;255;0;0m Player 1 Turn")
    user1 = random.randint(1, 6)
    print("Dice:", user1)

    if user1==1 or user1==2 or user1==3 :
        h = input("Player 1 - Buy yes or no: ")
        if h== "yes":
            amount -= 50
            print("Player 1 Amount:", amount)
        else:
            print("Go ahead!")

    elif user1 == 4:
        amount -= 10
        print("Deducted Player 1 Amount:", amount)

    else:
        h = input("Player 1 - Buy yes or no : ")
        if h== "yes":
            amount -= 100
            print("Player 1 Amount:\033[0m", amount)


    print("\033[1;38;2;0;0;255m Player 2 Turn ")
    user2 = random.randint(1, 6)
    print("Dice:", user2)

    if user2 == user1:
        amount2 -= 100
        amount=amount+100
        print(" Player 2 Amount:", amount2)

    elif user2==1 or user2==2 or user2==3:
        h = input("Player 2 - Buy (yes/no): ")
        if h== "yes":
            amount2 -= 50
            print("Player 2 Amount:", amount2)
        else:
            print("Go ahead!")

    elif user2 == 4:
        amount2 -= 10
        print("Deducted! Player 2 Amount:", amount2)

    else:
        h = input("Player 2 - Buy? (yes/no): ")
        if h== "yes":
            amount2 -= 100
            print("Player 2 Amount: \033[0m", amount2)

    i += 1

print("GAME OVER")
print("Player 1 Final Amount:", amount)
print("Player 2 Final Amount:", amount2)
if amount>amount2:
    print("\033[3;38;2;20;40;4;48;2;0;20;40m ")
    print(r'''           /$$                                          /$$                       /$$                                        
          | $$                                        /$$$$                      |__/                                        
  /$$$$$$ | $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$|_  $$         /$$  /$$  /$$ /$$ /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$ | $$        | $$ | $$ | $$| $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/ | $$        | $$ | $$ | $$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$ /$$__  $$| $$  | $$| $$_____/| $$       | $$        | $$ | $$ | $$| $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      /$$$$$$      |  $$$$$/$$$$/| $$| $$  | $$| $$  | $$|  $$$$$$$| $$      
| $$____/ |__/ \_______/ \____  $$ \_______/|__/     |______/       \_____/\___/ |__/|__/  |__/|__/  |__/ \_______/|__/      
| $$                     /$$  | $$                                                                                           
| $$                    |  $$$$$$/                                                                                           
|__/                     \______/                                                                                            
   ''')
    print("\033[0m")
          
elif amount<amount2:
    print("\033[3;38;2;10;10;10m ")
    print(r'''           /$$                                         /$$$$$$                      /$$                                        
          | $$                                        /$$__  $$                    |__/                                        
  /$$$$$$ | $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$|__/  \ $$       /$$  /$$  /$$ /$$ /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$$$$$/      | $$ | $$ | $$| $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__//$$____/       | $$ | $$ | $$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$ /$$__  $$| $$  | $$| $$_____/| $$     | $$            | $$ | $$ | $$| $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$     | $$$$$$$$      |  $$$$$/$$$$/| $$| $$  | $$| $$  | $$|  $$$$$$$| $$      
| $$____/ |__/ \_______/ \____  $$ \_______/|__/     |________/       \_____/\___/ |__/|__/  |__/|__/  |__/ \_______/|__/      
| $$                     /$$  | $$                                                                                             
| $$                    |  $$$$$$/                                                                                             
|__/                     \______/                                                                                              
  ''')
    print("\033[0m")
else:
    print(r"""    ___
                 _\  \_
                  /__|     
              ___//_        
             /      \       MATCH DRAW!
            /        \/\    
           / /\     \/  )   
           \_\|     |  /    
            (_      |\/
              |     |
              |_    |
               /   |
              / /| |
             /_/ |_|
            /|    /\
    _______/_/____\_\_________________________      """)  
