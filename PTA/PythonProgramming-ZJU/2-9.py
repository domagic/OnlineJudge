lower, upper = list(map(int, input().split()))
if lower <= 0 or upper <= 0 or lower > upper or upper > 100:
    print("Invalid.")
else:
    print("fahr celsius")
    for fahrenheit in range(lower, upper + 1, 2):
        celsius = 5 * (fahrenheit - 32) / 9
        print("{0}{1:>6.1f}".format(fahrenheit, celsius))
