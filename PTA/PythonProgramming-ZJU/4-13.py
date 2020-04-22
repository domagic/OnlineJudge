import math

error = float(input())
e_i = 1 / 1
e_j = 1 / 2
approximate_e = 1 + e_i
item = 2
while e_i - e_j >= error:
    item += 1
    approximate_e += e_j
    e_i, e_j = e_j, 1.0 / math.factorial(item)
print('{:.6f}'.format(approximate_e))
