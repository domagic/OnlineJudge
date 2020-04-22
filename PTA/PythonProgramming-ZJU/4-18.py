import numpy as np

n = int(input())
array = []
for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)
array = np.array(array)
lr_array = np.fliplr(array)
result_sum = array.sum() - (
        lr_array.diagonal().sum() + array[-1, :].sum() + array[:,
                                                         -1].sum() - array[
            -1, 0] - array[0, -1] - array[-1, -1])
print(result_sum)
