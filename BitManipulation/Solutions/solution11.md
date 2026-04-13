# Solution 11: Bitwise AND of Numbers Range

## Approach Explanation
Find the common bit prefix of `left` and `right`. Right-shift both until they are equal, then left-shift back by the number of shifts.

## Step-by-Step Logic
1. Count shifts while `left != right`: right-shift both by 1.
2. Left-shift the common prefix back by the shift count.

## Complexity
- **Time Complexity:** O(1) — at most 31 shifts.
- **Space Complexity:** O(1).

## Code
```python
def range_bitwise_and(left, right):
    shifts = 0
    while left != right:
        left >>= 1
        right >>= 1
        shifts += 1
    return left << shifts
```
