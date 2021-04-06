def check(a, x):
    if x in a:
        return True
    else:
        return False


def example_tests():
    print(check([66, 101], 66))
    print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
    print(check(['t', 'e', 's', 't'], 'e'))
    print(check(['what', 'a', 'great', 'kata'], 'kat'))


'''
# Details
    You will be given an array (a) and a value (x). All you need to do is check whether the provided array
    contains the value, without using a loop. Array can contain numbers or strings. X can be either. Return
    true if the array contains the value, false if not. With strings you will need to account for case.

# Exemplu 1
def check(a, x):
    return x in a

# Exemplu 2
def check(a, x):
    return True if x in a else False

# Exemplu 3
def check(a, x):
    try:
        return x in a
    except TypeError:
        return x == a
'''
