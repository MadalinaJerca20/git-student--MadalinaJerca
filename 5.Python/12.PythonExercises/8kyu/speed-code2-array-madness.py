def array_madness(a, b):
    return sum(x**2 for x in a) > sum(x**3 for x in b)


print(array_madness([4, 5, 6], [1, 2, 3]), True)
print(array_madness([1, 2, 3], [4, 5, 6]), False)


'''
# Details
    Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of
    the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
        E.g.
        array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
    Get your timer out. Are you ready? Ready, get set, GO!!!

# Exemplu 1
def array_madness(a,b):
    return sum(map(lambda a: a ** 2, a)) > sum(map(lambda b: b ** 3, b))

# Exemplu 2
def array_madness(a,b):
    squaresA = 0
    cubesB = 0
    for i in range(len(a)):
        squaresA += pow(a[i], 2)
    for j in range(len(b)):
        cubesB += pow(b[j], 3)
    return squaresA > cubesB
'''
