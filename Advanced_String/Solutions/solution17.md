# Solution 17: Longest Substring Without Repeating

## Approach Explanation
Use sliding window with a set to track characters in the window.

## Step-by-Step Logic
1. Expand right pointer, add chars.
2. If duplicate, shrink from left.
3. Track maximum window size.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(K) where K is charset

## Code
```python
def length_of_longest(s):
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```
