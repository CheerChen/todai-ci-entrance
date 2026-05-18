# coding=utf-8

def read_file_lines(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line)
    return lines


lines = read_file_lines('data/1000.txt')

import re

recs = []
for line in lines:
    # l = line.replace('\n', '')
    l = re.findall('\d+', line)
    recs.append(map(int, l))


# print recs

# stupid version
# def point_in_rec(p, rec):
#     if p[0] > rec[0] and p[0] <= rec[0] + rec[2]:
#         if p[1] > rec[1] and p[1] <= rec[1] + rec[3]:
#             return True
#     return False
# area_sum = 0
# for x in xrange(1, 1000):
#     for y in xrange(1, 1000):
#         for rec in recs:
#             if point_in_rec([x, y], rec):
#                 area_sum += 1
#                 break

# print area_sum
# 初始化一个矩阵


def get_max_p(recs):
    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 1000
    for rec in recs:
        if rec[0] + rec[2] > max_x:
            max_x = rec[0] + rec[2]
        if rec[1] + rec[3] > max_y:
            max_y = rec[1] + rec[3]
        if rec[0] < min_x:
            min_x = rec[0]
        if rec[1] < min_y:
            min_y = rec[1]
    return max_x, max_y, min_x, min_y


# 固定生成1000*1000
# 21.7514208013 用了21s之多
def get_area_sum(recs):
    table = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

    for rec in recs:
        for x in xrange(rec[0], rec[0] + rec[2]):
            for y in xrange(rec[1], rec[1] + rec[3]):
                table[y][x] += 1

    # print table
    area_sum = 0
    max_thickness = 0
    for row in table:
        for p in row:
            if p > 0:
                area_sum += 1
            if p > max_thickness:
                max_thickness = p

    return area_sum, max_thickness


# 动态生成矩阵
# 只用了0.10078154894
def new_get_area_sum(recs):
    max_x, max_y, min_x, min_y = get_max_p(recs)
    # print max_x, max_y, min_x, min_y
    table = [[0 for _ in xrange(max_x - min_x)] for _ in xrange(max_y - min_y)]

    for rec in recs:
        for x in xrange(rec[0] - min_x, rec[0] - min_x + rec[2]):
            for y in xrange(rec[1] - min_y, rec[1] - min_y + rec[3]):
                table[y][x] += 1

    # print table
    area_sum = 0
    max_thickness = 0
    for row in table:
        for p in row:
            if p > 0:
                area_sum += 1
            if p > max_thickness:
                max_thickness = p

    return area_sum, max_thickness


print new_get_area_sum(recs)


# print is_connected([1,1,2,1],[2,2,1,1])
def is_connected(rec1, rec2):
    x1, y1, l1, h1 = rec1[0], rec1[1], rec1[2], rec1[3]
    x2, y2, l2, h2 = rec2[0], rec2[1], rec2[2], rec2[3]
    f1 = x2 > x1 - l2
    f2 = x2 < x1 + l1
    f3 = y2 > y1 - h2
    f4 = y2 < y1 + h1

    if f1 and f2:
        f3 = y2 >= y1 - h2
        f4 = y2 <= y1 + h1

    if f3 and f4:
        f1 = x2 >= x1 - l2
        f2 = x2 <= x1 + l1

    return f1 and f2 and f3 and f4

# 将所有长方形根据is_connected分组

l = len(recs)
group_index = range(l)

for i in xrange(l):
    for j in xrange(i + 1, l):
        if is_connected(recs[i], recs[j]):
            group_index[j] = group_index[i]
group_dict = {}

for k, v in enumerate(group_index):
    try:
        group_dict[v].append(recs[k])
    except KeyError:
        group_dict[v] = [recs[k]]

print len(group_dict)


max_ele = 0
max_area = 0
for _, g in group_dict.items():
    if len(g) > max_ele:
        max_ele = len(g)
    area, _ = new_get_area_sum(g)
    if area > max_area:
        max_area = area



print max_ele
print max_area

# print t - s
