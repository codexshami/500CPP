# Solution 3: Z-Algorithm

## Approach Explanation
Maintain a Z-box [L,R] window. Use previous Z-values to speed up computation.

## Step-by-Step Logic
1. Initialize Z[0] = n, L = R = 0.
2. For each i, use Z-box to initialize Z[i].
3. Extend and update Z-box.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z
```
