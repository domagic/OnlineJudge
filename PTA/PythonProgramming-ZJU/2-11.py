a, n = list(input().split())
sequence = [a * i for i in range(2, int(n) + 1, 2)]
sequence = list(map(int, sequence))
print(sum(sequence))
