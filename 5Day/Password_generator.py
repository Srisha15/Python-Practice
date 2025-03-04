import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_l= int(input("How many letters would you like in your password?\n")) 
nr_s = int(input(f"How many symbols would you like?\n"))
nr_n = int(input(f"How many numbers would you like?\n"))
"""
for _ in range(nr_l + 1):
    print(random.choice(letters), end= "")
for _ in range(nr_s + 1):
    print(random.choice(numbers), end= "")
for _ in range(nr_n + 1):
    print(random.choice(symbols), end= "")
"""

#store the password!!!!! easy way
"""
password = ""
for _ in range(nr_l + 1):
    password += random.choice(letters)
for _ in range(nr_s + 1):
    password += random.choice(numbers)
for _ in range(nr_n + 1):
    password += random.choice(symbols)
print(password)
"""
#hard way
password = []
for _ in range(nr_l + 1):
    password.append(random.choice(letters))
for _ in range(nr_s + 1):
    password.append(random.choice(numbers))
for _ in range(nr_n + 1):
    password.append(random.choice(symbols))
#print(password)
random.shuffle(password)
#print(password)
"""for x in password:
    print(x, end = "")"""

final_pw = ""
for char in password:
    final_pw += char
print(f"Your Pasword is {final_pw}")

