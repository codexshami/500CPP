# Solution 5: Parking Lot System

## Approach Explanation
Use classes for ParkingSpot, Vehicle with size matching.

## Step-by-Step Logic
1. ParkingLot manages spots.
2. Vehicles have sizes.
3. Match vehicle to appropriate spot.

## Complexity
- **Time Complexity:** O(N) to find spot
- **Space Complexity:** O(N)

## Code
```python
class Vehicle:
    def __init__(self, plate, size):
        self.plate = plate
        self.size = size

class ParkingSpot:
    def __init__(self, spot_id, size):
        self.id = spot_id
        self.size = size
        self.vehicle = None
    def park(self, vehicle):
        if not self.vehicle and vehicle.size <= self.size:
            self.vehicle = vehicle
            return True
        return False
    def leave(self):
        self.vehicle = None
```
