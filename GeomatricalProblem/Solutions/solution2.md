# Solution 2: Area of Triangle

## Approach Explanation
Use the Shoelace formula: Area = |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2.

## Step-by-Step Logic
1. Plug coordinates into the formula.
2. Take absolute value and divide by 2.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def triangle_area(p1, p2, p3):
    return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0
```
