import numpy as np

array = []
for i in range(2):
    elements = list(map(int, input().split()))[1:]
    array.append(elements)
a = np.array(array[0])
b = np.array(array[1])
common = np.intersect1d(a, b)
difference = []
for i in range(a.size):
    if a[i] not in common and a[i] not in difference:
        difference.append(a[i])
for i in range(b.size):
    if b[i] not in common and b[i] not in difference:
        difference.append(b[i])
difference = [str(e) for e in difference]
print(' '.join(difference))
