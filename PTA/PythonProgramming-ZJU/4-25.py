def my_factorial():
    result = 1
    i = 1
    while True:
        result *= i
        yield result
        i += 1


n = int(input())
factorial_sum = 0
item = my_factorial()
for i in range(1, n + 1):
    value = next(item)
    if i % 2 != 0:
        factorial_sum += value
print('n={},s={}'.format(n, factorial_sum))
