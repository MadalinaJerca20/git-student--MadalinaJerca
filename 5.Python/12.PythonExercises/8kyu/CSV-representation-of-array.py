def toCsvText(array):
    return '\n'.join(','.join(str(c) for c in arr) for arr in array)


print(toCsvText([
    [0, 1, 2, 3, 45],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]), '0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34')

print(toCsvText([
    [-25, 21, 2, -33, 48],
    [30, 31, -32, 33, -34]
]), '-25,21,2,-33,48\n30,31,-32,33,-34')

print(toCsvText([
    [5, 55, 5, 5, 55],
    [6, 6, 66, 23, 24],
    [666, 31, 66, 33, 7]
]), '5,55,5,5,55\n6,6,66,23,24\n666,31,66,33,7')


'''
# Details
    Create a function that returns the CSV representation of a two-dimensional numeric array.
        Example:
        input:
        [[ 0, 1, 2, 3, 4 ],
            [ 10,11,12,13,14 ],
            [ 20,21,22,23,24 ],
            [ 30,31,32,33,34 ]]
        output:
            '0,1,2,3,4\n'
            +'10,11,12,13,14\n'
            +'20,21,22,23,24\n'
            +'30,31,32,33,34'
        Array's length > 2.

# Exemplu 1
def toCsvText(array):
    rs = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = str(array[i][j])
        rs.append(','.join(array[i]))
    return '\n'.join(rs)
'''
