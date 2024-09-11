from human import Human
import random

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.humans = []
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def populate(self, num_humans):
        for _ in range(num_humans):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            human = Human(x, y)
            self.humans.append(human)
            self.grid[y][x] = '@'

    def update(self):
        # Update world state and human actions
        for human in self.humans:
            human.update(self)

    def get_human_at(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            for human in self.humans:
                if human.x == x and human.y == y:
                    return human
        return None

    def move_human(self, human, new_x, new_y):
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.grid[human.y][human.x] = ' '
            human.x, human.y = new_x, new_y
            self.grid[new_y][new_x] = '@'