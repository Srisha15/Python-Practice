def format_name(f_name, l_name):
    # formatName = f_name.title()+" " + l_name.title()
    # return formatName
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"


print(format_name("SRisha","SHArma"))