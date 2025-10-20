def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print('Selection Sort:')
    print('-' * 20)
    for i in range(len(arr)):
        print(arr[i])

array = [2, 5, 12, 65, 9, 3, 1, 23, 80, 83, 6, 7, 8]
words = ['hello', 'welcome', 'hi', 'how', 'what', 'who']
selection_sort(words)