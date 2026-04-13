# Solution 19: Armstrong Number

## Approach Explanation
Sum the kth power of each digit (k = number of digits). Compare with original.

## Step-by-Step Logic
1. Count digits k.
2. Sum each digit raised to power k.
3. Compare with original.

## Complexity
- **Time Complexity:** O(k) where k is number of digits
- **Space Complexity:** O(1)

## Code
```python
def is_armstrong(n):
    digits = str(n)
    k = len(digits)
    return sum(int(d)**k for d in digits) == n
```
