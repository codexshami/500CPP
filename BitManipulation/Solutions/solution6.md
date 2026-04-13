# Solution 6: Missing Number

## Approach Explanation
XOR all numbers from 0 to n with all elements in the array. Paired values cancel out, leaving only the missing number.

## Step-by-Step Logic
1. Initialize `result = len(nums)` (to account for the index n).
2. XOR with each index and its corresponding value.
3. Return `result`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def missing_number(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```
