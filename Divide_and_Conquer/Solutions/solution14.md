# Solution 14: Count of Smaller Numbers After Self

## Approach Explanation
Use a modified merge sort that tracks original indices. During merging, count how many elements from the right half are placed before each left-half element.

## Step-by-Step Logic
1. Pair each element with its original index.
2. During merge sort, when placing a right element before left elements, increment counts for those left elements.
3. Return the counts array.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def count_smaller(nums):
    counts = [0] * len(nums)
    indices = list(range(len(nums)))
    
    def merge_sort(indices):
        if len(indices) <= 1:
            return indices
        mid = len(indices) // 2
        left = merge_sort(indices[:mid])
        right = merge_sort(indices[mid:])
        
        merged = []
        right_count = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if nums[right[j]] < nums[left[i]]:
                right_count += 1
                merged.append(right[j])
                j += 1
            else:
                counts[left[i]] += right_count
                merged.append(left[i])
                i += 1
        
        while i < len(left):
            counts[left[i]] += right_count
            merged.append(left[i])
            i += 1
        
        merged.extend(right[j:])
        return merged
    
    merge_sort(indices)
    return counts
```
