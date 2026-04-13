# Solution 9: Single Number II

## Approach Explanation
Use two variables `ones` and `twos` to track bits appearing once and twice. When a bit appears three times, it's cleared from both.

## Step-by-Step Logic
1. Initialize `ones = 0`, `twos = 0`.
2. For each number: `ones = (ones ^ num) & ~twos`, `twos = (twos ^ num) & ~ones`.
3. Return `ones`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def single_number_ii(nums):
    ones = 0
    twos = 0
    
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    
    return ones
```
