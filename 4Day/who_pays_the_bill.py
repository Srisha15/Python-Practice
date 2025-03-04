import random
members = ["Namjoon","Jin","Yoongi","JHope","Jimin","Taehyung","Jungkook"]

#option1
pay = random.choice(members)
print(f"The Member who has to pay is {pay}")

#option2
len_pay = len(members)
choice = random.randint(0, len_pay-1)
print(members[choice])