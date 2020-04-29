employee_num = int(input())
employee_year = list(map(int, input().split()))
year_count_pair = {}
for year in employee_year:
    if year not in year_count_pair:
        year_count_pair[year] = 1
    else:
        year_count_pair[year] += 1
year_count_pair = sorted(year_count_pair.items(),
                         key=lambda item: item[0])
for year, count in year_count_pair:
    print('{}:{}'.format(year, count))
