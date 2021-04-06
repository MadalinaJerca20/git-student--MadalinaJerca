def solution(string):
    return string[::-1]


print(solution('world'))
print(solution('hello'))
print(solution(''))
print(solution('h'))


'''
# Details
    Complete the solution so that it reverses the string passed into it.
        ('world'), 'dlrow')
        ('hello'), 'olleh')
        (''), '')
        ('h'), 'h')

# Exemplu 1
def solution(string):
    newstring = ""
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter -1
    return newstring
'''
