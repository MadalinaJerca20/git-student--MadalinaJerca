def lowercase_count(strng):
    return sum(a.islower() for a in strng)


print(lowercase_count("abc"))
print(lowercase_count("abcABC123"))
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count(""))
print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"))


'''
# Details
    Your task is simply to count the total number of lowercase letters in a string.
        Examples
        lowercaseCount("abc"); ===> 3
        lowercaseCount("abcABC123"); ===> 3
        lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3
        lowercaseCount(""); ===> 0;
        lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0
        lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26

# Exemplu 1
import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))

# Exemplu 2
def lowercase_count(strng):
    return len([ch for ch in strng if ch.islower()])
'''
