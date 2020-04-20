import math

x = float(input())
print("f({0:.1f}) = {1:.1f}".format(x, 1.0 / x if math.fabs(
    x - 0.0) > 0.1 else 0.0))
