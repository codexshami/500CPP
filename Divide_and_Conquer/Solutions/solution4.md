# Solution 4: Count Inversions

## Approach Explanation
Modify merge sort to count inversions during the merge step. When an element from the right half is placed before elements in the left half, those constitute inversions.

## Step-by-Step Logic
1. Split array and recursively count inversions in each half.
2. During merge, when `right[j] < left[i]`, add `(len(left) - i)` inversions.
3. Return total inversions.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    
    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
```
