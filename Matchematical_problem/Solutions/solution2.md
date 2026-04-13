# Solution 2: Sieve of Eratosthenes

## Approach Explanation
Create a boolean array of size n+1. Mark multiples of each prime as composite.

## Step-by-Step Logic
1. Initialize all as prime.
2. For each number from 2 to √n, mark its multiples.
3. Collect remaining primes.

## Complexity
- **Time Complexity:** O(N log log N)
- **Space Complexity:** O(N)

## Code
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]
```
