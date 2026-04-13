# Solution 3: Convex Hull (Graham Scan)

## Approach Explanation
Find the bottom-most point, sort by polar angle, and process points maintaining a left-turn stack.

## Step-by-Step Logic
1. Find anchor point.
2. Sort remaining by polar angle.
3. Process with stack, maintaining convexity.

## Complexity
- **Time Complexity:** O(N log N)
- **Space Complexity:** O(N)

## Code
```python
def convex_hull(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]
```
