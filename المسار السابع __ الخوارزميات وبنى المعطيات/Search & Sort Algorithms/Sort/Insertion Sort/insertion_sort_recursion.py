def insertion_sort_recu(arr, n):
    if n <= 1:
        return

    insertion_sort_recu(arr, n - 1)

    last = arr[n - 1]

    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

def print_array(arr, n):
    for i in range(n):
        print(arr[i])


array = [20, 4, 12, 3, 4, 9, 13, 12, 34]
insertion_sort_recu(array, len(array))
print_array(array, len(array))