# Solution 13: Rotate Point Around Origin

## Approach Explanation
Apply rotation matrix: x'=x*cos(θ)-y*sin(θ), y'=x*sin(θ)+y*cos(θ).

## Step-by-Step Logic
1. Convert angle to radians.
2. Apply rotation formulas.
3. Return new coordinates.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
import math
def rotate_point(x, y, angle_deg):
    angle = math.radians(angle_deg)
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return (round(x_new, 10), round(y_new, 10))
```
