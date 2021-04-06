from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


tests = [
    [6, [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
]

for exp, inp in tests:
    print(grow(inp), exp)


'''
# Details
    Given a non-empty array of integers, return the result of multiplying the values together in order.
        Example:
        [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# Exemplu 1
def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
'''
