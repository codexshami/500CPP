# Solution 20: Monotonic Stack

## Approach Explanation
Maintain a stack of elements in monotonically decreasing order. When a larger element is found, it is the next greater for all smaller elements popped.

## Step-by-Step Logic
1. Traverse array from right to left.
2. Pop elements smaller than current from stack.
3. Stack top is the next greater element.
4. Push current element.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result
```
