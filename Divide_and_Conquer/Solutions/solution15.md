# Solution 15: Karatsuba Multiplication

## Approach Explanation
Split each number into two halves. Compute three products instead of four: `z0 = low1*low2`, `z2 = high1*high2`, `z1 = (low1+high1)*(low2+high2) - z0 - z2`.

## Step-by-Step Logic
1. Base case: if either number < 10, multiply directly.
2. Find the number of digits `m` and split.
3. Compute three recursive multiplications.
4. Combine: `z2 * 10^(2*half) + z1 * 10^half + z0`.

## Complexity
- **Time Complexity:** O(N^1.585).
- **Space Complexity:** O(N log N).

## Code
```python
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    high1 = x // (10 ** half)
    low1 = x % (10 ** half)
    high2 = y // (10 ** half)
    low2 = y % (10 ** half)
    
    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2) - z0 - z2
    
    return z2 * (10 ** (2 * half)) + z1 * (10 ** half) + z0
```
