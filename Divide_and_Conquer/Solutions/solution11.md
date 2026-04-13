# Solution 11: Search in Rotated Sorted Array

## Approach Explanation
Modified binary search. At each step, one half is always sorted. Check if the target lies in the sorted half, and adjust search range accordingly.

## Step-by-Step Logic
1. Find mid. One of the halves is always sorted.
2. If left half is sorted and target is within it, search left. Otherwise search right.
3. If right half is sorted and target is within it, search right. Otherwise search left.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def search_rotated(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1
```
