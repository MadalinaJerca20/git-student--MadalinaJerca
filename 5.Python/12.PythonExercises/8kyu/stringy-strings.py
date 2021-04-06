def stringy(size):
    return "".join(str((i + 1) % 2) for i in range(size))


print("Should start with '1'")
print(stringy(10)[0], '1', "Whoops your string doesn't start with a '1'")


print("Should have the correct length")
for i in range(1, 5):
    print(len(stringy(i)), i, "Make sure your string is the right length")


print("Should work for some simple tests")
print(stringy(3), '101', 'oops try again')
print(stringy(5), '10101', 'oops try again')
print(stringy(12), '101010101010', 'oops try again')


'''
# Details
    Write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
    The string should start with a 1.
        a string with size 6 should return :'101010'.
        with size 4 should return : '1010'.
        with size 12 should return : '101010101010'.
    The size will always be positive and will only use whole numbers.

# Exemplu 1
def stringy(size):
    s = ""
    for x in range (0, size):
        s+= str("1") if x%2 == 0 else str("0")
    return s

# Exemplu 2
def stringy(size):
    str = ""
    while len(str) < size:
            str+="1"
            if len(str) < size:
                str+="0"
    return str

# Exemplu 3
def stringy(size):
    arr=[]
    for i in range(size):
        if i%2==0:
            arr.append('1')
        else:
            arr.append('0')
    return ''.join(arr)
'''
