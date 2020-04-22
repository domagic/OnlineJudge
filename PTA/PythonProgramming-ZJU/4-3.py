days = int(input())
n = 1
for i in range(days - 1, 0, -1):
    n = (n + 1) * 2
print(n)
