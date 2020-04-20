s1 = input()
s2 = input()
if s1 == s2:
    result = 'no'
else:
    s1_letters = {}
    s2_letters = {}
    for letter in s1:
        if letter not in s1_letters:
            s1_letters[letter] = 1
        else:
            s1_letters[letter] += 1
    for letter in s2:
        if letter not in s2_letters:
            s2_letters[letter] = 1
        else:
            s2_letters[letter] += 1
    result = 'yes' if s1_letters == s2_letters else 'no'
print(result)
