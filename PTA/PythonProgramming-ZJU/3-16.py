s = list(input().strip())
c = input().strip()
non_duplicate_s = []
for element in s:
    if element.lower() != c.lower():
        non_duplicate_s.append(element)
print("result:", ''.join(non_duplicate_s))
