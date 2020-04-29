array = eval(input())
if len(array) == 0:
    print(array)
else:
    non_duplicate_l = []
    for e in array:
        if e not in non_duplicate_l:
            non_duplicate_l.append(e)
    print(' '.join(map(str, non_duplicate_l)))
