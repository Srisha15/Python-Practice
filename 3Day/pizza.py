print("Welcome to Python pizza delivery")
size = input("What size of pizza do you want? s, m or l")
if size == "s":
    bill = 15
    print("Small Pizza costs $15")
elif size == "m":
    bill = 20
    print("Medium pizaa costs $20")
elif size == "l":
    bill = 25
    print("Large pizza costs $25")
else:
    print("Try again!!")
pepperoni = input("Do you want pepperoni on your pizza? y or n")
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
print(f"Addition of Pepperoni would be {bill}")
extra_cheese = input("Do you want extra cheese? y or n")
if extra_cheese == "y":
    bill += 1
print(f"Your final bill is {bill}")
print("Thank you visit again!!")
      


