# Solution 9: Point in Polygon (Ray Casting)

## Approach Explanation
Cast a ray from the point and count intersections with polygon edges. Odd count means inside.

## Step-by-Step Logic
1. Cast horizontal ray to the right.
2. Count edge crossings.
3. Odd = inside, even = outside.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
def point_in_polygon(polygon, point):
    n = len(polygon)
    inside = False
    x, y = point
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi):
            inside = not inside
        j = i
    return inside
```
