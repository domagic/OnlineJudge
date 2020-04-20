n = int(input())
sequence = [1.0 / i for i in range(1, n * 2, 2)]
print("sum = {0:.6f}".format(sum(sequence)))
