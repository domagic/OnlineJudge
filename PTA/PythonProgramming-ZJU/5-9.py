import numpy as np

n = int(input())
array = []
for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)
array = np.array(array)

count = 0
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i, j] == max(array[i]) and array[i, j] == min(array[:, j]):
            count += 1
print(count)
