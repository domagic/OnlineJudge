n = int(input())
circle = list(range(1, n + 1))
count_off = 0
index = -1
while len(circle) != 1:
    count_off += 1
    index = (index + 1) % len(circle)
    if count_off % 3 == 0:
        circle.pop(index)
        count_off = 0
        index = (len(circle) + index - 1) % len(circle)
print(circle[0])
