def is_prime(n):
    if n <= 1:
        print('False')
        return False

    for i in range(2, n):
        if n % i == 0:
            print('False')
            return False

    print('True')
    return True


is_prime(3)