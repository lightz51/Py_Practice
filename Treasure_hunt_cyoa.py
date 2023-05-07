print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
crossroad = input(("\nYou\'re at a crossroad, where do you go? Left or right?\n")).lower()
if crossroad == "left":
  water = input("\nYou come across a river, do you try to swim or wait for a boat?\n").lower()
  if water == "wait":
    door = input("\nA boat carries you across the shore, now there are three doors in front of you, red, blue and yellow, which door do you choose?\n").lower()
    if door == "yellow":
      print("\nYou find youself in a room filled with gold, YOU WIN!\n")
    elif door == "red":
      print("\nFire Golems burned you, Game Over.\n")
    elif door == "blue":
      print("\nThe room was filled with water and a live wire, Game Over.\n")
    else:
      print("\nYou didn't chose any door, and all three doors fell on you before you can react. Game Over\n")
  else:
    print("\nA trout bit your leg off, and you died from a mixture of blood loss and drowning. Game Over.\n")
else:
  print("\nYou fell into a hole. Game Over.\n")