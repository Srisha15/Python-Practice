def greet():
    print("Hello")
    print("How do you do?")
    print("Have a nice day ahead")


def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Have a nice day ahead " + name)

def greet_with_name(name,location):
    print(f"Hello {name}")
    print(f"How is {location}")
    print(f"How do you do {name}?")


greet_with_name(location = "LA" , name = "Jack Bauer")# Functions with Keyword parameter
greet_with_name("LA","SS")# Functions with positional paramete
greet_with_name("lucky")