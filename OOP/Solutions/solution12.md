# Solution 12: Decorator Pattern

## Approach Explanation
Wrap base component with decorator classes that add behavior.

## Step-by-Step Logic
1. Base Coffee class.
2. MilkDecorator wraps and adds cost.
3. Each decorator extends description and cost.

## Complexity
- **Time Complexity:** O(D) where D is decorators
- **Space Complexity:** O(D)

## Code
```python
class Coffee:
    def cost(self): return 2.0
    def description(self): return 'Coffee'

class MilkDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 0.5
    def description(self): return self._coffee.description() + ', Milk'

class SugarDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 0.25
    def description(self): return self._coffee.description() + ', Sugar'
```
