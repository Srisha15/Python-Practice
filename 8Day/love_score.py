def calculate_love_score(name1 , name2):
    name = name1 + name2
    sum1 = 0
    sum2 = 0
    for i in name:
        if i == 't' or i == 'r' or i == 'u' or i == 'e':
            sum1 += 1
        if i =='l' or i == 'o' or i == 'v' or i == 'e':
            sum2 += 1
    print(f"Your love score is:\n{sum1}{sum2}")
calculate_love_score("cheeku","cherry")
