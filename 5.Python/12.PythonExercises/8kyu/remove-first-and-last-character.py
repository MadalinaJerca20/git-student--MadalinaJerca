def remove_char(s):
    return s[1:-1]


print(remove_char('eloquent'), 'loquen')
print(remove_char('country'), 'ountr')
print(remove_char('person'), 'erso')
print(remove_char('place'), 'lac')
print(remove_char('ok'), '')


'''
# Details
    It's pretty straightforward. Your goal is to create a function that removes the first and last
    characters of a string. You're given one parameter, the original string. You don't have to worry with
    strings with less than two characters.

# Exemplu 1
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]
'''
