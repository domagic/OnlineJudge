string = input()
pattern = input().split()
results = []
for i, element in enumerate(string):
    if element in pattern:
        results.append((i, element))

while len(results):
    result = results.pop(-1)
    print(result[0], result[1])
