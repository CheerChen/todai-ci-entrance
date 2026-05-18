# 2017-02 Source Code Text Analysis

Archived Todai CI entrance programming attempt from 2017-02.

## Status

- Original problem statement is missing.
- Original answers are preserved but known to be incorrect.
- The input data is an extracted Chainer source tree plus provided source snippets.
- The original compressed input package is intentionally not stored in this repo.

## Files

- `problem/`: placeholder for the missing problem statement
- `data/chainer/`: extracted input source tree
- `data/foo.py`: provided source input
- `data/foo_test.py`: provided sample or test snippet
- `solutions/v0-original-wrong/`: original incorrect answer files
- `solutions/v1-python3-improved/`: Python 3 compatible copy for running with uv

## Run

Run from this directory:

```sh
uv run python solutions/v1-python3-improved/q1.py
uv run python solutions/v1-python3-improved/q2.py
echo "word" | uv run python solutions/v1-python3-improved/q3.py
echo "word" | uv run python solutions/v1-python3-improved/q5.py
```

## Notes

Based on the preserved answer files, this problem appears to involve source-code
text analysis tasks such as word extraction, word frequency, lexicographic lookup,
and edit distance.
