from math import sqrt


def square_or_square_root(arr):
    return list(map(lambda num: sqrt(num)
                    if has_integer_sqrt(num) else num**2, arr))


def has_integer_sqrt(num):
    return int(sqrt(num)) == sqrt(num)


tests = [
    [[4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]],
    [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
    [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
]

for inp, exp in tests:
    print(square_or_square_root(inp), exp)


'''
# Details
    Write a method, that will get an integer array as parameter and will process every number from this
    array. Return a new array with processing every number of the input-array like this:
    If the number has an integer square root, take this, otherwise square the number.
        [4,3,9,7,2,1] -> [2,9,3,49,4,1]
    The input array will always contain only positive numbers and will never be empty or null.
    The input array should not be modified!

# Exemplu 1
def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result

# Exemplu 2
from math import sqrt

def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]
'''
