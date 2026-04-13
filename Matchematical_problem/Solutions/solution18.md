# Solution 18: Nth Ugly Number

## Approach Explanation
Use three pointers for multiples of 2, 3, and 5. Always pick the minimum.

## Step-by-Step Logic
1. Maintain dp array and three pointers i2, i3, i5.
2. Next ugly = min(dp[i2]*2, dp[i3]*3, dp[i5]*5).
3. Advance the corresponding pointer(s).

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def nth_ugly(n):
    dp = [0] * n
    dp[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        next2, next3, next5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
        dp[i] = min(next2, next3, next5)
        if dp[i] == next2: i2 += 1
        if dp[i] == next3: i3 += 1
        if dp[i] == next5: i5 += 1
    return dp[n-1]
```
