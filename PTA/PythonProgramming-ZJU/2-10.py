m, n = list(map(int, input().split()))
odd_items = [i ** 2 for i in range(m, n + 1)]
even_items = [1 / i for i in range(m, n + 1)]
print("sum = {0:.6f}".format(sum(odd_items) + sum(even_items)))
