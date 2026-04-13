# Solution 17: Different Ways to Add Parentheses

## Approach Explanation
For each operator, split the expression into left and right parts. Recursively compute all results for both parts, then combine with the operator.

## Step-by-Step Logic
1. If expression is a number, return it as the only result.
2. For each operator, split into left and right subexpressions.
3. Recursively get all results for both parts.
4. Compute all combinations with the operator.

## Complexity
- **Time Complexity:** O(Catalan(N)) — exponential in number of operators.
- **Space Complexity:** O(Catalan(N)).

## Code
```python
def diff_ways_to_compute(expression):
    if expression.isdigit():
        return [int(expression)]
    
    results = []
    
    for i, char in enumerate(expression):
        if char in '+-*':
            left = diff_ways_to_compute(expression[:i])
            right = diff_ways_to_compute(expression[i+1:])
            
            for l in left:
                for r in right:
                    if char == '+':
                        results.append(l + r)
                    elif char == '-':
                        results.append(l - r)
                    elif char == '*':
                        results.append(l * r)
    
    return results
```
