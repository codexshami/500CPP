# Solution 12: Angle Between Two Vectors

## Approach Explanation
Use dot product formula: cos(θ) = (v1·v2) / (|v1|*|v2|).

## Step-by-Step Logic
1. Compute dot product.
2. Compute magnitudes.
3. Apply arccos.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
import math
def angle_between(v1, v2):
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_angle = dot / (mag1 * mag2)
    cos_angle = max(-1, min(1, cos_angle))
    return math.degrees(math.acos(cos_angle))
```
