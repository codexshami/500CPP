# Solution 11: Count Palindromic Substrings

## Approach Explanation
Expand around each center and count palindromes.

## Step-by-Step Logic
1. For each center (single and between chars), expand.
2. Count each valid expansion.

## Complexity
- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1)

## Code
```python
def count_palindromes(s):
    count = 0
    for i in range(len(s)):
        for l, r in [(i,i), (i,i+1)]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1; r += 1
    return count
```
