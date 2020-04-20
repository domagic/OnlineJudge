s = input()
non_duplicate_letters = {}
letters = []
for element in s:
    if element.isalpha() and element.isupper() and element not in \
            non_duplicate_letters:
        non_duplicate_letters[element] = 1
        letters.append(element)

if len(letters) == 0:
    print("Not Found")
else:
    print(''.join(letters))