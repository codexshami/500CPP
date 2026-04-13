# Solution 20: Social Media Post System

## Approach Explanation
Post has author, content, likes set, and comments list.

## Step-by-Step Logic
1. User creates Posts.
2. Post supports like/unlike.
3. Comment linked to Post.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(N)

## Code
```python
class User:
    def __init__(self, name): self.name = name

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.likes = set()
        self.comments = []
    def like(self, user): self.likes.add(user.name)
    def comment(self, user, text): self.comments.append((user.name, text))
    def like_count(self): return len(self.likes)
```
