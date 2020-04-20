weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
checksum_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6',
                    7: '5', 8: '4', 9: '3', 10: '2'}
all_valid_identify_number = True
n = int(input())
for i in range(n):
    identify_number = input()
    if all(identify_number[j].isdecimal() for j in
           range(0, len(identify_number) - 1)):
        checksum = 0
        check_digits = list(map(int, identify_number[:-1]))
        for j in range(len(check_digits)):
            checksum += check_digits[j] * weights[j]
        z = checksum % 11
        if checksum_mapping[z] == identify_number[-1]:
            continue
    print(identify_number)
    if all_valid_identify_number is True:
        all_valid_identify_number = False
if all_valid_identify_number:
    print("All passed")
