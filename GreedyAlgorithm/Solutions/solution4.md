# Solution 4: Job Sequencing with Deadlines

## Approach Explanation
Sort jobs by profit in descending order. For each job, find the latest available time slot before its deadline and assign the job to that slot. Use a boolean array to track occupied slots.

## Step-by-Step Logic
1. Sort jobs by profit in descending order.
2. Find the maximum deadline to determine the slot array size.
3. For each job, starting from its deadline, search backward for a free slot.
4. If a free slot is found, assign the job and add its profit.

## Complexity
- **Time Complexity:** O(N^2) in the worst case (can be improved to O(N log N) with Union-Find).
- **Space Complexity:** O(N) for the slot array.

## Code
```python
def job_sequencing(jobs):
    # Sort by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * (max_deadline + 1)
    
    count = 0
    total_profit = 0
    
    for job_id, deadline, profit in jobs:
        # Find a free slot from deadline backwards
        for slot in range(deadline, 0, -1):
            if not slots[slot]:
                slots[slot] = True
                count += 1
                total_profit += profit
                break
    
    return (count, total_profit)
```
