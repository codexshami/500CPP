# Solution 16: Happy Number

## Approach Explanation
Use Floyd's cycle detection (fast/slow pointers) on the digit-square-sum sequence.

## Step-by-Step Logic
1. Compute digit square sum repeatedly.
2. If it reaches 1, return True.
3. If cycle detected without reaching 1, return False.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Code
```python
def is_happy(n):
    def digit_sum(num):
        total = 0
        while num:
            total += (num % 10) ** 2
            num //= 10
        return total
    
    slow = n
    fast = digit_sum(n)
    while fast != 1 and slow != fast:
        slow = digit_sum(slow)
        fast = digit_sum(digit_sum(fast))
    return fast == 1
```
