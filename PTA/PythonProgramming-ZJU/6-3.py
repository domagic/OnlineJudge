neglectful_characters = {'(': 1, ')': 1, '[': 1, ']': 1, '{': 1, '}': 1}
s = input()
if s[0] == '(':
    s = s.lstrip('(').rstrip(')')
elif s[0] == '[':
    s = s.lstrip('[').rstrip(']')
num_s = ''
index = 0
while index < len(s):
    if s[index] == ',':
        num_s += ' '
    elif s[index] in ["'", '"']:
        index += 1
        while index < len(s) and s[index] not in ["'", '"']:
            index += 1
        index += 1
    elif s[index] not in neglectful_characters:
        num_s += s[index]
    index += 1
print(sum(map(int, num_s.split())))
