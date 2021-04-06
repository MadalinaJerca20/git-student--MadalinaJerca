def two_sort(array):
    first = sorted(array)[0]
    result = ""
    for i in first:
        result += i + "***"
    return result.strip("***")


print(two_sort(["bitcoin", "take", "over", "the",
                "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["turns", "out", "random", "test", "cases",
                "are", "easier", "than", "writing", "out", "basic", "ones"]))
print(two_sort(["lets", "talk", "about",
                "javascript", "the", "best", "language"]))
print(two_sort(["Lets", "all", "go", "on",
                "holiday", "somewhere", "very", "cold"]))


'''
# Details
    You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on
    the ASCII values of the chars) and then return the first value.
    The returned value must be a string, and have "***" between each of its letters.
    You should not remove or add elements from/to the array.

# Exemplu 1
def two_sort(arr):
    return '***'.join(sorted(arr)[0])

# Exemplu 2
def two_sort(array):
    return '***'.join(min(array))
'''
