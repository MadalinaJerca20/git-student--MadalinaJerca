def capitalize_word(word):
    return word[0].upper() + word[1:]


print(capitalize_word('word'))
print(capitalize_word('i'))
print(capitalize_word('glasswear'))


'''
# Details
    Your coworker was supposed to write a simple helper function to capitalize a string (that contains a
    single word) before they went on vacation. This one ->
            def capitalize_word(word):
                return "".join(char.upper() for char in word)
    Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function
    they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).
    Don't worry about numbers, special characters, or non-string types being passed to the function. The
    string lengths will be from 1 character up to 10 characters,but will never be empty.

# Exemplu 1
def capitalize_word(word):
    first = word[0].upper()
    remaining = word[1:].lower()
    text = first + remaining
    return text

# Exemplu 2
def capitalize_word(word):
    return "".join(char.capitalize() for char in word.split())
'''
