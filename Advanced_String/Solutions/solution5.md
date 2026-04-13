# Solution 5: Minimum Window Substring

## Approach Explanation
Use sliding window with two pointers. Expand right to include, contract left to minimize.

## Step-by-Step Logic
1. Count chars needed from t.
2. Expand right until all chars included.
3. Contract left to find minimum.
4. Track best window.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(K) where K is charset size

## Code
```python
from collections import Counter
def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = 0
    min_len = float('inf')
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if min_len == float('inf') else s[start:start+min_len]
```
