# Problem 2: Fractional Knapsack

## Problem Statement
Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value. You are allowed to break items (take fractions).

## Input Format
- An integer `W` — the capacity of the knapsack.
- A list of tuples `items` where each tuple `(value, weight)` represents an item.

## Output Format
- A float representing the maximum value achievable.

## Constraints
- 1 <= n <= 10^5
- 1 <= W <= 10^9
- 1 <= value, weight <= 10^6

## Example
**Input:** W = 50, items = [(60,10), (100,20), (120,30)]  
**Output:** 240.0  
**Explanation:** Take full items of weight 10 and 20, and 2/3 of item with weight 30.
