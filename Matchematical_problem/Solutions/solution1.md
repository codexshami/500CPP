# Solution 1: GCD and LCM

## Approach Explanation
Use Euclid's algorithm for GCD. LCM = (a * b) / GCD(a, b).

## Step-by-Step Logic
1. Compute GCD using Euclid's algorithm: gcd(a, b) = gcd(b, a%b).
2. Compute LCM = a * b // gcd.

## Complexity
- **Time Complexity:** O(log(min(a,b)))
- **Space Complexity:** O(1)

## Code
```python
import math

def gcd_lcm(a, b):
    g = math.gcd(a, b)
    l = a * b // g
    return (g, l)
```
