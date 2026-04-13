# Solution 2: Fractional Knapsack

## Approach Explanation
Calculate the value-to-weight ratio for each item. Sort items by this ratio in descending order. Greedily add items (or fractions) to the knapsack until it's full.

## Step-by-Step Logic
1. Compute value/weight ratio for each item.
2. Sort items by ratio in descending order.
3. For each item, if it fits entirely, add it. Otherwise, add the fraction that fits.
4. Return total value.

## Complexity
- **Time Complexity:** O(N log N) for sorting.
- **Space Complexity:** O(1) extra space.

## Code
```python
def fractional_knapsack(W, items):
    # Sort by value/weight ratio descending
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    
    for value, weight in items:
        if W >= weight:
            total_value += value
            W -= weight
        else:
            total_value += value * (W / weight)
            break
    
    return total_value
```
