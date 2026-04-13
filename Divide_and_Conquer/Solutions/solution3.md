# Solution 3: Binary Search

## Approach Explanation
Repeatedly halve the search space by comparing the target with the middle element.

## Step-by-Step Logic
1. Set `low = 0`, `high = len(arr) - 1`.
2. While `low <= high`: compute `mid = (low + high) // 2`.
3. If `arr[mid] == target`, return `mid`.
4. If `arr[mid] < target`, search right half. Otherwise, search left half.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
```
