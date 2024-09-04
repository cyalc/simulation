import curses

class UI:
    def __init__(self, stdscr, world):
        self.stdscr = stdscr
        self.world = world

    def draw(self):
        self.stdscr.clear()
        self._draw_world()
        self._draw_info_panel()
        self.stdscr.refresh()

    def _draw_world(self):
        height, width = self.stdscr.getmaxyx()
        for y in range(min(height - 1, self.world.height)):
            for x in range(min(width - 1, self.world.width)):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        try:
            self.stdscr.addch(y, x, self.world.grid[y][x])
        except curses.error:
            pass  # Ignore errors when drawing out of bounds

    def _draw_info_panel(self):
        height, _ = self.stdscr.getmaxyx()
        if height > self.world.height:
            info_start_y = min(self.world.height, height - 1)
            self._draw_info_text(info_start_y)

    def _draw_info_text(self, y):
        try:
            self.stdscr.addstr(y, 1, f"Humans: {len(self.world.humans)}")
        except curses.error:
            pass  # Ignore errors when drawing out of bounds