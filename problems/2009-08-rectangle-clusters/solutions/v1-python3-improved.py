# coding=utf-8

def read_file_lines(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line)
    return lines

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
    table = [[0 for _ in range(1000)] for _ in range(1000)]

    for rec in recs:
        for x in range(rec[0], rec[0] + rec[2]):
            for y in range(rec[1], rec[1] + rec[3]):
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
    table = [[0 for _ in range(max_x - min_x)] for _ in range(max_y - min_y)]

    for rec in recs:
        for x in range(rec[0] - min_x, rec[0] - min_x + rec[2]):
            for y in range(rec[1] - min_y, rec[1] - min_y + rec[3]):
                table[y][x] += 1

    # print table
    area_sum = 0
    area_covered = 0
    max_thickness = 0
    for row in table:
        for p in row:
            if p > 0:
                area_covered += 1
            if p > 0:
                area_sum += p
            if p > max_thickness:
                max_thickness = p

    return area_sum,area_covered,max_thickness

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

def new_get_connected_recs_num(recs):
    l = len(recs)
    group_index = list(range(l))

    for i in range(l):
        for j in range(i + 1, l):
            if is_connected(recs[i], recs[j]):
                to_update = group_index[j]
                group_index[j] = group_index[i]
                for idx in range(len(group_index)):
                    if group_index[idx] == to_update:
                        group_index[idx] = group_index[i] 
    group_dict = {}

    for k, v in enumerate(group_index):
        try:
            group_dict[v].append(recs[k])
        except KeyError:
            group_dict[v] = [recs[k]]
            
    max_ele = 0
    max_area = 0
    for _, g in group_dict.items():
        if len(g) > max_ele:
            max_ele = len(g)
        _, area_covered, _ = new_get_area_sum(g)
        if area_covered > max_area:
            max_area = area_covered

    return len(group_dict), max_ele, max_area

lines = read_file_lines('data/10.txt')

import re

recs = []
for line in lines:
    # l = line.replace('\n', '')
    l = re.findall(r'\d+', line)
    recs.append(list(map(int, l)))
    
_,_,max_thickness = new_get_area_sum(recs)
cluster_num, max_ele, max_area = new_get_connected_recs_num(recs)
    
print('(1-1) 厚さの最大値を求めよ．')
print(max_thickness)
# (1-2) クラスタの数を求めよ．
print('(1-2) クラスタの数を求めよ．')
print(cluster_num)
# (1-3) クラスタの要素数の最大値を求めよ．
print('(1-3) クラスタの要素数の最大値を求めよ．')
print(max_ele)
# (1-4) クラスタの面積の最大値を求めよ．
print('(1-4) クラスタの面積の最大値を求めよ．')
print(max_area)




lines = read_file_lines('data/1000.txt')

import re

recs = []
for line in lines:
    # l = line.replace('\n', '')
    l = re.findall(r'\d+', line)
    recs.append(list(map(int, l)))

# print(new_get_area_sum(recs))

area_sum,area_covered, max_thickness = new_get_area_sum(recs)
cluster_num, max_ele, max_area = new_get_connected_recs_num(recs)

# 1000.txt で与えられた1000 個の長方形のそれぞれの面積の総和を求めよ．
print('(2-1) 1000.txt で与えられた1000 個の長方形のそれぞれの面積の総和を求めよ．')
print(area_sum)

# (3-1) 厚さの最大値を求めよ．
print('(3-1) 厚さの最大値を求めよ．')
print(max_thickness)
# (3-2) クラスタの数を求めよ．
print('(3-2) クラスタの数を求めよ．')
print(cluster_num)
# (3-3) クラスタの要素数の最大値を求めよ．
print('(3-3) クラスタの要素数の最大値を求めよ．')
print(max_ele)
# (3-4) クラスタの面積の最大値を求めよ．
print('(3-4) クラスタの面積の最大値を求めよ．')

print(max_area)

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
