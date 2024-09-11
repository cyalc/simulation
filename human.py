import random

from need import Need
from trait import Trait

class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.traits = {trait: random.random() for trait in Trait}
        self.need_levels = {need: 0.0 for need in Need}  # Start with all needs unfulfilled
        self.id = random.randint(1000, 9999)  # Add this line

    def update(self, world):
        for need in Need:
            if self.need_levels[need] < 1.0:  # Need is not fully satisfied
                self.fulfill_need(need, world)
                break  # Focus on the lowest unfulfilled need in the hierarchy

    def fulfill_need(self, need, world):
        # Implement need fulfillment logic here
        # Increase the need level based on actions taken
        pass

    def get_properties(self):  # Add this method
        return {
            "ID": self.id,
            "Position": f"({self.x}, {self.y})",
            "Traits": {trait.name: f"{value:.2f}" for trait, value in self.traits.items()},
            "Needs": {need.name: f"{value:.2f}" for need, value in self.need_levels.items()}
        }
