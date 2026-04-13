# Solution 1: Single Number

## Approach Explanation
XOR all elements together. Since `a XOR a = 0` and `a XOR 0 = a`, all paired elements cancel out, leaving only the single number.

## Step-by-Step Logic
1. Initialize `result = 0`.
2. XOR every element with `result`.
3. Return `result`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```
