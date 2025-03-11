import art
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

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("Enter the first number"))

    while should_accumulate:
        # num1 = float(input("Enter the first number"))
        for symbols in operations:
            print(symbols)
        operation_symbol = input('Enter the operation')
        num2 = float(input("Enter the second number"))

        res1 =operations[operation_symbol](num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {res1}')
        print(f"Your result is: {res1}")

        choice = input(f"Do you want to continue working with the previous result? {res1} y or n").strip().lower()

        if choice == "y":
            num1 = res1
        else:
            should_accumulate = False
            print("\n")
            calculator()

calculator()



