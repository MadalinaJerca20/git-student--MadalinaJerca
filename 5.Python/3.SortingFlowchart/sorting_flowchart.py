def sort_list(_list):
    N = len(_list)
    for number in _list:
        while number in range(1, N):
            if _list[number] < _list[number - 1]:
                temp = _list[number - 1]
                _list[number - 1] = _list[number]
                _list[number] = temp
            number += 1
    print(_list)


if __name__ == "__main__":
    numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    print(numbers, '\n')
    sort_list(numbers)
    