# Solution 18: Reorganize String

## Approach Explanation
Place the most frequent character first at even indices, then fill remaining characters. If any character's frequency exceeds `(len(s) + 1) // 2`, it's impossible.

## Step-by-Step Logic
1. Count character frequencies.
2. If max frequency > `(len(s) + 1) // 2`, return "".
3. Sort characters by frequency (descending).
4. Place characters at even indices first, then odd indices.
5. Return the rearranged string.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
from collections import Counter

def reorganize_string(s):
    freq = Counter(s)
    max_freq = max(freq.values())
    
    if max_freq > (len(s) + 1) // 2:
        return ""
    
    # Sort by frequency descending
    sorted_chars = sorted(freq.keys(), key=lambda c: -freq[c])
    
    result = [''] * len(s)
    idx = 0
    
    for char in sorted_chars:
        for _ in range(freq[char]):
            result[idx] = char
            idx += 2
            if idx >= len(s):
                idx = 1
    
    return ''.join(result)
```
