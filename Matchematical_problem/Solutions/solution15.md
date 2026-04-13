# Solution 15: Roman to Integer

## Approach Explanation
Process right to left. If current value < next value, subtract it; otherwise add it.

## Step-by-Step Logic
1. Map symbols to values.
2. Iterate right to left, comparing with previous.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result
```
