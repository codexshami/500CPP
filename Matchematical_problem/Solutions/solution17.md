# Solution 17: Ugly Number

## Approach Explanation
Repeatedly divide by 2, 3, 5. If result is 1, it's ugly.

## Step-by-Step Logic
1. If n <= 0, return False.
2. Divide by 2, 3, 5 while divisible.
3. Check if result is 1.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Code
```python
def is_ugly(n):
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1
```
