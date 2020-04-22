def is_daffodil(x):
    y = list(str(x))
    y = list(map(int, y))
    if sum([element ** len(y) for element in y]) == int(x):
        return True
    else:
        return False


num_digits = int(input())
numbers = []
for i in range(10 ** (num_digits - 1), 10 ** num_digits):
    if is_daffodil(i):
        print(i)
