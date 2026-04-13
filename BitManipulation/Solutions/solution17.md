# Solution 17: Find Two Non-Repeating Elements

## Approach Explanation
Same as Single Number III. XOR all to get combined XOR of the two unique numbers. Use a differentiating bit to split into two groups.

## Step-by-Step Logic
1. XOR all elements → `xor_all`.
2. Find any set bit in `xor_all`: `diff = xor_all & (-xor_all)`.
3. Partition array and XOR each group.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def find_two_non_repeating(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    diff = xor_all & (-xor_all)
    
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    
    return [a, b]
```
