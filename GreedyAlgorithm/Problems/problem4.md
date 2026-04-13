# Problem 4: Job Sequencing with Deadlines

## Problem Statement
Given a set of `n` jobs where each job has a deadline and a profit, schedule jobs to maximize total profit. Each job takes one unit of time to complete and only one job can be scheduled at a time. A job earns its profit only if completed before its deadline.

## Input Format
- A list of tuples `jobs` where each tuple `(job_id, deadline, profit)`.

## Output Format
- A tuple `(count, max_profit)` — number of jobs scheduled and total profit earned.

## Constraints
- 1 <= n <= 10^5
- 1 <= deadline <= n
- 1 <= profit <= 10^5

## Example
**Input:** jobs = [('a',2,100), ('b',1,19), ('c',2,27), ('d',1,25), ('e',3,15)]  
**Output:** (3, 142)  
**Explanation:** Jobs 'a', 'c', 'e' can be scheduled for a profit of 100+27+15 = 142.
