def bubble_sort_opt(arr):
    count = sort = 0

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                sort += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    print(f'Count: {count}')
    print(f'Swapped: {sort}')
    print('-' * 20)
    for i in range(len(arr)):
        print(arr[i])



array = [6, 1, 5, 10, 3, 90, 2, 53]
bubble_sort_opt(array)
