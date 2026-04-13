# Solution 15: Merge Intervals

## Approach Explanation
Sort intervals by start time. Iterate and merge overlapping intervals by comparing the current interval's start with the previous interval's end.

## Step-by-Step Logic
1. Sort intervals by start time.
2. Initialize `merged` with the first interval.
3. For each interval, if its start <= end of last merged interval, extend the end. Otherwise, add as new interval.
4. Return `merged`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N) for the result.

## Code
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged
```
