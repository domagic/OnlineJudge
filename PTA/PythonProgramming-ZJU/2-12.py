a, b, c = list(map(int, input().split()))
if a + b <= c or a + c <= b or b + c <= a:
    print("These sides do not correspond to a valid triangle")
else:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    perimeter = s * 2
    print("area = {0:.2f}; perimeter = {1:.2f}".format(area, perimeter))
