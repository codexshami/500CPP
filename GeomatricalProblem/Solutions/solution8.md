# Solution 8: Polygon Area (Shoelace Formula)

## Approach Explanation
Sum cross products of consecutive vertices and take half the absolute value.

## Step-by-Step Logic
1. Apply Shoelace formula.
2. Sum x_i*y_{i+1} - x_{i+1}*y_i.
3. Return absolute value / 2.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
```
