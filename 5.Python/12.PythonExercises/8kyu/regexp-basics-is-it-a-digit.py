def is_digit(n):
    return n.isdigit() and len(n) == 1


print(is_digit(""))
print(is_digit("7"))
print(is_digit(" "))
print(is_digit("a"))
print(is_digit("a5"))


'''
# Details
    Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given
    object is a digit (0-9), false otherwise.

# Exemplu 1
def is_digit(n):
    try:
        if int(n) < 10 > 0 and len(n) == 1:
            return True
        else:
            return False
    except:
        return False
'''
