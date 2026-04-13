# Problem 19: Skyline Problem

## Problem Statement
Given a list of buildings represented as `[left, right, height]`, compute the skyline formed by these buildings.

## Input Format
- A list of lists `buildings` where each `[li, ri, hi]` represents a building.

## Output Format
- A list of key points `[x, height]` representing the skyline contour.

## Constraints
- 1 <= len(buildings) <= 10^4
- 0 <= left < right <= 2^31 - 1
- 1 <= height <= 2^31 - 1

## Example
**Input:** buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]  
**Output:** [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
