# Solution 6: Strategy Pattern

## Approach Explanation
Define a PaymentStrategy interface and concrete implementations.

## Step-by-Step Logic
1. Abstract PaymentStrategy with pay method.
2. CreditCard, PayPal, Crypto implement pay.
3. Context class uses the strategy.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): pass

class CreditCard(PaymentStrategy):
    def pay(self, amount): return f'Paid {amount} via Credit Card'

class PayPal(PaymentStrategy):
    def pay(self, amount): return f'Paid {amount} via PayPal'

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute(self, amount):
        return self.strategy.pay(amount)
```
