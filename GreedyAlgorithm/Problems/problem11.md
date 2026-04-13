# Problem 11: Gas Station

## Problem Statement
There are `n` gas stations along a circular route. You are given two arrays `gas` and `cost` where `gas[i]` is the amount of gas at station `i` and `cost[i]` is the cost to travel from station `i` to station `i+1`. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

## Input Format
- A list of integers `gas`.
- A list of integers `cost`.

## Output Format
- An integer representing the starting station index, or -1 if impossible.

## Constraints
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4

## Example
**Input:** gas = [1,2,3,4,5], cost = [3,4,5,1,2]  
**Output:** 3
