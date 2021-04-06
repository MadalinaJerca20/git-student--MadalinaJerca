def print_array(arr):
    return ",".join([str(elem) for elem in arr])


data = [2, 4, 5, 2]
print(print_array(data), "2,4,5,2")


data = [2.0, 4.2, 5.1, 2.2]
print(print_array(data), "2.0,4.2,5.1,2.2")

data = ["2", "4", "5", "2"]
print(print_array(data), "2,4,5,2")

data = [True, False, False]
print(print_array(data), "True,False,False")

array1 = ["hello", "this", "is", "an", "array!"]
array2 = ["a", "b", "c", "d", "e!"]
data = array1+array2
print(print_array(data), "hello,this,is,an,array!,a,b,c,d,e!")


'''
# Details
    Input: Array of elements
        ["h","o","l","a"]
    Output: String with comma delimited elements of the array in th same order.
        "h,o,l,a"

# Exemplu 1
def print_array(arr):
    result = []
    for ar in arr:
        if ar is list:
            result.append(print_array(ar))
        else:
            result.append(str(ar))
    return ','.join(result)
'''
