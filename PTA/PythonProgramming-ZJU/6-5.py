s = input()
weights = []
dim = 0
for i in range(len(s)):
    character = s[i]
    if character == '[':
        dim += 1
    elif character == ']':
        if s[i - 1].isdecimal():
            weights.append(dim)
        dim -= 1
    elif character == ',':
        if s[i - 1].isdecimal():
            weights.append(dim)
print(sum(weights))
