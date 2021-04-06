def repeat_it(string, n):
    return string * n if isinstance(string, str) else 'Not a string'


print(repeat_it("*", 3)
print(repeat_it("Hello", 5))


'''
# Details
    Create a function that takes a string and an integer (n).
    The function should return a string that repeats the input string n number of times.
    If anything other than a string is passed in you should return "Not a string"
        Example
        "Hi", 2 --> "HiHi"
        1234, 5 --> "Not a string"

# Exemplu 1
def repeat_it(string,n):
    if type(string) is not str:
        return 'Not a string'
    return string * n
'''
