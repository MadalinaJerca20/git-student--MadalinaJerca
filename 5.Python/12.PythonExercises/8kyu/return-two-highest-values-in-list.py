def two_highest(nums):
    if not nums:
        return []
    elif isinstance(nums, str):
        return False
    return sorted(set(nums), reverse=True)[:2]


print(two_highest([15, 20, 20, 17]), [20, 17])


'''
# Details
    In this kata, your job is to return the two distinct highest values in a list. If there're less than
    2 unique values, return as many of them, as possible.
    The result should also be ordered from highest to lowest.
        Examples:
        [4, 10, 10, 9]  =>  [10, 9]
        [1, 1, 1]  =>  [1]
        []  =>  []

# Exemplu 1
return False if isinstance(list, str) else sorted(set(list), reverse=True)[0:2]
'''
