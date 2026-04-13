# Solution 12: Longest Repeating Substring

## Approach Explanation
Use binary search on length + rolling hash to check if a substring of that length repeats.

## Step-by-Step Logic
1. Binary search on the length.
2. For each length, use rolling hash to find duplicates.
3. Return the maximum length found.

## Complexity
- **Time Complexity:** O(N log N)
- **Space Complexity:** O(N)

## Code
```python
def longest_repeating(s):
    def check(length):
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub in seen: return True
            seen.add(sub)
        return False
    lo, hi, ans = 1, len(s)-1, 0
    while lo <= hi:
        mid = (lo+hi)//2
        if check(mid): ans = mid; lo = mid+1
        else: hi = mid-1
    return ans
```
