print("Welcome to the Ticket Centre!")
height = int(input("Enter your Height in cm\n"))
bill = 0
if height > 120:
    print("You can ride! Welcome!!")
    age = int(input("Enter your age\n"))
    if age < 12:
        print("Kids Ticket costs $5")
        bill = 5
    elif age < 18:
        print("Teens Ticket costs $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Cheer up! You get to have free rides!!")
        bill = 0
    else:
        print("Adults Ticket costs$12")
        bill = 12
    photo = input("Do you want to have a photo taken? y for Yes, n for No\n")
    if photo == "y":
        bill += 3
    number = int(input("How many tickets do you want?\n"))
    bill *= number
    print(f"Your final bill is ${bill}")
else:
    print("Sorry! Come back when you grow up!!")
