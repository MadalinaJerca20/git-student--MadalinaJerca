def string_to_array(s):
    return s.split() if s else['']


print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))
print(string_to_array("1 2 3"))
print(string_to_array(""), [""])


'''
# Details
    Write a function to split a string and convert it into an array of words. For example:
        "Robin Singh" ==> ["Robin", "Singh"]
        "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

# Exemplu 1
def string_to_array(string):
    return string.split(" ")

# Exemplu 2
def string_to_array(s):
    words = []
    if s == '':
        words.append(s)
    else:
        words = s.split()
    return words

# Exemplu 3
def string_to_array(string):
    return string.split() if string else [""]
'''
