def array(string):
    parts = string.split(',')[1:-1]
    return ' '.join(parts) if parts else None


print(array(''))
print(array('1'))
print(array('1, 3'))
print(array('1,2,3'))
print(array('1,2,3,4'))


'''
# Details
    This is a spin off of my first kata. You are given a list of character sequences as a comma separated
    string. Write a function which returns another string containing all the character sequences except
    the first and the last ones, separated by spaces. If the input string is empty, or the removal of the
    first and last items would cause the string to be empty, return a null value.

# Exemplu 1
def array(string):
    arr = [elem for elem in string.replace(' ', '').split(',')]
    if len(arr) > 2:
        return " ".join(arr[1:-1])
'''
