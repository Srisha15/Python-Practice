def add(n1,n2):
    return n1+n2


my_operation = add
"""storing the function
in order to strore the function do not add the ()
as it triggers the function"""

my_operation(2,3)
# can work instead of add

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


"""add the four functions as values in the dictionary
keys = +,-,*,%"""

operations = {}
operations["+"] = add
operations["-"] = sub
operations["*"] = mul
operations["/"] = div
# print(calculator)


"""use dictionary operations to perform calculations"""

# print(operations["*"](4,8))


"""user input"""
n1 = int(input("Enter the first number"))
operation = input('Enter the operation(a choice of "+", "-", "*" or "/")')
n2 = int(input("Enter the second number"))

m1 =operations[operation](n1,n2)

print("Your result is: "+ m1)

choice = input("Do you want to continue working with the previous result? yes or no").strip().lower()

if choice == "yes":
    operation = input('Enter the operation(a choice of "+", "-", "*" or "/")')
    m2 = int(input("Enter the second number"))
    n1 = operations[operation](m1,m2)
    print("Your result is: "+ n1)


# def calculator(){
#     n1 = int(input("Enter the first number"))
#     operation = input('Enter the operation(a choice of "+", "-", "*" or "/")')
#     n2 = int(input("Enter the second number"))

#     r1 =operations[operation](n1,n2)

#     print("Your result is: "+ m1)

# }


