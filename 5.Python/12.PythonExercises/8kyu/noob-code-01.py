def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))


print(super_size(69))
print(super_size(513))
print(super_size(414))
print(super_size(700000000001))
print(super_size(666666))
print(super_size(2))
print(super_size(0))


'''
# Details
    Write a function that rearranges an integer into its largest possible value.
        super_size(123456) # 654321
        super_size(105)    # 510
        super_size(12)     # 21
    If the argument passed through is single digit or is already the maximum possible integer, your
    function should simply return it.

# Exemplu 1
def super_size(n):
    list_ = sorted(list(str(n)))
    list_.reverse()
    return int(''.join(tuple(list_)))

# Exemplu 2
def super_size(n):
    x = sorted(list(str(n)), reverse=True)
    return int(''.join(x))
'''
