# Solution 10: Kth Largest Element (QuickSelect)

## Approach Explanation
Use QuickSelect — partition the array and recurse only on the relevant side. Convert kth largest to (n-k)th smallest for easier indexing.

## Step-by-Step Logic
1. Convert to finding the (n-k)th index.
2. Partition array around a pivot.
3. If pivot index == target, return element.
4. Otherwise recurse on the appropriate side.

## Complexity
- **Time Complexity:** O(N) average, O(N²) worst case.
- **Space Complexity:** O(1).

## Code
```python
import random

def find_kth_largest(nums, k):
    target = len(nums) - k
    
    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        
        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        
        nums[store], nums[right] = nums[right], nums[store]
        
        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)
    
    return quickselect(0, len(nums) - 1)
```
