students_num = int(input())
students_info = []
for i in range(students_num):
    student = input().split()
    students_info.append(student)
is_pair = [False for i in range(students_num)]
for i in range(students_num // 2):
    for j in range(students_num - 1, students_num // 2 - 1, -1):
        if is_pair[j]:
            continue
        if int(students_info[i][0]) ^ int(students_info[j][0]):
            print(students_info[i][1], students_info[j][1])
            is_pair[j] = True
            break
