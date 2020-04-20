s = list(input())
balance_number = ord('A') + ord('Z')
for index, element in enumerate(s):
    if element.isalpha() and element.isupper():
        s[index] = chr(balance_number - ord(element))
print(''.join(s))
