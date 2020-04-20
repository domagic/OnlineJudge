sentence = input()
vowel_letters = ['A', 'E', 'I', 'O', 'U']
count_consonant = 0
for element in sentence:
    if element.isalpha() and element.isupper() and element not in vowel_letters:
        count_consonant += 1
print(count_consonant)
