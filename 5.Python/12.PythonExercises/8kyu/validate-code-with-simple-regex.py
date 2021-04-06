def validate_code(code):
    return str(code)[0] in '123'


print(validate_code(123))
print(validate_code(248))
print(validate_code(8))
print(validate_code(321))
print(validate_code(9453))


'''
# Details
    Basic regex tasks. Write a function that takes in a numeric code of any length. The function should
    check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
    You can assume the input will always be a number.

# Exemplu 1
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

# Exemplu 2
def validate_code(code):
    return int(str(code)[0]) < 4
'''
