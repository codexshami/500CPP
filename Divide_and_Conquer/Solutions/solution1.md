# Solution 1: Merge Sort

## Approach Explanation
Divide the array into two halves, recursively sort each half, then merge the two sorted halves.

## Step-by-Step Logic
1. If array length <= 1, return.
2. Find mid, split into left and right halves.
3. Recursively sort both halves.
4. Merge back by comparing elements from both halves.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
