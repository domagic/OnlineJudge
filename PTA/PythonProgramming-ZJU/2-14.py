a, b = list(map(int, input().split()))
sequence = list(range(a, b + 1))
for index, element in enumerate(sequence):
    if index != 0 and index % 5 == 0:
        print()
    print("{0:>5}".format(element), end="")
print()
print("Sum =", sum(sequence))
