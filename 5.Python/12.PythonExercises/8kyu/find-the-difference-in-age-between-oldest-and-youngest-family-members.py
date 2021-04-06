def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))


print(difference_in_ages([5, 8, 72, 98, 41, 16, 55]), (5, 98, 93))
print(difference_in_ages([57, 99, 14, 32]), (14, 99, 85))
print(difference_in_ages([0, 110]), (0, 110, 110))
print(difference_in_ages([33, 33, 33]), (33, 33, 0))


'''
# Details
    At the annual family gathering, the family likes to find the oldest living family member’s age and
    the youngest family member’s age and calculate the difference between them.
    You will be given an array of all the family members' ages, in any order. The ages will be given in
    whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0. Return a new array (a tuple
    in Python) with [youngest age, oldest age, difference between the youngest and oldest age].

# Exemplu 1
def difference_in_ages(ages):
    x, y = min(ages), max(ages)
    return x, y, y-x

# Exemplu 2
def difference_in_ages(ages):
    age = sorted(ages)
    return (age[0], age[-1], (age[-1]-age[0]))

# Exemplu 3
def difference_in_ages(a):
    L=[]
    L.append(min(a))
    L.append(max(a))
    L.append(max(a)-min(a))
    return tuple(L)
'''
