# Solution 11: Check if Point is on Line Segment

## Approach Explanation
Check if point is collinear with endpoints and lies within the bounding box.

## Step-by-Step Logic
1. Check collinearity using cross product.
2. Check bounding box constraints.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def on_segment(a, b, p):
    cross = (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0])
    if abs(cross) > 1e-9:
        return False
    return min(a[0],b[0]) <= p[0] <= max(a[0],b[0]) and min(a[1],b[1]) <= p[1] <= max(a[1],b[1])
```
