import numpy as np

m, _ = map(int, input().split())
array = []
for i in range(m):
    row = list(map(int, input().split()))
    array.append(row)
array = np.array(array)
for i in range(array.shape[0]):
    print(array[i, :].sum())
