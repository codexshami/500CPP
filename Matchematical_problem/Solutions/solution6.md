# Solution 6: Factorial Trailing Zeros

## Approach Explanation
Count factors of 5 in n!. Every pair of 2 and 5 contributes a trailing zero, and 2s are always more plentiful.

## Step-by-Step Logic
1. Count = n//5 + n//25 + n//125 + ...
2. Keep dividing n by 5 and adding.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Code
```python
def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
```
