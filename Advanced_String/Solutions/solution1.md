# Solution 1: KMP Pattern Matching

## Approach Explanation
Build a failure function (partial match table) to skip unnecessary comparisons.

## Step-by-Step Logic
1. Build LPS (Longest Proper Prefix which is Suffix) array.
2. Use LPS to skip ahead on mismatches.
3. Collect all match positions.

## Complexity
- **Time Complexity:** O(N + M)
- **Space Complexity:** O(M)

## Code
```python
def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    lps = build_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return result
```
