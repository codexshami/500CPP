# Problem 17: Assign Cookies

## Problem Statement
You are an awesome parent and want to give cookies to your children. Each child `i` has a greed factor `g[i]` and each cookie `j` has a size `s[j]`. A child `i` is content if `s[j] >= g[i]`. Maximize the number of content children.

## Input Format
- A list of integers `g` — greed factors of children.
- A list of integers `s` — sizes of cookies.

## Output Format
- An integer — the maximum number of content children.

## Constraints
- 1 <= len(g) <= 3 * 10^4
- 1 <= len(s) <= 3 * 10^4
- 1 <= g[i], s[j] <= 2^31 - 1

## Example
**Input:** g = [1,2,3], s = [1,1]  
**Output:** 1
