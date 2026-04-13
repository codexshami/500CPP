# Solution 20: Excel Sheet Column Number

## Approach Explanation
Treat as base-26 number where A=1, B=2, ..., Z=26.

## Step-by-Step Logic
1. Initialize result = 0.
2. For each character: result = result * 26 + (ord(ch) - ord('A') + 1).
3. Return result.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
def title_to_number(columnTitle):
    result = 0
    for ch in columnTitle:
        result = result * 26 + (ord(ch) - ord('A') + 1)
    return result
```
