# Solution 4: Observer Pattern

## Approach Explanation
Subject maintains a list of observers and notifies them on state changes.

## Step-by-Step Logic
1. Subject has list of observers.
2. subscribe/unsubscribe manage the list.
3. notify calls update on all observers.

## Complexity
- **Time Complexity:** O(N) for notify
- **Space Complexity:** O(N)

## Code
```python
class Subject:
    def __init__(self):
        self._observers = []
    def subscribe(self, observer):
        self._observers.append(observer)
    def unsubscribe(self, observer):
        self._observers.remove(observer)
    def notify(self, event):
        for obs in self._observers:
            obs.update(event)

class Observer:
    def update(self, event):
        print(f'Received: {event}')
```
