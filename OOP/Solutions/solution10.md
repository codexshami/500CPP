# Solution 10: Singleton Pattern

## Approach Explanation
Use __new__ to control instance creation, returning existing instance if one exists.

## Step-by-Step Logic
1. Override __new__.
2. Check if instance exists.
3. If not, create and store it.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
