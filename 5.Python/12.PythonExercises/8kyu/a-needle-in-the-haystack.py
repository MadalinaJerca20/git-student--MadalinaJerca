def find_the_other_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle':
            return 'found the needle at position %d' % i


print(find_the_other_needle(
    ['3', '123', None, 'needle', 'world', 'hay', 2, '3', True, False]))
print(find_the_other_needle(
    ['28344', 'a dog', 'a cat', 'a piece of hay', 'needle']))


'''
# Details
    Can you find the needle in the haystack?
    Write a function findNeedle() that takes an array full of junk but containing one "needle"
    After your function finds the needle it should return a message (as a string) that says:
    "found the needle at position " plus the index it found the needle, so:
        find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
        should return "found the needle at position 5"


# Exemplu 1
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

# Exemplu 2
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
'''
