string = input()
digits = []
for element in string:
    if element.isdigit():
        digits.append(element)
num = int("".join(digits))
print(num)
