# Solution 8: Regex Matching

## Approach Explanation
Use DP where dp[i][j] = whether s[:i] matches p[:j].

## Step-by-Step Logic
1. Handle '.' as any char match.
2. Handle '*' as zero or more of preceding.
3. Build DP table.

## Complexity
- **Time Complexity:** O(M*N)
- **Space Complexity:** O(M*N)

## Code
```python
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[m][n]
```
