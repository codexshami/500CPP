# Solution 19: Distinct Subsequences

## Approach Explanation
DP where dp[i][j] = number of ways to form t[:j] from s[:i].

## Step-by-Step Logic
1. If chars match: dp[i][j] = dp[i-1][j-1] + dp[i-1][j].
2. If not: dp[i][j] = dp[i-1][j].
3. Return dp[m][n].

## Complexity
- **Time Complexity:** O(M*N)
- **Space Complexity:** O(M*N)

## Code
```python
def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[m][n]
```
