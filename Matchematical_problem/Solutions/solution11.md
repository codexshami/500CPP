# Solution 11: Check Perfect Number

## Approach Explanation
Find all divisors up to √n and check if their sum equals n.

## Step-by-Step Logic
1. Iterate from 1 to √n.
2. Add both divisor and n/divisor.
3. Check if sum equals n.

## Complexity
- **Time Complexity:** O(√N)
- **Space Complexity:** O(1)

## Code
```python
def is_perfect(n):
    if n <= 1:
        return False
    div_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
        i += 1
    return div_sum == n
```
