# Solution 18: Check if Points Form Square

## Approach Explanation
Compute all 6 pairwise distances. A square has 4 equal sides and 2 equal (longer) diagonals.

## Step-by-Step Logic
1. Compute all 6 distances.
2. Sort them.
3. First 4 should be equal (sides), last 2 equal (diagonals).

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
import math
def is_square(p1, p2, p3, p4):
    def dist_sq(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2
    points = [p1, p2, p3, p4]
    dists = sorted([dist_sq(points[i], points[j]) for i in range(4) for j in range(i+1, 4)])
    return dists[0] > 0 and dists[0]==dists[1]==dists[2]==dists[3] and dists[4]==dists[5]
```
