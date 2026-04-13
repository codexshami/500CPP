# Solution 15: Perimeter of Polygon

## Approach Explanation
Sum distances between consecutive vertices (including last to first).

## Step-by-Step Logic
1. Iterate through vertices.
2. Add distance between consecutive pairs.
3. Include closing edge.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
import math
def polygon_perimeter(vertices):
    n = len(vertices)
    perimeter = 0
    for i in range(n):
        j = (i + 1) % n
        perimeter += math.sqrt((vertices[j][0]-vertices[i][0])**2 + (vertices[j][1]-vertices[i][1])**2)
    return perimeter
```
