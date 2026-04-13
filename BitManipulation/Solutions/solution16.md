# Solution 16: Count Total Set Bits from 1 to N

## Approach Explanation
For each bit position, count how many numbers from 1 to n have that bit set. Use the pattern: groups of `2^(i+1)` have `2^i` consecutive set bits.

## Step-by-Step Logic
1. For each bit position `i` from 0 to 30.
2. Count full groups and partial group contributions.
3. Sum all contributions.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def count_set_bits(n):
    total = 0
    for i in range(32):
        # Total pairs of (2^(i+1))
        full_pairs = (n + 1) // (1 << (i + 1))
        total += full_pairs * (1 << i)
        
        # Remaining numbers
        remainder = (n + 1) % (1 << (i + 1))
        total += max(0, remainder - (1 << i))
    
    return total
```
