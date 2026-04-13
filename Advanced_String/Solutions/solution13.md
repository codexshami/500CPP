# Solution 13: String Compression

## Approach Explanation
Walk through the string counting consecutive characters.

## Step-by-Step Logic
1. Track current char and count.
2. Append char + count to result.
3. Return shorter of original and compressed.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def compress(s):
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s
```
