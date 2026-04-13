# Solution 20: Text Justification

## Approach Explanation
Greedily pack words into lines. Distribute extra spaces evenly between words.

## Step-by-Step Logic
1. Pack words into lines greedily.
2. Distribute extra spaces left-to-right.
3. Left-justify last line.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def full_justify(words, maxWidth):
    result, line, line_len = [], [], 0
    for word in words:
        if line_len + len(word) + len(line) > maxWidth:
            for i in range(maxWidth - line_len):
                line[i % max(len(line)-1, 1)] += ' '
            result.append(''.join(line))
            line, line_len = [], 0
        line.append(word)
        line_len += len(word)
    result.append(' '.join(line).ljust(maxWidth))
    return result
```
