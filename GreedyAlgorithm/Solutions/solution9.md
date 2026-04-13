# Solution 9: Jump Game

## Approach Explanation
Track the farthest index reachable. Iterate through the array; at each position, update the farthest reachable index. If the current index exceeds the farthest reachable, return False.

## Step-by-Step Logic
1. Initialize `max_reach = 0`.
2. For each index `i`, if `i > max_reach`, return False (unreachable).
3. Update `max_reach = max(max_reach, i + nums[i])`.
4. If `max_reach >= len(nums) - 1`, return True.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def can_jump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    
    return True
```
