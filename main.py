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

#Write your code below this line 👇

choice_1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n').lower()

death_1 = "You weren't paying attention and fell in a hole. Good job. Game Over."
death_2 = "You weren't fast enough. A pack of carnivorous tuna have attacked. Game over."

if choice_1 == "left":
  choice_2 = input('You\'ve arrived at a mysterious body of water. You can see an island a few hundred yards away. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice_2 == "wait":
    choice_3 = input('After some time, a boat arrives and takes you to the island. You see three houses, each with a different color door. Type "blue", "red", or "yellow" to choose.\n').lower()
    if choice_3 == "blue":
      print("You enter the blue door and are bludgeoned by smurfs drinking koolaid. Game Over.")
    elif choice_3 == "red":
      print("You enter the red door. It locks behind you and the entire house is engulfed in flames. Game Over.")
    elif choice_3 == "yellow":
      print("You've done it! The treasure sits in the center of the room in all its shiny glory. Congrats. You win.")
    else:
      print("I guess you can do that, but game over.")
  else:
    print(death_2)
else:
  print(death_1)
  
