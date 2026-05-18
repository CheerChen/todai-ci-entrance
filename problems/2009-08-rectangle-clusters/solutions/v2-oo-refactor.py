# coding=utf-8
import re


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        """返回矩形自身面积 w×h"""
        return self.w * self.h
    
    def is_connected(self, other):
        """判断与另一个矩形是否连通（重叠或共边，仅共角点不算）"""
        x1, y1, l1, h1 = self.x, self.y, self.w, self.h
        x2, y2, l2, h2 = other.x, other.y, other.w, other.h
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


class Cluster:
    def __init__(self, rectangles):
        self.rectangles = rectangles
    def get_max_rectangle(self):
        max_x = 0
        max_y = 0
        min_x = 1000
        min_y = 1000
        for rec in self.rectangles:
            if rec.x + rec.w > max_x:
                max_x = rec.x + rec.w
            if rec.y + rec.h > max_y:
                max_y = rec.y + rec.h
            if rec.x < min_x:
                min_x = rec.x
            if rec.y < min_y:
                min_y = rec.y
        return Rectangle(min_x, min_y, max_x - min_x, max_y - min_y)
        

    def num_elements(self):
        """cluster 中矩形的数量"""
        return len(self.rectangles)

    def covered_area(self):
        """cluster 所有矩形覆盖的并集面积（单位格子数）"""
        max_rec = self.get_max_rectangle()
        table = [[0 for _ in range(max_rec.w)] for _ in range(max_rec.h)]
        for rec in self.rectangles:
            for x in range(rec.x - max_rec.x, rec.x - max_rec.x + rec.w):
                for y in range(rec.y - max_rec.y, rec.y - max_rec.y + rec.h):
                    table[y][x] += 1
        area_covered = 0
        for row in table:
            for p in row:
                if p > 0:
                    area_covered += 1
        return area_covered
    
    def max_thickness(self):
        """cluster 中单位格子被覆盖的最大次数（厚さの最大値）"""
        max_rec = self.get_max_rectangle()
        table = [[0] * max_rec.w for _ in range(max_rec.h)]
        for rec in self.rectangles:
            for x in range(rec.x - max_rec.x, rec.x - max_rec.x + rec.w):
                for y in range(rec.y - max_rec.y, rec.y - max_rec.y + rec.h):
                    table[y][x] += 1
        return max(p for row in table for p in row)
        


class RectangleLayout:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    @classmethod
    def from_file(cls, filename):
        """从文件读取矩形数据，返回 RectangleLayout 实例"""
        lines = []
        with open(filename, 'r') as f:
            for line in f:
                if len(line) > 0:
                    lines.append(line)
        recs = []
        for line in lines:
            recs.append(list(map(int, re.split(r'\s+', line.strip()))))
        rectangles = [Rectangle(*rec) for rec in recs]
        return cls(rectangles)

    def get_clusters(self):
        """将矩形按连通性分组，返回 list[Cluster]"""
        n = len(self.rectangles)
        parent = list(range(n))
        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
            
        for i in range(n):
            for j in range(i + 1, n):
                if self.rectangles[i].is_connected(self.rectangles[j]):
                    union(i, j)
                    
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(self.rectangles[i])
            
        return [Cluster(recs) for recs in groups.values()]

    def total_area_sum(self):
        """Q2: 所有矩形面积之和 Σ(w×h)"""
        recs = self.rectangles
        area_sum = 0
        for rec in recs:
            area_sum += rec.area()
        return area_sum

    def max_thickness(self):
        """Q1-1 / Q3-1: 最大厚度（某单位格子被最多几个矩形覆盖）"""
        # clusters = self.get_clusters()
        # max_thickness = 0
        # for cluster in clusters:
        #     thickness = cluster.max_thickness()
        #     if thickness > max_thickness:
        #         max_thickness = thickness
        # return max_thickness
        return max(c.max_thickness() for c in self.get_clusters())

    def num_clusters(self):
        """Q1-2 / Q3-2: cluster 总数"""
        return len(self.get_clusters())

    def max_cluster_elements(self):
        """Q1-3 / Q3-3: 单个 cluster 的最大矩形数"""
        max_ele = 0
        for cluster in self.get_clusters():
            num_ele = cluster.num_elements()
            if num_ele > max_ele:
                max_ele = num_ele
        return max_ele

    def max_cluster_area(self):
        """Q1-4 / Q3-4: 单个 cluster 的最大覆盖面积"""
        max_area = 0
        for cluster in self.get_clusters():
            area_covered = cluster.covered_area()
            if area_covered > max_area:
                max_area = area_covered
        return max_area


def main():
    # Q1: 10.txt
    layout_10 = RectangleLayout.from_file('data/10.txt')
    print(layout_10.max_thickness())       # (1-1)
    print(layout_10.num_clusters())        # (1-2)
    print(layout_10.max_cluster_elements()) # (1-3)
    print(layout_10.max_cluster_area())    # (1-4)

    # Q2 + Q3: 1000.txt
    layout_1000 = RectangleLayout.from_file('data/1000.txt')
    print(layout_1000.total_area_sum())       # Q2
    print(layout_1000.max_thickness())        # (3-1)
    print(layout_1000.num_clusters())         # (3-2)
    print(layout_1000.max_cluster_elements()) # (3-3)
    print(layout_1000.max_cluster_area())     # (3-4)


if __name__ == '__main__':
    main()
