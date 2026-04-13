# Solution 1: Activity Selection

## Approach Explanation
Sort activities by their finish time. Greedily select the first activity and then always pick the next activity whose start time is >= finish time of the previously selected activity.

## Step-by-Step Logic
1. Sort activities by finish time.
2. Select the first activity (earliest finish).
3. For each remaining activity, if its start time >= last selected finish time, select it.
4. Return the count of selected activities.

## Complexity
- **Time Complexity:** O(N log N) for sorting.
- **Space Complexity:** O(1) extra space.

## Code
```python
def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    count = 1
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:
            count += 1
            last_finish = activities[i][1]
    
    return count
```
