# Solution 2: Quick Sort

## Approach Explanation
Choose a pivot, partition the array so elements less than pivot go left and greater go right, then recursively sort each partition.

## Step-by-Step Logic
1. Choose last element as pivot.
2. Partition: move elements < pivot to the left side.
3. Place pivot at its correct position.
4. Recursively sort left and right partitions.

## Complexity
- **Time Complexity:** O(N log N) average, O(N²) worst case.
- **Space Complexity:** O(log N) for recursion stack.

## Code
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
