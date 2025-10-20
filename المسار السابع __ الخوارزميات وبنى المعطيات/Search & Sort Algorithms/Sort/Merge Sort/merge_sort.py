def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while len(left) > i:
            arr[k] = left[i]
            i += 1
            k += 1

        while len(right) > j:
            arr[k] = right[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print('\n')


arr = [12, 11, 13, 5, 6, 7, 20, 53, 12, 1, 0, 58, 23, 12, 8, 69, 231, 38, 85, 81]
print("Given array is")
print_list(arr)
merge_sort(arr)
print("Sorted array is: ")
print_list(arr)
