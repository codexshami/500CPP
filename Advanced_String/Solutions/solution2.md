# Solution 2: Rabin-Karp Algorithm

## Approach Explanation
Use rolling hash to compare pattern hash with text window hashes.

## Step-by-Step Logic
1. Compute hash of pattern.
2. Slide window over text, updating hash.
3. On hash match, verify characters.

## Complexity
- **Time Complexity:** O(N + M) average
- **Space Complexity:** O(1)

## Code
```python
def rabin_karp(text, pattern):
    d, q = 256, 101
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p_hash = t_hash = 0
    result = []
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0: t_hash += q
    return result
```
