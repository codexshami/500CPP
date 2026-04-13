# Solution 18: Composition vs Inheritance

## Approach Explanation
Car HAS-A Engine (composition) rather than IS-A Engine

## Step-by-Step Logic
1. Engine class with start/stop.
2. Car holds an Engine instance.
3. Car delegates to engine.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
class Engine:
    def __init__(self, engine_type): self.type = engine_type
    def start(self): return f'{self.type} engine started'
    def stop(self): return f'{self.type} engine stopped'

class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self): return self.engine.start()
    def stop(self): return self.engine.stop()
```
