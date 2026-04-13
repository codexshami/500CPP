# Solution 19: Optimal Merge Pattern

## Approach Explanation
Use a min-heap. Repeatedly extract the two smallest files, merge them (cost = sum of sizes), and insert the merged file back. The total cost is the sum of all merge costs.

## Step-by-Step Logic
1. Build a min-heap from file sizes.
2. While heap has more than one element: extract two minimums, add their sum as cost, push the merged size back.
3. Return total cost.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def optimal_merge(sizes):
    heapq.heapify(sizes)
    total_cost = 0
    
    while len(sizes) > 1:
        first = heapq.heappop(sizes)
        second = heapq.heappop(sizes)
        cost = first + second
        total_cost += cost
        heapq.heappush(sizes, cost)
    
    return total_cost
```
