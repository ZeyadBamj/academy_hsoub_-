def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)



array = [12, 11, 13, 5, 6, 7, 20, 53, 12, 1, 0, 58, 23, 12, 8, 69, 231, 38, 85, 81]
n = len(array)
quick_sort(array, 0, n - 1)

for i in range(n):
    print(array[i])