# Solution 10: Single Number III

## Approach Explanation
XOR all numbers to get `xor = a ^ b`. Find a set bit in `xor` (differentiating bit). Partition numbers into two groups based on that bit and XOR each group separately.

## Step-by-Step Logic
1. XOR all elements → `xor_all = a ^ b`.
2. Find the rightmost set bit: `diff_bit = xor_all & (-xor_all)`.
3. Partition and XOR: one group with that bit set, one without.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def single_number_iii(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Get rightmost set bit
    diff_bit = xor_all & (-xor_all)
    
    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num
    
    return [a, b]
```
