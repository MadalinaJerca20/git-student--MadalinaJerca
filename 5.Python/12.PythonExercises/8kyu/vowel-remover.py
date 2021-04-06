def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')


print(shortcut('hello'))


'''
# Details
    Create a function called shortcut to remove all the lowercase vowels in a given string.
        Examples
        shortcut("codewars") # --> cdwrs
        shortcut("goodbye")  # --> gdby
        Don't worry about uppercase vowels.

# Exemplu 1
def shortcut(s):
    return s.translate(None, 'aeiou')

# Exemplu 2
def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s
'''
