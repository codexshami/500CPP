# Problem 13: Interval Scheduling — Maximum Non-Overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals you can select.

## Input Format
- A list of tuples `intervals` where each tuple `(start, end)` represents an interval.

## Output Format
- An integer representing the maximum number of non-overlapping intervals.

## Constraints
- 1 <= len(intervals) <= 10^5
- -10^4 <= start < end <= 10^4

## Example
**Input:** intervals = [(1,3), (2,4), (3,6), (5,7), (6,8)]  
**Output:** 3  
**Explanation:** Select (1,3), (3,6), (6,8) — they don't overlap.
