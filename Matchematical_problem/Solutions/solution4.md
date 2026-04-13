# Solution 4: Fibonacci Number

## Approach Explanation
Use iterative approach with two variables to avoid exponential recursion.

## Step-by-Step Logic
1. Initialize a=0, b=1.
2. Iterate n times, updating a and b.
3. Return a.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Code
```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```
