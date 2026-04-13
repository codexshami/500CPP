# Solution 15: Word Break

## Approach Explanation
DP where dp[i] = True if s[:i] can be segmented.

## Step-by-Step Logic
1. dp[0] = True (empty string).
2. For each i, check all j < i if dp[j] and s[j:i] in wordDict.
3. Return dp[n].

## Complexity
- **Time Complexity:** O(N^2 * M)
- **Space Complexity:** O(N)

## Code
```python
def word_break(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
```
