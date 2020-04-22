import math

n = int(input())
for i in range(n + 1):
    print("pow(3,{0}) = {1}".format(i, int(math.pow(3, i))))
