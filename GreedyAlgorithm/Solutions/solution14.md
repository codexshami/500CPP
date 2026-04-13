# Solution 14: Minimum Number of Arrows to Burst Balloons

## Approach Explanation
Sort balloons by end position. Shoot an arrow at the end of the first balloon. Any overlapping balloon is also burst. For non-overlapping balloons, shoot a new arrow.

## Step-by-Step Logic
1. Sort balloons by their end coordinate.
2. Set `arrow_pos` to the end of the first balloon. Count = 1.
3. For each balloon, if its start > `arrow_pos`, shoot a new arrow at the current balloon's end.
4. Return total arrows.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(1).

## Code
```python
def find_min_arrows(points):
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    arrow_pos = points[0][1]
    
    for start, end in points[1:]:
        if start > arrow_pos:
            arrows += 1
            arrow_pos = end
    
    return arrows
```
