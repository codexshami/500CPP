# Solution 10: Shortest Palindrome

## Approach Explanation
Find the longest palindromic prefix, then prepend the reverse of the remaining suffix.

## Step-by-Step Logic
1. Reverse the string.
2. Find longest palindromic prefix using KMP.
3. Prepend reverse of suffix.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def shortest_palindrome(s):
    rev = s[::-1]
    combined = s + '#' + rev
    lps = [0] * len(combined)
    for i in range(1, len(combined)):
        j = lps[i-1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j-1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j
    return rev[:len(s) - lps[-1]] + s
```
