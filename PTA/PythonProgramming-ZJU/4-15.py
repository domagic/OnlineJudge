a, b, c = map(int, input().split())
if a + b > c and a + c > b:
    answer = 'yes'
else:
    answer = 'no'
print(answer)
