nums = list(map(int, input().split()))
num_count_pair = {}
for key in nums:
    if key in num_count_pair:
        num_count_pair[key] += 1
    else:
        num_count_pair[key] = 1
max_count = 0
key_with_max_count = 0
for value, count in num_count_pair.items():
    if count >= max_count:
        key_with_max_count = value
        max_count = count
print(key_with_max_count, max_count)
