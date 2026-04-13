# Problem 1: Activity Selection

## Problem Statement
Given `n` activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

## Input Format
- An integer `n` — the number of activities.
- A list of tuples `activities` where each tuple `(start, finish)` represents the start and finish time of an activity.

## Output Format
- An integer representing the maximum number of activities that can be selected.

## Constraints
- 1 <= n <= 10^5
- 0 <= start < finish <= 10^9

## Example
**Input:** activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]  
**Output:** 4  
**Explanation:** Selected activities are (1,4), (5,7), (8,11), (12,16).
