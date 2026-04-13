# Solution 12: Power Set using Bits

## Approach Explanation
For `n` elements, there are `2^n` subsets. Each number from `0` to `2^n - 1` represents a subset where the i-th bit indicates whether `nums[i]` is included.

## Step-by-Step Logic
1. For each number `mask` from 0 to `2^n - 1`.
2. Check each bit: if bit `j` is set, include `nums[j]` in the subset.
3. Collect all subsets.

## Complexity
- **Time Complexity:** O(N * 2^N).
- **Space Complexity:** O(N * 2^N).

## Code
```python
def power_set(nums):
    n = len(nums)
    result = []
    
    for mask in range(1 << n):
        subset = []
        for j in range(n):
            if mask & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    
    return result
```
