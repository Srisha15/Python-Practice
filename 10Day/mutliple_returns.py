def format_name(f_name, l_name):
    if l_name == "" or f_name == "":
        return  
    # returns none
    # early return terminates the function early without having it go through all the code
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"


print(format_name(input("What is your first name?"), input("Enter your last name?")))