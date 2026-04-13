# Solution 14: Integer to Roman

## Approach Explanation
Map values to symbols. Greedily subtract the largest value and append its symbol.

## Step-by-Step Logic
1. Define value-symbol pairs in descending order.
2. For each pair, repeatedly subtract and append.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
def int_to_roman(num):
    val_sym = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
               (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
               (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for val, sym in val_sym:
        while num >= val:
            result += sym
            num -= val
    return result
```
