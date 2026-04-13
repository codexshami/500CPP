# Problem 3: LFU Cache

## Problem Statement
Design a Least Frequently Used (LFU) Cache with O(1) get and put.

## Input Format
- Operations: get(key), put(key, value), capacity.

## Output Format
- Integer for get (-1 if not found).

## Constraints
- 0 <= capacity <= 10^4

## Example
**Input:** LFUCache(2), put(1,1), put(2,2), get(1)  
**Output:** 1
