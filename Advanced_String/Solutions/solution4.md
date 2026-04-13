# Solution 4: Longest Palindromic Substring

## Approach Explanation
Expand around each center (both single character and between characters).

## Step-by-Step Logic
1. For each possible center, expand outward.
2. Track the longest palindrome found.
3. Return the longest.

## Complexity
- **Time Complexity:** O(N^2) or O(N) with Manacher's
- **Space Complexity:** O(1)

## Code
```python
def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    result = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        result = max(result, odd, even, key=len)
    return result
```
