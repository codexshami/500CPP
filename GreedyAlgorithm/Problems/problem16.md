# Problem 16: Task Scheduler

## Problem Statement
Given a list of tasks represented by characters and a non-negative integer `n` representing the cooldown period between two same tasks, find the minimum number of intervals the CPU will take to finish all tasks.

## Input Format
- A list of characters `tasks`.
- An integer `n` — cooldown interval.

## Output Format
- An integer representing the minimum number of intervals needed.

## Constraints
- 1 <= len(tasks) <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

## Example
**Input:** tasks = ['A','A','A','B','B','B'], n = 2  
**Output:** 8  
**Explanation:** A -> B -> idle -> A -> B -> idle -> A -> B
