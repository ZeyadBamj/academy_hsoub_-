def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3, 5, 1, 6, 12, 65 ,7]
target = 6

if target != -1:
    print(f'Find it in Index: {linear_search(arr, target)}')
else:
    print('Not Found!')