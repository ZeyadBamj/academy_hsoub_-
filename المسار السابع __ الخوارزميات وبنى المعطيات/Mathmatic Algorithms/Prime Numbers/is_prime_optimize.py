def is_prime_opt(n):
    if n <= 1:
        print('False')
        return False
    if n <= 3:
        print('True')
        return True
    if n % 2 == 0 or n % 3 == 0:
        print('False')
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % i + 2 == 0:
            print('False')
            return False
        i += 6
    print('True')
    return True


is_prime_opt(37)