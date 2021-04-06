def no_space(x):
    return x.replace(' ', '')


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))
print(no_space('8aaaaa dddd r     '))
print(no_space('jfBm  gk lf8hg  88lbe8 '))
print(no_space('8j aam'))


'''
# Details
    Simple, remove the spaces from the string, then return the resultant string.
        ('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
        ('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
        ('8aaaaa dddd r     '), '8aaaaaddddr')
        ('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
        ('8j aam'), '8jaam')

# Exemplu 1
def no_space(x):
    return "".join(x.split())

# Exemplu 2
def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char
'''
