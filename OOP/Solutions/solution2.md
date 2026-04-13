# Solution 2: Shape Hierarchy

## Approach Explanation
Use abstract base class with abc module. Each subclass implements area() and perimeter().

## Step-by-Step Logic
1. Define abstract Shape with @abstractmethod.
2. Circle uses pi*r^2 and 2*pi*r.
3. Rectangle uses l*w and 2*(l+w).

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perimeter(self): return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
    def perimeter(self): return 2 * (self.l + self.w)
```
