import curses
from world import World
from human import Human
from ui import UI

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.clear()

    # Create world and populate with humans
    world = World(width=50, height=20)
    world.populate(num_humans=10)

    # Create UI
    ui = UI(stdscr, world)

    # Main game loop
    while True:
        world.update()
        ui.draw()
        
        # Handle user input
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)