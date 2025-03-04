print("Welcome to the tip calculator!\n")
total = float(input("What was the total bill?\n "))
tip = int(input("How much percentage of tip would you like to give?\n"))
tip_percent = tip / 100
total_amt = total*tip_percent + total
share = int(input("How many people will share the bill?\n"))
amount = total_amt / share
print(f"Each person has to pay ${round(amount,2)}")