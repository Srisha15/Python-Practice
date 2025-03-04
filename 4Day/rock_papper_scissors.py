import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
             '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''

symbol = [rock,paper,scissors]



print("Let's Play Rock, Paper, Scissors!!!")
uchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors!!\n"))
if uchoice >= 3 or uchoice < 0:
    print("You typed an invalid number!!! You are'nt focused, are you??!!")
else:
    choice = [0,1,2]
    cchoice = random.choice(choice)
    print("Your choice:\n")
    print(symbol[uchoice])
    print("Computer's choice:\n")
    print(symbol[cchoice])
    if uchoice == cchoice:
        print("It's a tie!! You must think like me huhh")
    elif uchoice == 0 & cchoice == 1:
        print("You loose!! Haha")
    elif uchoice == 0 & cchoice == 2:
        print("You win!!")
    elif uchoice == 1 & cchoice == 0:
        print("You Win!!")
    elif uchoice == 1 & cchoice == 2:
        print("I win!!")
    elif uchoice == 2 & cchoice == 0:
        print("I win!!")
    elif uchoice == 2 & cchoice == 1:
        print("You Win!!")
    else:
        print("You typed an invalid number!!! You are'nt focused, are you??!!")
