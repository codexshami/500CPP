# Problem 14: Minimum Number of Arrows to Burst Balloons

## Problem Statement
Given a list of balloons represented as intervals `[start, end]` on a number line, find the minimum number of arrows that must be shot vertically to burst all balloons. An arrow at position `x` bursts all balloons where `start <= x <= end`.

## Input Format
- A list of lists `points` where each `[start, end]` represents a balloon.

## Output Format
- An integer representing the minimum number of arrows needed.

## Constraints
- 1 <= len(points) <= 10^5
- -2^31 <= start <= end <= 2^31 - 1

## Example
**Input:** points = [[10,16],[2,8],[1,6],[7,12]]  
**Output:** 2
