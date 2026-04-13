# Solution 13: Majority Element

## Approach Explanation
Divide array in half. The majority element of the whole array must be the majority in at least one half. Recursively find majority of each half, then count to determine the overall majority.

## Step-by-Step Logic
1. Base case: single element is the majority.
2. Recursively find majority of left and right halves.
3. If they agree, return that element.
4. Otherwise, count occurrences of each candidate in the full range.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(log N).

## Code
```python
def majority_element(nums):
    def helper(lo, hi):
        if lo == hi:
            return nums[lo]
        
        mid = (lo + hi) // 2
        left_maj = helper(lo, mid)
        right_maj = helper(mid + 1, hi)
        
        if left_maj == right_maj:
            return left_maj
        
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left_maj)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right_maj)
        
        return left_maj if left_count > right_count else right_maj
    
    return helper(0, len(nums) - 1)
```
