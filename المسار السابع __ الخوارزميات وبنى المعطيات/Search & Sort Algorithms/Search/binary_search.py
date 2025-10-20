def binary_search_re(arr, f, l, s):
    if f <= l:
        mid = f + (l - f) // 2

        if arr[mid] == s:
            return mid

        elif arr[mid] > s:
            return binary_search_re(arr, f, mid - 1, s)

        else:
            return binary_search_re(arr, mid + 1, l, s)

    else:
        return -1

array = [1, 2, 5, 7 , 11, 23, 64, 99]

target = 11

result = binary_search_re(array, 0, len(array) - 1, target)

if result != -1:
    print(f'Find it in Index: {result}')
else:
    print('Not found')