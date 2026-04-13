# Solution 5: Maximum Subarray (Divide & Conquer)

## Approach Explanation
Divide at mid. Max subarray is either entirely in left half, entirely in right half, or crossing the midpoint. Solve all three and return the maximum.

## Step-by-Step Logic
1. Base case: single element returns itself.
2. Recursively find max in left and right halves.
3. Find max crossing subarray by extending left and right from mid.
4. Return max of all three.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(log N).

## Code
```python
def max_subarray(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    
    if left == right:
        return nums[left]
    
    mid = (left + right) // 2
    
    left_max = max_subarray(nums, left, mid)
    right_max = max_subarray(nums, mid + 1, right)
    
    # Max crossing subarray
    left_sum = float('-inf')
    curr = 0
    for i in range(mid, left - 1, -1):
        curr += nums[i]
        left_sum = max(left_sum, curr)
    
    right_sum = float('-inf')
    curr = 0
    for i in range(mid + 1, right + 1):
        curr += nums[i]
        right_sum = max(right_sum, curr)
    
    cross_max = left_sum + right_sum
    return max(left_max, right_max, cross_max)
```
