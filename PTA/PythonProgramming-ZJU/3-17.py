s = input()
letters = []
non_duplicate_letters = {}
for letter in s:
    if letter.isalpha() and (letter.lower() not in non_duplicate_letters) and \
            (letter.upper() not in non_duplicate_letters):
        letters.append(letter)
        non_duplicate_letters[letter] = 1
    if len(letters) >= 10:
        break
if len(letters) < 10:
    print("not found")
else:
    print(''.join(letters[:10]))
