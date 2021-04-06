def positive_sum(arr):
    return sum(x if x > 0 else 0 for x in arr)


print("works for some examples")
print(positive_sum([1, 2, 3, 4, 5]), 15)
print(positive_sum([1, -2, 3, 4, 5]), 13)
print(positive_sum([-1, 2, 3, 4, -5]), 9)

print("returns 0 when array is empty")
print(positive_sum([]), 0)

print("returns 0 when all elements are negative")
print(positive_sum([-1, -2, -3, -4, -5]), 0)


'''
# Details
    You get an array of numbers, return the sum of all of the positives ones.
    Example [1,-4,7,12] => 1 + 7 + 12 = 20
    Note: if there is nothing to sum, the sum is default to 0.

# Exemplu 1
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum
'''
