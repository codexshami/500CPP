# Solution 12: Find Peak Element

## Approach Explanation
Binary search: if `nums[mid] < nums[mid+1]`, peak is in the right half. Otherwise, peak is in the left half (including mid).

## Step-by-Step Logic
1. Binary search with `low` and `high`.
2. If `nums[mid] < nums[mid+1]`, move `low = mid + 1`.
3. Else, move `high = mid`.
4. When `low == high`, that's the peak.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def find_peak_element(nums):
    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    
    return low
```
