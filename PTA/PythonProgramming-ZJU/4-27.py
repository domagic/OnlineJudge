import numpy as np

array = list(map(int, input().split()))
array = np.array(array).reshape(3, 3)
array = array.T
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        print('{:4d}'.format(array[i, j]), end='')
    print()
