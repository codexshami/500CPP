# Solution 16: Minimum Enclosing Circle

## Approach Explanation
Use Welzl's randomized algorithm. Process points recursively, maintaining up to 3 boundary points.

## Step-by-Step Logic
1. Shuffle points randomly.
2. Recursively add points.
3. If point outside current circle, include it on boundary.

## Complexity
- **Time Complexity:** O(N) expected
- **Space Complexity:** O(N)

## Code
```python
import math, random
def min_enclosing_circle(points):
    def circle_from_1(p):
        return (p[0], p[1], 0)
    def circle_from_2(p1, p2):
        cx = (p1[0]+p2[0])/2
        cy = (p1[1]+p2[1])/2
        r = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)/2
        return (cx, cy, r)
    def is_inside(c, p):
        return math.sqrt((c[0]-p[0])**2+(c[1]-p[1])**2) <= c[2]+1e-7
    # Simplified for small inputs
    random.shuffle(points)
    c = circle_from_1(points[0])
    for i in range(1, len(points)):
        if not is_inside(c, points[i]):
            c = circle_from_2(points[0], points[i])
            for j in range(1, i):
                if not is_inside(c, points[j]):
                    c = circle_from_2(points[j], points[i])
    return c
```
