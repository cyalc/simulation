import tcod

class UI:
    def __init__(self, console, world):
        self.console = console
        self.world = world
        self.selected_human = None
        self.panel_width = 40
        self.info_panel_height = 1
        self.game_width = self.console.width - self.panel_width - 1
        self.game_height = self.console.height - self.info_panel_height

    def draw(self):
        self.console.clear()
        self._draw_world()
        self._draw_info_panel()
        self._draw_right_panel()

    def _draw_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        char = self.world.grid[y][x]
        self.console.print(x, y, char)

    def _draw_info_panel(self):
        info_start_y = self.game_height
        self._draw_info_text(info_start_y)

    def _draw_info_text(self, y):
        self.console.print(1, y, f"Humans: {len(self.world.humans)}")

    def _draw_right_panel(self):
        panel_start_x = self.game_width + 1
        
        # Draw panel border
        for y in range(self.console.height):
            self.console.print(panel_start_x - 1, y, "│")

        if self.selected_human:
            self._draw_human_properties(panel_start_x)

    def _draw_human_properties(self, x):
        if not self.selected_human:
            return

        properties = self.selected_human.get_properties()
        y = 1
        for key, value in properties.items():
            if isinstance(value, dict):
                self.console.print(x, y, f"{key}:")
                y += 1
                for subkey, subvalue in value.items():
                    self.console.print(x + 2, y, f"{subkey}: {subvalue}")
                    y += 1
            else:
                self.console.print(x, y, f"{key}: {value}")
                y += 1

    def select_human(self, human):
        self.selected_human = human

    def get_game_dimensions(self):
        return self.game_width, self.game_height