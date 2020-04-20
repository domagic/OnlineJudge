len_nums = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
for i, element in enumerate(nums):
    if element == max_num:
        print(element, i)
        break
