# Solution 9: Wildcard Matching

## Approach Explanation
DP where '?' matches any single char and '*' matches any sequence.

## Step-by-Step Logic
1. Build DP table.
2. '?' matches any single character.
3. '*' matches any sequence (including empty).

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
            dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '?' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[m][n]
```
