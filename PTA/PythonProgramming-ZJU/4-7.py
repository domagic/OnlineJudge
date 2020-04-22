students_num = int(input())
if students_num == 0:
    print('average = 0.0')
    print('count = 0')
else:
    students_score = list(map(int, input().split()))
    pass_score = [score for score in students_score if score >= 60]
    print('average = {:.1f}'.format(sum(students_score) / students_num))
    print('count = {}'.format(len(pass_score)))
