# Solution 13: Euler's Totient Function

## Approach Explanation
Use the formula: φ(n) = n * Π(1 - 1/p) for each prime factor p of n.

## Step-by-Step Logic
1. Start with result = n.
2. For each prime factor p, multiply result by (1 - 1/p).
3. Handle repeated factors.

## Complexity
- **Time Complexity:** O(√N)
- **Space Complexity:** O(1)

## Code
```python
def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
```
