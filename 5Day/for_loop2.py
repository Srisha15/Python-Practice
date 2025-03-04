numb = [10,20,3,4,1,13,123,44,1000,34,2]
print(sum(numb))
sum = 0
for x in numb:
    sum += x
print(sum)



print(max(numb))
highest = 0
for y in numb:
    if y > highest:
        highest = y
print(highest)

"""
highest = numb[0]
for i in range(len(numb) +1 ):
    j = i + 1
    if numb[j] > numb[i] :
        highest = numb[j]
    i = i + 1

print(highest)
since for loop iterates thriugh each number why do you use indexes to access an compare them
store the max value only and compare with the current values
"""
