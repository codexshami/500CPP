# Solution 10: Jump Game II

## Approach Explanation
Use a BFS-like greedy approach. Track the current jump range and the farthest reachable. When we exhaust the current range, increment jumps and extend to the farthest reachable point.

## Step-by-Step Logic
1. Initialize `jumps = 0`, `current_end = 0`, `farthest = 0`.
2. For each index `i` (up to n-2), update `farthest = max(farthest, i + nums[i])`.
3. When `i == current_end`, we must jump: increment `jumps`, set `current_end = farthest`.
4. Return `jumps`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps
```
