# Solution 16: Group Anagrams

## Approach Explanation
Sort each string to create a canonical key. Group strings with the same key.

## Step-by-Step Logic
1. For each string, sort it to get key.
2. Add to dictionary with key.
3. Return all groups.

## Complexity
- **Time Complexity:** O(N * K log K)
- **Space Complexity:** O(N * K)

## Code
```python
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```
