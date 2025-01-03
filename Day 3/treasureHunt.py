print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
dir1 = input('You are at a crossroad where do you want to go?\n\t Type "left" or "right"\n')
if dir1 == "left" :
    dir2 = input('You have come to a lake. There is an island in the middle of the lake.\n\t Type "wait" to wait for the boat. Type "swim" to swim across.\n')
    if dir2 == "wait" :
        dir3 = input("You arrive at an island unharmed. There is a house with 3 doors.\n\t One red, one yellow and one blue. Which one will you choose?\n")
        if dir3 == "red" :
            print("It's a room full of fire. Game Over")
        elif dir3 == "blue" :
            print("It's a room full of beasts, you have been eaten. Game OVer")
        elif dir3 == "yellow" :
            print("You found the treasure. You WIN!")
        else :
            print("Game Over")
    elif dir2 == "swim" :
        print("You've been attacked by the trout. Game Over.")
    else :
        print("Game Over")
elif dir1 == "right" :
    print("You fell into a hole and hurt your head. Game Over")
else :
    print("Game Over")
