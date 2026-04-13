# Solution 17: Reflect Point Over Line

## Approach Explanation
Use the reflection formula for point over line ax+by+c=0.

## Step-by-Step Logic
1. Compute d = (ax+by+c)/(a²+b²).
2. x' = x - 2ad, y' = y - 2bd.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def reflect_point(x, y, a, b, c):
    d = (a*x + b*y + c) / (a*a + b*b)
    x_ref = x - 2*a*d
    y_ref = y - 2*b*d
    return (x_ref, y_ref)
```
