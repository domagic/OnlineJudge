import numpy as np

s = input()
nums = ''
weights = []
dim = 0
for i in range(len(s)):
    character = s[i]
    if character == '[':
        dim += 1
    elif character == ']':
        if s[i-1].isdecimal() :
            weights.append(dim)
        dim -= 1
    elif character == ',':
        nums += character
        if s[i-1].isdecimal():
            weights.append(dim)
    else:
        nums += character
nums = list(map(int, nums.split(',')))
print(sum(np.multiply(nums, weights)))
