# Solution 6: Minimum Number of Coins

## Approach Explanation
Use a greedy approach with the largest denomination first. Since the Indian denomination system is canonical, the greedy approach yields the optimal solution. Repeatedly subtract the largest coin that fits.

## Step-by-Step Logic
1. Define denominations in descending order.
2. For each denomination, use as many as possible.
3. Append each coin used to the result list.

## Complexity
- **Time Complexity:** O(V) in the worst case.
- **Space Complexity:** O(V) for the result list.

## Code
```python
def min_coins(V):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []
    
    for coin in denominations:
        while V >= coin:
            V -= coin
            result.append(coin)
    
    return result
```
