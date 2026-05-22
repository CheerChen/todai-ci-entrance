# coding=utf-8
import re
import sys
sys.setrecursionlimit(20000)
from collections import defaultdict
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


class ArcOperation:
    def __init__(self, source, target, is_delete=False):
        self.source = source
        self.target = target
        self.is_delete = is_delete

    @classmethod
    def from_line(cls, line):
        numbers = re.findall(r'\d+', line)
        return cls(numbers[0], numbers[1], line.startswith('!'))


class DynamicDirectedGraph:
    def __init__(self):
        self.out_graph = defaultdict(set)
        self.in_graph = defaultdict(set)
        self.vertices = set()

    def add_arc(self, source, target):
        self.vertices.add(source)
        self.vertices.add(target)
        self.out_graph[source].add(target)
        self.in_graph[target].add(source)

    def remove_arc(self, source, target):
        if source in self.out_graph:
            self.out_graph[source].discard(target)
            if len(self.out_graph[source]) == 0:
                del self.out_graph[source]

        if target in self.in_graph:
            self.in_graph[target].discard(source)
            if len(self.in_graph[target]) == 0:
                del self.in_graph[target]

    def apply(self, operation):
        if operation.is_delete:
            self.remove_arc(operation.source, operation.target)
        else:
            self.add_arc(operation.source, operation.target)

    def max_out_degree(self):
        return self._max_degree(self.out_graph)

    def max_in_degree(self):
        return self._max_degree(self.in_graph)

    def arc_count(self):
        total = 0
        for targets in self.out_graph.values():
            total += len(targets)
        return total

    def traverse_from(self, start):
        reachable = set()
        visiting = set()
        visited = set()
        has_cycle = False

        def dfs(vertex):
            # 闭包捕获外层变量
            nonlocal has_cycle

            if vertex in visiting:
                has_cycle = True
                return
            if vertex in visited:
                return

            reachable.add(vertex)
            visiting.add(vertex)

            for next_vertex in self.out_graph.get(vertex, []):
                dfs(next_vertex)

            visiting.remove(vertex)
            visited.add(vertex)

        if start is not None:
            dfs(start)

        return reachable, has_cycle

    def reachable_from(self, start):
        reachable, _ = self.traverse_from(start)
        return reachable

    def has_cycle_from(self, start):
        _, has_cycle = self.traverse_from(start)
        return has_cycle

    def _max_degree(self, graph):
        max_vertex = ''
        max_len = 0
        for vertex in graph.keys():
            if len(graph[vertex]) > max_len:
                max_len = len(graph[vertex])
                max_vertex = vertex
        return max_vertex, max_len


def read_operations(filename):
    operations = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0:
                operations.append(ArcOperation.from_line(line))
    return operations


def vertex_count_seen_in_input(operations):
    vertices = set()
    for operation in operations:
        vertices.add(operation.source)
        vertices.add(operation.target)
    return len(vertices)


def graph_after_operations(operations):
    graph = DynamicDirectedGraph()
    for operation in operations:
        graph.apply(operation)
    return graph


def first_line_seen_vertices_reach(operations, count):
    vertices = set()
    for line_number, operation in enumerate(operations, start=1):
        vertices.add(operation.source)
        vertices.add(operation.target)
        if len(vertices) >= count:
            return line_number
    return None


# def first_source(operations):
#     if len(operations) == 0:
#         return None
#     return operations[0].source


def first_line_reachable_vertices_reach(operations, count):
    graph = DynamicDirectedGraph()
    start = "0"

    for line_number, operation in enumerate(operations, start=1):
        graph.apply(operation)

        reachable, _ = graph.traverse_from(start)
        if len(reachable) >= count:
            return line_number
    return None


def first_line_cycle_reachable_from_start(operations):
    graph = DynamicDirectedGraph()
    start = "0"

    for line_number, operation in enumerate(operations, start=1):
        graph.apply(operation)

        _, has_cycle = graph.traverse_from(start)
        if has_cycle:
            return line_number
    return None


def data_file(name):
    path = Path(name)
    if path.exists():
        return path
    return DATA_DIR / name


def lines_where_root_set_reach_limit(operations, limit):
    graph = DynamicDirectedGraph()
    t_list = []
    prev = 1
    for line_number, operation in enumerate(operations, start=1):
        graph.apply(operation)
        reachable = graph.reachable_from("0")
        # print(f'line {line_number} reachable: {len(reachable)}')
        if len(reachable) >= limit and prev < limit:
            t_list.append(line_number)
        prev = len(reachable)
    return t_list


def main():
    operations = read_operations(data_file('a.txt'))
    graph = graph_after_operations(operations)

    # Q1-1: |V_a|
    q1_1 = vertex_count_seen_in_input(operations)
    print('Q1-1   |V_a|        :', q1_1)

    # Q1-2: max out-degree / max in-degree (vertex, degree)
    q1_2_1 = graph.max_out_degree()
    q1_2_2 = graph.max_in_degree()
    print('Q1-2-1 max out-deg   :', q1_2_1)
    print('Q1-2-2 max in-deg    :', q1_2_2)

    # Q1-3: first t with |V(t)| >= 1000 / first t with |R(t)| >= 1000
    q1_3_1 = first_line_seen_vertices_reach(operations, 1000)
    q1_3_2 = first_line_reachable_vertices_reach(operations, 1000)
    print('Q1-3-1 t_v           :', q1_3_1)
    print('Q1-3-2 t_r           :', q1_3_2)

    # Q1-4: first t when v_0 creates a cycle
    q1_4 = first_line_cycle_reachable_from_start(operations)
    print('Q1-4   cycle t       :', q1_4)
    
    operations = read_operations(data_file('b.txt'))
    graph = graph_after_operations(operations)
    
    # Q2-1: |V_b|, |A_b|
    q2_1 = graph.arc_count()
    print('Q2-1   |A_b|        :', q2_1)
    q2_2 = len(graph.reachable_from("0"))
    print('Q2-2   |R_b|        :', q2_2)
    q2_3 = lines_where_root_set_reach_limit(operations, 1000)
    print('Q2-3   t with R=1000 :', q2_3)


if __name__ == '__main__':
    main()
