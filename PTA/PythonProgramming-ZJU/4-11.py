import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


line_num = int(input())
for line_index in range(line_num):
    num = int(input())
    if is_prime(num):
        print('Yes')
    else:
        print('No')
