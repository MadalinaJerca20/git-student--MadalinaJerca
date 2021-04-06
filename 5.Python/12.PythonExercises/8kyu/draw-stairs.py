def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


stairs = '''I\n I\n  I'''
print(draw_stairs(3), stairs)


'''
# Details
    Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in
    the top left.
    For example n = 3 result in:
    "I\n I\n  I"
    or printed:
        I
         I
          I

# Exemplu 1
def draw_stairs(n):
    count = 1
    res = ""
    while count < n:
        res += "I\n" + " " * count
        count += 1
    res += "I"
    return res
'''
