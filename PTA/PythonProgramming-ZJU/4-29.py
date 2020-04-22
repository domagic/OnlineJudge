import math


def get_divisor(x, divisors):
    divisors[1] = 1
    for num in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % num == 0:
            divisors[num] = 1
            divisors[x // num] = 1


m, n = map(int, input().split())
has_perfect_number = False
for i in range(m, n + 1):
    result = {}
    get_divisor(i, result)
    result = list(result.keys())
    result.sort()
    if sum(result) == i:
        has_perfect_number = True
        print('{} = {}'.format(i, ' + '.join(list(map(str, result)))))
if not has_perfect_number:
    print('None')
