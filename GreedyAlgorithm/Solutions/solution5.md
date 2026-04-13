# Solution 5: Minimum Number of Platforms

## Approach Explanation
Sort arrivals and departures independently. Use two pointers to simulate events in chronological order: an arrival adds a platform, a departure frees one. Track the maximum platforms needed at any moment.

## Step-by-Step Logic
1. Sort both `arrivals` and `departures`.
2. Initialize two pointers `i` and `j` at 0, `platforms = 0`, `max_platforms = 0`.
3. If `arrivals[i] <= departures[j]`, increment platforms and move `i`.
4. Otherwise, decrement platforms and move `j`.
5. Track `max_platforms` at each step.

## Complexity
- **Time Complexity:** O(N log N) for sorting.
- **Space Complexity:** O(1) extra space.

## Code
```python
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    platforms = 0
    max_platforms = 0
    i = j = 0
    n = len(arrivals)
    
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    return max_platforms
```
