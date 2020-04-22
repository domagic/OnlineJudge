import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


m, n = list(map(int, input().split()))
prime_numbers = []

if m < 1 or n > 500 or m > n:
    pass
else:
    if m <= 2:
        m = 2
    for number in range(m, n + 1):
        if is_prime(x=number):
            prime_numbers.append(number)
    print(len(prime_numbers), sum(prime_numbers))
