def insertion_sort_iter(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    for i in range(len(arr)):
        print(arr[i])

array = [20, 4, 12, 3, 4, 9, 13, 12, 34]
insertion_sort_iter(array)