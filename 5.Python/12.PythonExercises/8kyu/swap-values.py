def swap_values(args):
    temp = args[1]
    args[1] = args[0]
    args[0] = temp


arr = [1, 2]
swap_values(arr)
print(arr, [2, 1])


'''
# Details
    I would like to be able to pass an array with two elements to my swapValues function to swap the
    values. However it appears that the values aren't changing. Can you figure out what's wrong here?

# Exemplu 1
def swap_values(args):
    args[0], args[1] = args[1], args[0]

# Exemplu 2
def swap_values(arr):
    arr.reverse()

# Exemplu 3
def swap_values(args):
    args[:]=args[::-1]
'''
