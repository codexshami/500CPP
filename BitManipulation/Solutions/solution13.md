# Solution 13: Swap Two Numbers Without Temp Variable

## Approach Explanation
Use XOR: `a ^= b`, `b ^= a`, `a ^= b`. This swaps the values without extra storage.

## Step-by-Step Logic
1. `a = a ^ b` → a now holds the XOR of both.
2. `b = a ^ b` → b gets the original value of a.
3. `a = a ^ b` → a gets the original value of b.

## Complexity
- **Time Complexity:** O(1).
- **Space Complexity:** O(1).

## Code
```python
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
```
