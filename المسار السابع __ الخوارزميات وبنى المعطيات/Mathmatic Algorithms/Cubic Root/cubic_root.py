def diff(n, mid):
    if n > mid * mid * mid:
        return n - (mid * mid * mid)
    else:
        return (mid * mid * mid) - n

def cubic_root(n):
    if n == 0 or n == 1:
        return n

    start = 0
    end = n
    e = 0.0000001
    while True:
        mid = (start + end) / 2
        error = diff(n, mid)

        if error <= e:
            return mid

        elif mid ** 3 > n:
            end = mid

        else:
            start = mid


x = 125
print(round(cubic_root(x), 9))