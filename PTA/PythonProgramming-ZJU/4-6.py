def my_fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


N = int(input())
if N < 1:
    print('Invalid.')
else:
    generator = my_fibonacci()
    for i in range(1, N + 1):
        num = next(generator)
        print('{:11}'.format(num), end='')
        if i % 5 == 0:
            print()

