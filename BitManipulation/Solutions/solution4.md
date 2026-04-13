# Solution 4: Counting Bits

## Approach Explanation
Use the relation: `bits[i] = bits[i >> 1] + (i & 1)`. The number of set bits in `i` equals the set bits in `i // 2` plus 1 if `i` is odd.

## Step-by-Step Logic
1. Create array `ans` of size `n + 1`, initialized to 0.
2. For each `i` from 1 to n: `ans[i] = ans[i >> 1] + (i & 1)`.
3. Return `ans`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def count_bits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
```
