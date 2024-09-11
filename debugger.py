class Debugger:
    def __init__(self, world):
        self.world = world

    def debug_print(self):
        print("Humans in the world:")
        for i, human in enumerate(self.world.humans, 1):
            print(f"  Human {i}:")
            print(f"    Position: ({human.x}, {human.y})")
            print("    Traits:")
            for trait, value in human.traits.items():
                print(f"      {trait.name}: {value:.2f}")
            print("    Needs:")
            for need, value in human.need_levels.items():
                print(f"      {need.name}: {value:.2f}")
            print()  # Add a blank line between humans