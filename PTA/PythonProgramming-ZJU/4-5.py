def factorial(x, result):
    for j in range(1, x + 1):
        if len(result) == 0:
            result.append(j)
        else:
            result.append(result[-1] * j)


n = int(input())
factorial_numbers = []
factorial(x=n, result=factorial_numbers)
approximate_e = 1
for i in range(n):
    approximate_e += 1 / factorial_numbers[i]
print('{:.8f}'.format(approximate_e))
