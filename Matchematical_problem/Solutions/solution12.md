# Solution 12: Sum of Divisors

## Approach Explanation
Iterate to √n, adding both divisor and its complement.

## Step-by-Step Logic
1. For each i from 1 to √n, if n%i==0, add i and n//i.
2. Handle perfect square case.

## Complexity
- **Time Complexity:** O(√N)
- **Space Complexity:** O(1)

## Code
```python
def sum_of_divisors(n):
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total
```
