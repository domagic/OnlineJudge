import numpy as np

student_num = int(input())
student_info = []
score_array = []
for line_index in range(student_num):
    student_info.append(input().split())
    score = student_info[-1][2:]
    score = list(map(int, score))
    score_array.append(score)
score_array = np.array(score_array)
total_score_array = np.sum(score_array, axis=1)
index_max_total_score = np.argmax(total_score_array)
print(student_info[int(index_max_total_score)][1], student_info[
    int(index_max_total_score)][0], total_score_array[index_max_total_score])
