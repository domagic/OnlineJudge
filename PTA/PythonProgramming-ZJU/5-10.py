array = list(map(int, input().split(',')))
target = int(input())
number_position_pair = {}
find_target = False
for i in range(len(array)):
    element = array[i]
    if target - element not in number_position_pair:
        number_position_pair[element] = i
    else:
        find_target = True
        if number_position_pair[target - element] > i:
            print(i, number_position_pair[target - element])
        else:
            print(number_position_pair[target - element], i)
        break
if not find_target:
    print('no answer')
