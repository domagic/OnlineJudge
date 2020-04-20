s = list(input())
s.pop(-1)
for index, element in enumerate(s):
    if not element.isalpha():
        continue
    elif element.isupper():
        s[index] = element.lower()
    elif element.islower():
        s[index] = element.upper()
print(''.join(s))
