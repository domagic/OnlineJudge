import numpy as np

m, n = map(int, input().split())
array = []
for i in range(m):
    row = list(map(int, input().split()))
    array.append(row)
array = np.array(array)
local_max_value = False
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if array[i, j] > array[i - 1, j] and array[i, j] > array[i + 1, j] and \
                array[i, j] > array[i, j - 1] and array[i, j] > array[i, j + 1]:
            local_max_value = True
            print(array[i, j], i + 1, j + 1)
if not local_max_value:
    print('None {} {}'.format(m, n))
