import math


def is_prime(x):
    for number in range(2, int(math.sqrt(x)) + 1):
        if x % number == 0:
            return False
    return True


n = int(input())
for i in range(2, n + 1):
    if is_prime(i) and is_prime(n - i):
        print('{0} = {1} + {2}'.format(n, i, n - i))
        break
