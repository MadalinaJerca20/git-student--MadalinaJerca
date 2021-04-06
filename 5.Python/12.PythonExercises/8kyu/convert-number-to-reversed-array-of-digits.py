def digitize(n):
    return [int(x) for x in str(n)][::-1]


print(digitize(35231), [1, 3, 2, 5, 3])


'''
# Details
    Given a random non-negative number, you have to return the digits of this number within an array in
    reverse order.
        Example:
        348597 => [7,9,5,8,4,3]

# Exemplu 1
def digitize(n):
    return map(int, str(n)[::-1])
'''
