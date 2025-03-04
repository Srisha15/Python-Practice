import random
print(''' Let's Toss a Coin!!
           Are you Ready?
           Let's Go''')
random_choice = random.randint(0,1)
if random_choice == 0:
    print("Tails")
else:
    print("Heads")