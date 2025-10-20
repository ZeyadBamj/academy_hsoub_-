def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for i in range(len(arr)):
        print(arr[i])


array = [2, 5, 12, 65, 9, 3, 1]
letters = ['c', 'a', 'e', 'g', 'f', 'k']
words = ['hello', 'welcome', 'hi', 'how', 'what', 'who']

bubble_sort(words)