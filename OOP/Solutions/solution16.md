# Solution 16: Command Pattern

## Approach Explanation
Commands encapsulate actions. Invoker stores and executes commands.

## Step-by-Step Logic
1. Command interface with execute/undo.
2. Concrete commands implement actions.
3. Invoker stores command history.

## Complexity
- **Time Complexity:** O(1) per command
- **Space Complexity:** O(N)

## Code
```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): pass

class LightOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.on()

class Light:
    def on(self): print('Light is ON')
    def off(self): print('Light is OFF')

class RemoteControl:
    def __init__(self): self.commands = {}
    def set_command(self, slot, cmd): self.commands[slot] = cmd
    def press(self, slot): self.commands[slot].execute()
```
