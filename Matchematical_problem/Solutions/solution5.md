# Solution 5: Power Modular Exponentiation

## Approach Explanation
Use binary exponentiation: square the base and halve the exponent at each step.

## Step-by-Step Logic
1. If exp is odd, multiply result by base.
2. Square base, halve exponent.
3. Apply mod at each step.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Code
```python
def power_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result
```
