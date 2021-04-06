def two_decimal_places(n):
    return round(n, decimals=2)


print(two_decimal_places(4.659725356))
print(two_decimal_places(173735326.3783732637948948))
print(two_decimal_places(4.653725356))


'''
# Details
    Each number should be formatted that it is rounded to two decimal places. You don't need to check
    whether the input is a valid number because only valid numbers are used in the tests.
        Example:
        5.5589 is rounded 5.56
        3.3424 is rounded 3.34

# Exemplu 1
def two_decimal_places(n):
    return float("{0:.2f}".format(n))
'''
