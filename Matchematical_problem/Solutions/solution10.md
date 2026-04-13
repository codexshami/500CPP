# Solution 10: nCr (Binomial Coefficient)

## Approach Explanation
Use DP table or the multiplicative formula: C(n,r) = n!/(r!*(n-r)!).

## Step-by-Step Logic
1. Use iterative multiplication to avoid overflow.
2. C(n,r) = C(n,n-r) for optimization.

## Complexity
- **Time Complexity:** O(R)
- **Space Complexity:** O(1)

## Code
```python
def ncr(n, r):
    if r > n - r:
        r = n - r
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result
```
