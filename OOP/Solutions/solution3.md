# Solution 3: Library Management System

## Approach Explanation
Use classes with relationships: Library has Books and Members.

## Step-by-Step Logic
1. Book tracks title, author, available status.
2. Member has borrowed books list.
3. Library manages checkout/return.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(N)

## Code
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def borrow(self, member, book):
        if book.available and len(member.borrowed) < 5:
            book.available = False
            member.borrowed.append(book)
            return True
        return False
```
