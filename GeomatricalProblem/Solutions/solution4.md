# Solution 4: Check Collinear Points

## Approach Explanation
Three points are collinear if the area of triangle they form is 0.

## Step-by-Step Logic
1. Compute cross product (or area).
2. If zero, points are collinear.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def are_collinear(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1]) == 0
```
