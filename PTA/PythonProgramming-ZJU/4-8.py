n = int(input())
numerator, denominator = 2, 1
partial_sum = numerator / denominator
for i in range(2, n + 1):
    numerator, denominator = numerator + denominator, numerator
    partial_sum += numerator / denominator
print('{:.2f}'.format(partial_sum))
