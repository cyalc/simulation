import tcod

class UI:
    def __init__(self, console, world):
        self.console = console
        self.world = world

    def draw(self):
        self.console.clear()
        self._draw_world()
        self._draw_info_panel()

    def _draw_world(self):
        for y in range(min(self.console.height - 1, self.world.height)):
            for x in range(min(self.console.width - 1, self.world.width)):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        char = self.world.grid[y][x]
        self.console.print(x, y, char)

    def _draw_info_panel(self):
        if self.console.height > self.world.height:
            info_start_y = min(self.world.height, self.console.height - 1)
            self._draw_info_text(info_start_y)

    def _draw_info_text(self, y):
        self.console.print(1, y, f"Humans: {len(self.world.humans)}")