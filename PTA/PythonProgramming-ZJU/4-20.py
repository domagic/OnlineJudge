import numpy as np

t = int(input())
for i in range(t):
    n = int(input())
    array = []
    for j in range(n):
        row = list(map(int, input().split()))
        array.append(row)
    array = np.array(array)
    if (array - np.triu(array)).sum() != 0:
        print('NO')
    else:
        print('YES')
