# Problem 5: Minimum Number of Platforms

## Problem Statement
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required at the station so that no train has to wait.

## Input Format
- A list `arrivals` of arrival times.
- A list `departures` of departure times.

## Output Format
- An integer representing the minimum number of platforms needed.

## Constraints
- 1 <= n <= 10^5
- Arrival and departure times are in 24-hour format (e.g., 900 means 9:00).

## Example
**Input:** arrivals = [900, 940, 950, 1100, 1500, 1800], departures = [910, 1200, 1120, 1130, 1900, 2000]  
**Output:** 3
