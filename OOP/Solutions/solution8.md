# Solution 8: Factory Pattern

## Approach Explanation
A factory method creates objects based on a type parameter.

## Step-by-Step Logic
1. Define Vehicle base class.
2. Car, Truck, Motorcycle subclasses.
3. Factory method returns correct type.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
class Vehicle:
    def describe(self): pass

class Car(Vehicle):
    def describe(self): return 'Car'

class Truck(Vehicle):
    def describe(self): return 'Truck'

def vehicle_factory(v_type):
    types = {'car': Car, 'truck': Truck}
    cls = types.get(v_type.lower())
    if cls: return cls()
    raise ValueError(f'Unknown type: {v_type}')
```
