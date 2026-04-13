# Solution 14: Decode String

## Approach Explanation
Use a stack to handle nested encodings. Push counts and strings on encountering '['.

## Step-by-Step Logic
1. Use stack for nested brackets.
2. On '[': push current string and count.
3. On ']': pop and multiply.
4. Build result.

## Complexity
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Code
```python
def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0
    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif ch == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += ch
    return curr_str
```
