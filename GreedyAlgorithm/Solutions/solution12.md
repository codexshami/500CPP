# Solution 12: Candy Distribution

## Approach Explanation
Use two passes. First pass (left-to-right): ensure each child with a higher rating than the left neighbor gets more candies. Second pass (right-to-left): ensure each child with a higher rating than the right neighbor gets more candies. Take the maximum at each position.

## Step-by-Step Logic
1. Initialize all candies to 1.
2. Left-to-right: if `ratings[i] > ratings[i-1]`, set `candies[i] = candies[i-1] + 1`.
3. Right-to-left: if `ratings[i] > ratings[i+1]`, set `candies[i] = max(candies[i], candies[i+1] + 1)`.
4. Return sum of candies.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    
    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)
```
