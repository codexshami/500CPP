# Solution 16: Task Scheduler

## Approach Explanation
The most frequent task determines the minimum intervals. Place the most frequent task in slots separated by `n` gaps, then fill gaps with other tasks. Formula: `intervals = (max_freq - 1) * (n + 1) + count_of_max_freq_tasks`.

## Step-by-Step Logic
1. Count the frequency of each task.
2. Find the maximum frequency `max_freq`.
3. Count how many tasks have `max_freq`.
4. Result = `max((max_freq - 1) * (n + 1) + max_count, len(tasks))`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) — at most 26 unique tasks.

## Code
```python
from collections import Counter

def least_interval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for v in freq.values() if v == max_freq)
    
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(intervals, len(tasks))
```
