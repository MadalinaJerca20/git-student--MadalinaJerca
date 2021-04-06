def reverse(st):
    return " ".join(st.split()[::-1]).rstrip()


print(reverse('Hello World'), 'World Hello')
print(reverse('Hi There.'), 'There. Hi')


'''
# Details
    You need to write a function that reverses the words in a given string. A word can also fit an empty
    string. If this is not clear enough, here are some examples:
    As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
        reverse('Hello World') == 'World Hello'
        reverse('Hi There.') == 'There. Hi'

# Exemplu 1
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

# Exemplu 2
def reverse(st):
    return " ".join(reversed(st.split())).strip()
'''
