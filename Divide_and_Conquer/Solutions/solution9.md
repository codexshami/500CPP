# Solution 9: Median of Two Sorted Arrays

## Approach Explanation
Binary search on the shorter array. Partition both arrays such that left elements ≤ right elements, and left partition has half of total elements.

## Step-by-Step Logic
1. Ensure binary search on the shorter array.
2. Binary search partition point in shorter array.
3. Compute corresponding partition in longer array.
4. Check if left max ≤ right min for valid partition.
5. Compute median from boundary elements.

## Complexity
- **Time Complexity:** O(log(min(m, n))).
- **Space Complexity:** O(1).

## Code
```python
def find_median(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i
        
        left1 = nums1[i-1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j-1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')
        
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2.0
            else:
                return max(left1, left2)
        elif left1 > right2:
            high = i - 1
        else:
            low = i + 1
```
