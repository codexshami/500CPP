# Solution 14: Suffix Array

## Approach Explanation
Build suffix array by sorting all suffixes. Use the sorted indices.

## Step-by-Step Logic
1. Generate all suffixes with their starting indices.
2. Sort them lexicographically.
3. Return the indices.

## Complexity
- **Time Complexity:** O(N log^2 N) or O(N log N)
- **Space Complexity:** O(N)

## Code
```python
def build_suffix_array(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]
```
