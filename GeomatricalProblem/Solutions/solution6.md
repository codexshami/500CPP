# Solution 6: Line Intersection

## Approach Explanation
Use parametric form and solve the system of equations. Check if parameters are within [0,1] for segments.

## Step-by-Step Logic
1. Express lines parametrically.
2. Solve for parameters using cross products.
3. Check bounds.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def line_intersection(p1, p2, p3, p4):
    d = (p1[0]-p2[0])*(p3[1]-p4[1]) - (p1[1]-p2[1])*(p3[0]-p4[0])
    if d == 0:
        return None  # Parallel
    t = ((p1[0]-p3[0])*(p3[1]-p4[1]) - (p1[1]-p3[1])*(p3[0]-p4[0])) / d
    x = p1[0] + t*(p2[0]-p1[0])
    y = p1[1] + t*(p2[1]-p1[1])
    return (x, y)
```
