n = int(input())
letter = 'A'
for i in range(n, 0, -1):
    for j in range(i):
        print(letter, end=' ')
        letter = chr(ord(letter) + 1)
    print()
