# 2010-02 Dynamic Directed Graph

CI entrance practice problem about a directed graph that changes over time.

## Problem

Input lines describe directed arcs:

- `u->v` adds an arc from `u` to `v`
- `!u->v` removes an arc from `u` to `v`

The original solution computes vertex counts, maximum outdegree/indegree,
timestamps related to 1000 vertices reachable from the first source vertex,
and final graph statistics after deletions.

## Files

- `problem/`: original problem PDFs
- `data/`: input datasets
- `solutions/v0-python2-original.py`: original Python 2 implementation
- `solutions/v1-python3-improved.py`: Python 3 port of the original logic
- `solutions/v2-oo-refactor.py`: object-oriented graph framework for solving later questions

## Run

Run the original `a.txt` / `b.txt` pairing from the repository root:

```sh
python3 problems/2010-02-dynamic-directed-graph/solutions/v1-python3-improved.py
```

Run the same logic with one dataset substituted for both inputs:

```sh
python3 problems/2010-02-dynamic-directed-graph/solutions/v1-python3-improved.py --a-file a.txt --b-file a.txt
python3 problems/2010-02-dynamic-directed-graph/solutions/v1-python3-improved.py --a-file b.txt --b-file b.txt
python3 problems/2010-02-dynamic-directed-graph/solutions/v1-python3-improved.py --a-file c.txt --b-file c.txt
```

Run the object-oriented framework version on one dataset:

```sh
python3 problems/2010-02-dynamic-directed-graph/solutions/v2-oo-refactor.py a.txt
```

## Recorded Outputs

Default original pairing, `a.txt` for Q1-style functions and `b.txt` for Q2-style functions:

```text
9296
('42', 9)
('5552', 8)
523
10479
10404
(8909, 11172)
11172
7
```

Substituted `a.txt`:

```text
9296
('42', 9)
('5552', 8)
523
10479
10404
(9296, 13400)
13400
6437
```

Substituted `b.txt`:

```text
9832
('8663', 7)
('8726', 14)
755
15135
14127
(8909, 11172)
11172
7
```

Substituted `c.txt`:

```text
5569
('9985', 12)
('1462', 15)
1759
257
17
(5185, 8034)
8034
2
```

## Notes

`v1-python3-improved.py` is intentionally a Python 3 version of the original
source logic, not a corrected graph algorithm. It preserves the old handling of
deletions, indegrees, reachability, duplicate reachable vertices, and cycle
detection behavior.

`v2-oo-refactor.py` is a clearer framework for continuing the problem. It keeps
the graph operations reusable, applies both additions and deletions uniformly,
and uses standard set-based reachability and DFS cycle detection, so its answers
are not intended to be byte-for-byte equivalent to `v1`.
