def sqrt_binary_search(x):
    if x == 0 or x == 1:
        return x

    start = 1
    end = x
    answer = 1
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid

        elif mid * mid > x:
            end = mid - 1

        else:
            start = mid + 1
            answer = mid

    return answer

x = 88
print(sqrt_binary_search(x))