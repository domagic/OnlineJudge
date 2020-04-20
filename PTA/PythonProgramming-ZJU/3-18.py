num_lines = int(input())
lines = []
for i in range(num_lines):
    lines.append(input())
longest = max(map(len, lines))
for line in lines:
    if len(line) == longest:
        print("The longest is:", line)
        break
