# Solution 8: Catalan Number

## Approach Explanation
Use DP: C(n) = Σ C(i)*C(n-1-i) for i=0..n-1.

## Step-by-Step Logic
1. Initialize dp[0] = dp[1] = 1.
2. For each n, compute sum of dp[i]*dp[n-1-i].
3. Return dp[n].

## Complexity
- **Time Complexity:** O(N²)
- **Space Complexity:** O(N)

## Code
```python
def catalan(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]
```
