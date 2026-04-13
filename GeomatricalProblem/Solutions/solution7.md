# Solution 7: Circle-Line Intersection

## Approach Explanation
Substitute line equation into circle equation and solve the resulting quadratic.

## Step-by-Step Logic
1. Set up quadratic equation.
2. Compute discriminant.
3. Find intersection points if discriminant >= 0.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
import math
def circle_line_intersect(cx, cy, r, p1, p2):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    fx, fy = p1[0]-cx, p1[1]-cy
    a = dx*dx + dy*dy
    b = 2*(fx*dx + fy*dy)
    c = fx*fx + fy*fy - r*r
    disc = b*b - 4*a*c
    if disc < 0: return []
    disc = math.sqrt(disc)
    t1 = (-b - disc) / (2*a)
    t2 = (-b + disc) / (2*a)
    pts = []
    for t in [t1, t2]:
        pts.append((p1[0]+t*dx, p1[1]+t*dy))
    return pts
```
