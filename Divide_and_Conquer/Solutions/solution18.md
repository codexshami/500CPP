# Solution 18: Longest Common Prefix using Divide and Conquer

## Approach Explanation
Split the array of strings in half. Find the LCP of each half, then find the LCP of the two results.

## Step-by-Step Logic
1. Divide strings into left and right halves.
2. Recursively find LCP of each half.
3. Compare the two LCPs character by character.

## Complexity
- **Time Complexity:** O(S) where S is total characters across all strings.
- **Space Complexity:** O(M * log N) for recursion.

## Code
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    def lcp(left, right):
        if left == right:
            return strs[left]
        
        mid = (left + right) // 2
        lcp_left = lcp(left, mid)
        lcp_right = lcp(mid + 1, right)
        
        return common_prefix(lcp_left, lcp_right)
    
    def common_prefix(s1, s2):
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:min_len]
    
    return lcp(0, len(strs) - 1)
```
