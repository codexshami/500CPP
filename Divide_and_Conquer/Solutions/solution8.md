# Solution 8: Power Function (x^n)

## Approach Explanation
Use the property: x^n = (x^(n/2))^2 if n is even, x * (x^(n/2))^2 if n is odd. Handle negative exponents by using 1/x.

## Step-by-Step Logic
1. If n < 0, compute `pow(1/x, -n)`.
2. Base case: n == 0 returns 1.
3. Compute `half = pow(x, n // 2)`.
4. If n is even: return `half * half`. If odd: return `half * half * x`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(log N) for recursion.

## Code
```python
def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    
    if n == 0:
        return 1
    
    half = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```
