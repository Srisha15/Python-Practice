def is_leap_year(year):
    # if year % 4 != 0:
    #     return False
    # if year % 100 == 0:
    #     if year % 400 == 0:
    #         return True
    # return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2400))
print(is_leap_year(1989))
