# Solution 9: Pascal's Triangle

## Approach Explanation
Each element is the sum of the two elements above it. Edge elements are 1.

## Step-by-Step Logic
1. Create rows iteratively.
2. Each row starts and ends with 1.
3. Inner elements = sum of two above.

## Complexity
- **Time Complexity:** O(N²)
- **Space Complexity:** O(N²)

## Code
```python
def generate_pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```
