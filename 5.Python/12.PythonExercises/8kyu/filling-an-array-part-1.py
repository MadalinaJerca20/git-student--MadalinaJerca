def arr(n=0):
    return list(range(n))


print(arr(4))
print(arr(0))
print(arr())


'''
# Details
    We want an array, but not just any old array, an array with contents!
    Write a function that produces an array with the numbers 0 to N-1 in it.
    For example, the following code will result in an array containing the numbers 0 to 4:
        arr(5) // => [0,1,2,3,4]

# Exemplu 1
def arr(n=0):
    return [i for i in range(n)]

# Exemplu 2
def arr(n=0):
    # [ the numbers 0 to N-1 ]
    aux = []
    for x in range(n):
        aux.append(x)
    return aux
'''
