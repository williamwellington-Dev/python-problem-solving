# Python Problem Solving

Selected solutions from **109 Python Problems**, a public set of algorithmic programming problems by Ilkka Kokkarinen ([problem specs and tester](https://github.com/ikokkari/PythonProblems)). I solved these during my Computer Science minor at Toronto Metropolitan University in 2021.

I solved **46 problems** from the set. All of them pass the set's automated tester, which runs each function against thousands of generated test cases and compares a checksum of the results with the instructor's model solutions. This repo shows 10 of them.

## Selected Solutions

All solutions are in [`solutions.py`](solutions.py).

| Problem | What it does | Technique |
|---|---|---|
| `josephus` | Elimination order when every k-th person in a circle is removed | List simulation with wraparound indexing |
| `first_preceded_by_smaller` | First element with at least k smaller elements before it | Nested scanning |
| `reverse_ascending_sublists` | Reverses each strictly ascending run in a list | Run detection, recursive flattening |
| `collapse_intervals` | Turns `[1, 2, 3, 5, 7, 8]` into `"1-3,5,7-8"` | Single-pass scan for consecutive runs |
| `knight_jump` | Checks a knight move in any number of dimensions | Matching coordinate differences |
| `give_change` | Breaks an amount into coins | Greedy algorithm |
| `milton_work_point_count` | Scores a bridge hand with shape and suit adjustments | Rule-based scoring with dictionaries |
| `eliminate_neighbours` | Counts removals until the largest number is eliminated | Step-by-step list simulation |
| `words_with_given_shape` | Finds words matching an up/down/same letter pattern | List comprehensions, pattern matching |
| `perimeter_limit_split` | Minimum cuts to split a rectangle into pieces under a perimeter limit | Recursion with memoization (dynamic programming) |

## Test Results

```
josephus: Success in 51.550 seconds.
first_preceded_by_smaller: Success in 3.795 seconds.
reverse_ascending_sublists: Success in 3.219 seconds.
collapse_intervals: Success in 0.561 seconds.
knight_jump: Success in 0.539 seconds.
give_change: Success in 0.392 seconds.
milton_work_point_count: Success in 0.189 seconds.
eliminate_neighbours: Success in 17.068 seconds.
words_with_given_shape: Success in 5.953 seconds.
perimeter_limit_split: Success in 5.277 seconds.
10 out of 10 functions of 109 possible work.
```

To verify: clone the [problem repo](https://github.com/ikokkari/PythonProblems), copy `solutions.py` into it as `labs109.py`, and run `python tester109.py`.

## What I'd Improve Today

These are my original solutions from 2021. Looking back at them:

- **`josephus` is the slowest (about 50 seconds).** Deleting from the middle of a Python list shifts every element after it, so the algorithm is O(n²). A `collections.deque` rotated with `rotate()` would avoid most of that cost.
- **`first_preceded_by_smaller`** recounts all earlier elements for every position, which is also O(n²). Keeping the earlier elements in a sorted structure (with `bisect`) would make each check much faster.
- **`eliminate_neighbours`** calls `items.index()` on every step, which searches the whole list each time. Tracking positions in a dictionary, or using a linked structure, would speed it up.
- **`reverse_ascending_sublists`** uses a recursive `flatten` lambda where a simple loop that extends the result list would be clearer.

## Notes

- The problems, specifications, and tester belong to Ilkka Kokkarinen and are released under the GNU GPL v3 in the linked repository. Only my solutions are included here.
- The solution logic is unchanged from my 2021 coursework. Formatting was standardized and docstrings were added with AI assistance.

**Author:** William Wellington
