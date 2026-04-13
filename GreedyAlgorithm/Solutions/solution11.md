# Solution 11: Gas Station

## Approach Explanation
If total gas >= total cost, a solution exists. Start from each station and track the running tank. If tank goes negative, reset the start to the next station. The greedy insight: if you can't reach station j from station i, no station between i and j can reach j either.

## Step-by-Step Logic
1. Track `total_tank` and `curr_tank`, and `start = 0`.
2. For each station `i`, add `gas[i] - cost[i]` to both tanks.
3. If `curr_tank < 0`, reset `start = i + 1` and `curr_tank = 0`.
4. If `total_tank >= 0`, return `start`. Otherwise, return -1.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def can_complete_circuit(gas, cost):
    total_tank = 0
    curr_tank = 0
    start = 0
    
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        curr_tank += diff
        
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
    
    return start if total_tank >= 0 else -1
```
