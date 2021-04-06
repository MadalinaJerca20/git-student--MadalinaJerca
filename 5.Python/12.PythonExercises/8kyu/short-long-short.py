def solution(a, b):
    return a+b+a if len(a) < len(b) else b+a+b


BASIC_TESTS = (
    (('45', '1'), '1451'),
    (('13', '200'), '1320013'),
    (('Soon', 'Me'), 'MeSoonMe'),
    (('U', 'False'), 'UFalseU')
)

for pair, result in BASIC_TESTS:
    print("'{}', '{}'".format(*pair))
    print(solution(*pair), result)


'''
# Details
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on
    the outside and the longer string on the inside. The strings will not be the same length, but they
    may be empty ( length 0 ).
        For example:
        solution("1", "22") # returns "1221"
        solution("22", "1") # returns "1221"

# Exemplu 1
def solution(a, b):
    if len(a)>len(b):
        return(b+a+b)
    else:
        return(a+b+a)

# Exemplu 2
def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short
'''
