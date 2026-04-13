# Solution 7: Count Digits in Factorial

## Approach Explanation
Use Kamenetsky's formula: digits ≈ log10(n!) = Σlog10(i) for i=1..n, or use Stirling's approx.

## Step-by-Step Logic
1. Sum log10(i) for i from 1 to n.
2. Return floor(sum) + 1.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
import math

def count_digits_factorial(n):
    if n <= 1:
        return 1
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
    return int(digits) + 1
```
