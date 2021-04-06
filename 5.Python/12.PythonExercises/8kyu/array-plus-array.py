def array_plus_array(arr1, arr2):
    counter = 0
    for i in arr1:
        counter += i
    for i in arr2:
        counter += i
    return counter


print(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
print(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
print(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
print(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)


'''
# Details
    I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their
    elements. I'll appreciate for your help.
    P.S. Each array includes only integer numbers. Output is a number too.

# Exemplu 1
def array_plus_array(arr1,arr2):
    counter = 0
    for i in arr1:
        counter += i
    for i in arr2:
        counter += i
    return counter
'''
