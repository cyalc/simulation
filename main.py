import tcod
from debugger import Debugger
from world import World
from ui import UI
import tcod.event

def main():
    # Initialize tcod
    screen_width = 192
    screen_height = 108
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    with tcod.context.new(
        width=1920,
        height=1080,
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Human Simulation",
        vsync=True,
    ) as context:
        console = tcod.console.Console(screen_width, screen_height, order="F")
        
        # Create UI first to get game dimensions
        ui = UI(console, None)
        game_width, game_height = ui.get_game_dimensions()

        # Create world with game dimensions
        world = World(width=game_width, height=game_height)
        world.populate(num_humans=10)

        # Set the world for UI
        ui.world = world

        debugger = Debugger(world)
        
        # Main game loop
        while True:
            world.update()
            ui.draw()
            context.present(console)

            for event in tcod.event.wait():
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.MouseButtonDown) and event.button == 1:  # Left click
                    mouse_event = context.convert_event(event)
                    x, y = mouse_event.position
                    clicked_human = world.get_human_at(x, y)
                    if clicked_human:
                        ui.select_human(clicked_human)
                elif isinstance(event, tcod.event.KeyDown):
                    if event.sym == tcod.event.KeySym.q:
                        raise SystemExit()
                    if event.sym == tcod.event.KeySym.d:
                        debugger.debug_print()

if __name__ == "__main__":
    main()