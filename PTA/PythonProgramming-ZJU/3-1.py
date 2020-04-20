heights = list(map(int, input().split()))
average_height = sum(heights) / len(heights)
greater_than_average_height = [height for height in heights if
                               height > average_height]
for element in greater_than_average_height:
    print(element, end=' ')
