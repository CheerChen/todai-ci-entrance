# 2009-08 Rectangle Clusters

CI entrance practice problem about rectangles on a grid.

## Problem

Given rectangles described by `x y width height`, compute:

- maximum thickness
- number of connected clusters
- maximum number of rectangles in one cluster
- maximum covered area of one cluster
- total area sum for the 1000-rectangle dataset

## Files

- `problem/`: original problem PDFs
- `data/`: input datasets
- `solutions/v0-original-2017.py`: original 2017 implementation
- `solutions/v1-python3-improved.py`: Python 3 improved version
- `solutions/v2-oo-refactor.py`: object-oriented refactor

## Run

Run from this directory:

```sh
uv run python solutions/v1-python3-improved.py
```

## Notes

This problem is useful for reviewing grid simulation, rectangle overlap,
connected components, and union-find style grouping.
