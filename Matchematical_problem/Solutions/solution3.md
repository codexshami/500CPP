# Solution 3: Check Prime Number

## Approach Explanation
Check divisibility up to √n. If no divisor found, the number is prime.

## Step-by-Step Logic
1. Handle edge cases: n < 2 is not prime.
2. Check divisibility from 2 to √n.
3. If no divisor found, return True.

## Complexity
- **Time Complexity:** O(√N)
- **Space Complexity:** O(1)

## Code
```python
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
