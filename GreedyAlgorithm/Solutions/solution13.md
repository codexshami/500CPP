# Solution 13: Interval Scheduling — Maximum Non-Overlapping Intervals

## Approach Explanation
Sort intervals by end time. Greedily select intervals that don't overlap with the last selected one. Choosing the earliest-ending interval maximizes room for future intervals.

## Step-by-Step Logic
1. Sort intervals by end time.
2. Select the first interval. Track its end time.
3. For each subsequent interval, if its start >= last end, select it and update end time.
4. Return the count.

## Complexity
- **Time Complexity:** O(N log N) for sorting.
- **Space Complexity:** O(1).

## Code
```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    
    count = 1
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count
```
