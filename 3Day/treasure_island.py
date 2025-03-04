print('''  
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
      
      ''')

print('''Welcome to Treasure Island 
         Your mission is to find the Treasure!!
         Good Luck out there!!''')
ch1 = input('You have started your\'e journey! Which direction do you go? "Left" or "Right" ').lower()
if ch1 == "right":
    print("You find a light and continue to walk")
    ch2 = input('You proceed to walk in the island and reach to the point where you see the sea, Would you like to "swim" or "wait?" ').lower()
    if ch2 == "swim":
        print('''Oops! You got chewed up by a Shark!! There's blood in the sea now, Eww!!
              Game Over!''')
    elif ch2 == "wait":
        ch3 = input('You find a empty boat in coming towards your direction, you get into the boat an sail the sea'
                    'You reach the other side of the sea and walk for some time until you reach a house with three doors of three colours.'
                    'Which coloured door would you pick? "Red", "Green" or "Yellow" ').lower()
        if ch3 == "red":
            print("You got pranked by a Youtuber! sad to be you")
        elif ch3 == "green":
            print("You found the Treasure!! Congragulations buddy!!")
        elif ch3 == "yellow":
            print("You found a large number of kittens!! God loves you buddy!!")
        else:
            print("Dude you neeed to type in the coreect response! I'm dissapointed in you...")
    else:
        print("Did you even read the Question? *slapping on the face emoji* ")
elif ch1 == "left":
    print('''Oops! You slip and fall off the hill
          Game Over!!''')
else:
    print("Wrong Response!Try Again")
    
