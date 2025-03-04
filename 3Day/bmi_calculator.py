print("Welcome to BMI Calculator!!!")
height = int(input("Enter your Height\n"))
weight = int(input("Enter your weight\n"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 24.9:
    print("normal weight")
else:
    print("overweight")
print("Stay Healthy!!")
