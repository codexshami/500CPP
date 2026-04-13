# Solution 6: Closest Pair of Points

## Approach Explanation
Sort points by x-coordinate. Divide into two halves. Find closest pair in each half and the strip around the dividing line. The answer is the minimum of all three.

## Step-by-Step Logic
1. Sort points by x-coordinate.
2. Recursively find closest distance in left and right halves.
3. Find the strip of points within `delta` of the midline.
4. Check pairs in the strip (sorted by y) — at most 7 comparisons per point.
5. Return minimum distance.

## Complexity
- **Time Complexity:** O(N log²N) or O(N log N) with optimization.
- **Space Complexity:** O(N).

## Code
```python
import math

def closest_pair(points):
    points.sort()
    return closest_util(points)

def closest_util(pts):
    n = len(pts)
    if n <= 3:
        return brute_force(pts)
    
    mid = n // 2
    mid_point = pts[mid]
    
    dl = closest_util(pts[:mid])
    dr = closest_util(pts[mid:])
    d = min(dl, dr)
    
    strip = [p for p in pts if abs(p[0] - mid_point[0]) < d]
    strip.sort(key=lambda p: p[1])
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            d = min(d, dist(strip[i], strip[j]))
            j += 1
    
    return d

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def brute_force(pts):
    min_d = float('inf')
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            min_d = min(min_d, dist(pts[i], pts[j]))
    return min_d
```
