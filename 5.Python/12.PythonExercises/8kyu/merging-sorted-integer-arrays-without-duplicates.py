def merge_arrays(first, second):
    return sorted(set(first + second))


print(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
print(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])


'''
# Details
    Write a function that merges two sorted arrays into a single one. The arrays only contain integers.
    Also, the final outcome must be sorted and not have any duplicate.

# Exemplu 1
def merge_arrays(first, second):
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)
    return sorted(working)
'''
