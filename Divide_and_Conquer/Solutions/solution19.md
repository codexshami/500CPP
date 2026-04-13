# Solution 19: Skyline Problem

## Approach Explanation
Divide buildings in half. Recursively compute skylines for each half, then merge the two skylines by tracking the current height of both skylines and outputting changes.

## Step-by-Step Logic
1. Base case: single building produces two key points.
2. Recursively compute left and right skylines.
3. Merge: scan both skylines left to right, tracking current heights.
4. Output a key point whenever the max height changes.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def get_skyline(buildings):
    if not buildings:
        return []
    if len(buildings) == 1:
        l, r, h = buildings[0]
        return [[l, h], [r, 0]]
    
    mid = len(buildings) // 2
    left = get_skyline(buildings[:mid])
    right = get_skyline(buildings[mid:])
    
    return merge_skylines(left, right)

def merge_skylines(left, right):
    result = []
    h1 = h2 = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x = left[i][0]
            h1 = left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            x = right[j][0]
            h2 = right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1
        
        max_h = max(h1, h2)
        if not result or result[-1][1] != max_h:
            result.append([x, max_h])
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
