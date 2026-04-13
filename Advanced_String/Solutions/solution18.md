# Solution 18: Palindrome Partitioning

## Approach Explanation
Use backtracking. At each position, try all palindromic prefixes and recurse.

## Step-by-Step Logic
1. At each index, check all substrings starting there.
2. If palindrome, add to current partition and recurse.
3. When reaching end, add partition to results.

## Complexity
- **Time Complexity:** O(N * 2^N)
- **Space Complexity:** O(N)

## Code
```python
def partition(s):
    result = []
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                path.append(sub)
                backtrack(end, path)
                path.pop()
    backtrack(0, [])
    return result
```
