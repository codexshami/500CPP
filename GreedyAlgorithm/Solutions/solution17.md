# Solution 17: Assign Cookies

## Approach Explanation
Sort both greed factors and cookie sizes. Use two pointers to greedily match the smallest possible cookie that satisfies each child.

## Step-by-Step Logic
1. Sort `g` and `s`.
2. Use pointer `i` for children and `j` for cookies.
3. If `s[j] >= g[i]`, the child is content: increment both pointers.
4. Otherwise, try the next (larger) cookie: increment `j`.
5. Return the count of content children.

## Complexity
- **Time Complexity:** O(N log N + M log M).
- **Space Complexity:** O(1).

## Code
```python
def find_content_children(g, s):
    g.sort()
    s.sort()
    
    child = 0
    cookie = 0
    
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    
    return child
```
