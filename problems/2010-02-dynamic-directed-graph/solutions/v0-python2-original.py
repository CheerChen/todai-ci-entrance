# coding=utf-8
# 读取图的数据生成图
import re


def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line)
    return lines


def q1_1():
    vertices = set()
    lines = read_file('a.txt')
    for line in lines:
        matches = re.findall('\d+', line)
        vertices.add(matches[0])
        vertices.add(matches[1])

    return len(vertices)


def createOutGraph(file):
    graph = {}
    with open(file, 'r') as f:
        for line in f:
            if len(line) > 0:
                matches = re.findall('\d+', line)
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
                matches = re.findall('\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if v1 not in graph:
                    graph[v1] = []
                graph[v1].append(v0)

    return graph


def findMaxOutDegree():
    maxLen = 0
    maxOut = ''
    graph = createOutGraph('a.txt')
    for k in graph.keys():
        if len(graph[k]) > maxLen:
            maxLen = len(graph[k])
            maxOut = k

    return maxOut, maxLen


def findMaxInDegree():
    maxLen = 0
    maxIn = ''
    graph = createInGraph('a.txt')

    for k in graph.keys():
        if len(graph[k]) > maxLen:
            maxLen = len(graph[k])
            maxIn = k

    return maxIn, maxLen


print q1_1()
print findMaxOutDegree()
print findMaxInDegree()


def find1000Vt():
    vertices = set()
    t = 0
    with open('a.txt', 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall('\d+', line)
                vertices.add(matches[0])
                vertices.add(matches[1])
            if len(vertices) >= 1000:
                break

    return t


print find1000Vt()


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


def q1_3():
    graph = {}
    veryFirst = ''
    t = 0
    with open('a.txt', 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall('\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if v0 not in graph:
                    graph[v0] = []
                graph[v0].append(v1)

                if t == 1:
                    veryFirst = v0
                rt, _ = findReachable(veryFirst, graph)

                # print 'current reachable:' , len(rt)

                if len(rt) >= 1000:
                    break
    return t


print q1_3()


def findCycleT():
    graph = {}
    veryFirst = ''
    t = 0
    with open('a.txt', 'r') as f:
        for line in f:
            if len(line) > 0:
                t += 1
                matches = re.findall('\d+', line)
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


print findCycleT()


# exclamation mark

def q2_1():
    vertices = set()
    arc_count = 0
    out_graph = createOutGraph('b.txt')
    for v0 in out_graph.keys():
        vertices.add(v0)
        for v1 in out_graph[v0]:
            vertices.add(v1)
            arc_count += 1

    return len(vertices), arc_count


print q2_1()


def createAt(file):
    at = []
    with open(file, 'r') as f:
        for line in f:
            if len(line) > 0:
                matches = re.findall('\d+', line)
                v0 = matches[0]
                v1 = matches[1]
                if line[0] != '!':
                    at.append([v0, v1])
                else:
                    at.remove([v0, v1])
    return at


def q2_2():
    out_graph = createOutGraph('b.txt')
    at = createAt('b.txt')
    print len(at)
    # print at[0][0]
    rt, _ = findReachable(at[0][0], out_graph)

    return len(rt)


print q2_2()
