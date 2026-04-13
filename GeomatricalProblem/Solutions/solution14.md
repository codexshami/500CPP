# Solution 14: Check Rectangle Overlap

## Approach Explanation
Two rectangles don't overlap if one is above, below, left, or right of the other.

## Step-by-Step Logic
1. Check non-overlap conditions.
2. Return negation.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def is_overlap(r1, r2):
    # r = [x1, y1, x2, y2]
    if r1[0] >= r2[2] or r2[0] >= r1[2]:
        return False
    if r1[1] >= r2[3] or r2[1] >= r1[3]:
        return False
    return True
```
