# Solution 20: Smallest Number with Given Digit Sum and Number of Digits

## Approach Explanation
Greedily assign digits from the last position to the first. Place the largest possible digit (up to 9) at each position from right to left, ensuring the first digit is at least 1.

## Step-by-Step Logic
1. If `s == 0` and `m > 1`, return "-1". If `s == 0` and `m == 1`, return "0".
2. If `s > 9 * m`, return "-1" (impossible).
3. Fill digits from right to left: place `min(s, 9)` at each position.
4. Ensure the leftmost digit is at least 1.

## Complexity
- **Time Complexity:** O(M).
- **Space Complexity:** O(M).

## Code
```python
def smallest_number(m, s):
    if s == 0:
        return "0" if m == 1 else "-1"
    if s > 9 * m:
        return "-1"
    
    result = [0] * m
    
    for i in range(m - 1, -1, -1):
        if i == 0:
            # First digit must be at least 1
            result[i] = s
        else:
            digit = min(s - 1, 9)  # Reserve at least 1 for remaining positions
            result[i] = digit
            s -= digit
    
    return ''.join(map(str, result))
```
