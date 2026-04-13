# Problem 15: Merge Intervals

## Problem Statement
Given an array of intervals where `intervals[i] = [start, end]`, merge all overlapping intervals and return a list of non-overlapping intervals that cover all the input intervals.

## Input Format
- A list of lists `intervals`.

## Output Format
- A list of merged intervals.

## Constraints
- 1 <= len(intervals) <= 10^4
- intervals[i].length == 2
- 0 <= start <= end <= 10^4

## Example
**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]  
**Output:** [[1,6],[8,10],[15,18]]
