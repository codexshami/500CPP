# Solution 11: Employee Management

## Approach Explanation
Use inheritance: Employee base, Manager extends with reports.

## Step-by-Step Logic
1. Employee has name, salary.
2. Manager has list of reports.
3. Department aggregates employees.

## Complexity
- **Time Complexity:** O(N) for total salary
- **Space Complexity:** O(N)

## Code
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.reports = []
    def add_report(self, emp): self.reports.append(emp)

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add(self, emp): self.employees.append(emp)
    def total_salary(self): return sum(e.salary for e in self.employees)
```
