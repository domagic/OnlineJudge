import numpy as np

elements = list(map(int, input().split()))
array = np.array(elements).reshape((3, 3))
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        print('{:4d}'.format(array[i, j]), end='')
    print('{:4d}'.format(array[i].max()), end='')
    print('{:4d}'.format(array[i].sum()))
