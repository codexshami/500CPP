# Solution 20: Maximum XOR of Two Numbers in an Array

## Approach Explanation
Build a bitwise trie of all numbers. For each number, traverse the trie choosing the opposite bit at each level to maximize XOR.

## Step-by-Step Logic
1. Insert all numbers into a binary trie (from MSB to LSB).
2. For each number, traverse the trie greedily choosing the opposite bit.
3. Track the maximum XOR found.

## Complexity
- **Time Complexity:** O(N * 31) = O(N).
- **Space Complexity:** O(N * 31) for the trie.

## Code
```python
def find_maximum_xor(nums):
    max_xor = 0
    mask = 0
    
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = set()
        
        for num in nums:
            prefixes.add(num & mask)
        
        candidate = max_xor | (1 << i)
        
        for prefix in prefixes:
            if (candidate ^ prefix) in prefixes:
                max_xor = candidate
                break
    
    return max_xor
```
