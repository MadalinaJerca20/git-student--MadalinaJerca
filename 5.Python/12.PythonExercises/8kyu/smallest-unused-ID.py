def next_id(arr):
    current_id = 0
    while current_id in arr:
        current_id += 1
    return current_id


print(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
print(next_id([5, 4, 3, 2, 1]), 0)
print(next_id([0, 1, 2, 3, 5]), 4)
print(next_id([0, 0, 0, 0, 0, 0]), 1)
print(next_id([]), 0)


'''
# Details
    You've got much data to manage and of course you use zero-based and non-negative ID's to make each
    data item unique! Therefore you need a method, which returns the smallest unused ID for your next
    new data item. Note: The given array of used IDs may be unsorted. For test reasons there may be
    duplicate IDs, but you don't have to find or remove them!

# Exemplu 1
def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i
'''
