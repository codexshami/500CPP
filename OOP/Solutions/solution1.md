# Solution 1: Bank Account Class

## Approach Explanation
Encapsulate balance as private, expose methods for deposits and withdrawals with validation.

## Step-by-Step Logic
1. Define __init__ with balance.
2. deposit adds to balance.
3. withdraw checks for sufficient funds.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(1)

## Code
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    def balance(self):
        return self._balance
```
