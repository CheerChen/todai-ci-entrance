# coding=utf-8
import argparse
import re
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line)
    return lines


def q1_1(a_file):
    vertices = set()
    lines = read_file(a_file)
    for line in lines:
        matches = re.findall(r'\d+', line)
        vertices.add(matches[0])
        vertices.add(matches[1])

    return len(vertices)


def createOutGraph(file):
    graph = {}
    with open(file, 'r') as f:
        for line in f:
            if len(line) > 0:
                matches = re.findall(r'\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if line[0] != '!':
                    if v0 not in graph:
                        graph[v0] = []
                    graph[v0].append(v1)
                else:
                    if len(graph[v0]) == 1:
                        del graph[v0]
                    else:
                        del graph[v0][graph[v0].index(v1)]

    return graph


def createInGraph(file):
    graph = {}
    with open(file, 'r') as f:
        for line in f:
            if len(line) > 0:
                matches = re.findall(r'\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if v1 not in graph:
                    graph[v1] = []
                graph[v1].append(v0)

    return graph


def findMaxOutDegree(a_file):
    maxLen = 0
    maxOut = ''
    graph = createOutGraph(a_file)
    for k in graph.keys():
        if len(graph[k]) > maxLen:
            maxLen = len(graph[k])
            maxOut = k

    return maxOut, maxLen


def findMaxInDegree(a_file):
    maxLen = 0
    maxIn = ''
    graph = createInGraph(a_file)

    for k in graph.keys():
        if len(graph[k]) > maxLen:
            maxLen = len(graph[k])
            maxIn = k

    return maxIn, maxLen


def find1000Vt(a_file):
    vertices = set()
    t = 0
    with open(a_file, 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall(r'\d+', line)
                vertices.add(matches[0])
                vertices.add(matches[1])
            if len(vertices) >= 1000:
                break

    return t


def findReachable(v0, g):
    rt = [v0]
    next_rt = [v0]
    is_cycle = False
    while len(next_rt) != 0:
        temp = []
        for v in next_rt:
            if v in g and len(g[v]) > 0:
                temp += g[v]
        for v in temp:
            if v in rt:
                is_cycle = True
                temp.remove(v)
        next_rt = temp
        rt += temp
    return rt, is_cycle


def q1_3(a_file):
    graph = {}
    veryFirst = ''
    t = 0
    with open(a_file, 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall(r'\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if v0 not in graph:
                    graph[v0] = []
                graph[v0].append(v1)

                if t == 1:
                    veryFirst = v0
                rt, _ = findReachable(veryFirst, graph)

                if len(rt) >= 1000:
                    break
    return t


def findCycleT(a_file):
    graph = {}
    veryFirst = ''
    t = 0
    with open(a_file, 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall(r'\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if v0 not in graph:
                    graph[v0] = []
                graph[v0].append(v1)

                if t == 1:
                    veryFirst = v0
                rt, is_cycle = findReachable(veryFirst, graph)

                if is_cycle:
                    break
    return t


def q2_1(b_file):
    vertices = set()
    arc_count = 0
    out_graph = createOutGraph(b_file)
    for v0 in out_graph.keys():
        vertices.add(v0)
        for v1 in out_graph[v0]:
            vertices.add(v1)
            arc_count += 1

    return len(vertices), arc_count


def createAt(file):
    at = []
    with open(file, 'r') as f:
        for line in f:
            if len(line) > 0:
                matches = re.findall(r'\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if line[0] != '!':
                    at.append([v0, v1])
                else:
                    at.remove([v0, v1])
    return at


def q2_2(b_file):
    out_graph = createOutGraph(b_file)
    at = createAt(b_file)
    print(len(at))
    rt, _ = findReachable(at[0][0], out_graph)

    return len(rt)


def run(a_file, b_file):
    print(q1_1(a_file))
    print(findMaxOutDegree(a_file))
    print(findMaxInDegree(a_file))
    print(find1000Vt(a_file))
    print(q1_3(a_file))
    print(findCycleT(a_file))
    print(q2_1(b_file))
    print(q2_2(b_file))


def data_file(name):
    path = Path(name)
    if path.exists():
        return path
    return DATA_DIR / name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a-file', default='a.txt')
    parser.add_argument('--b-file', default='b.txt')
    args = parser.parse_args()
    run(data_file(args.a_file), data_file(args.b_file))


if __name__ == '__main__':
    main()
