line_num = int(input())
points = {}
edge_count = 0
edge_weight_sum = 0
for i in range(line_num):
    row = eval(input())
    keys = list(row.keys())
    points[keys[0]] = 1
    edge_weight = row[keys[0]].values()
    edge_count += len(edge_weight)
    edge_weight_sum += sum(edge_weight)
print(len(points), edge_count, edge_weight_sum)
