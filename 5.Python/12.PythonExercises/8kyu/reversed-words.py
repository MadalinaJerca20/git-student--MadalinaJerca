def reverseWords(s):
    return ' '.join(reversed(s.split(" ")))


print(reverseWords("hello world!"))


'''
# Details
    Complete the solution so that it reverses all of the words within the string passed in.
        Example:
        reverseWords("The greatest victory is that which requires no battle")
        // should return "battle no requires which that is victory greatest The"

# Exemplu 1
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

# Exemplu 2
def reverseWords(str):
    k = str.split(' ')
    k.reverse()
    str = ' '.join(k)
    return str

# Exemplu 3
def reverseWords(str):
    str = str.split()
    str = reversed(str)
    return " ".join(str)
'''
