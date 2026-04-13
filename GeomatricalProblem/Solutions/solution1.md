# Solution 1: Point in Triangle

## Approach Explanation
Use area method: if Area(PAB) + Area(PBC) + Area(PCA) == Area(ABC), point is inside.

## Step-by-Step Logic
1. Compute area of triangle ABC.
2. Compute areas of PAB, PBC, PCA.
3. Check if sum equals ABC area.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def point_in_triangle(p, a, b, c):
    def area(p1, p2, p3):
        return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)
    
    A = area(a, b, c)
    A1 = area(p, b, c)
    A2 = area(a, p, c)
    A3 = area(a, b, p)
    
    return abs(A - (A1 + A2 + A3)) < 1e-9
```
