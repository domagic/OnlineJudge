n = int(input())
a, b = 0, 1
while True:
    if b > n:
        print(b)
        break
    else:
        b, a = a + b, b
