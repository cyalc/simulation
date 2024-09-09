import tcod
from debugger import Debugger
from world import World
from human import Human
from ui import UI

def main():
    # Initialize tcod
    screen_width = 80
    screen_height = 50
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Human Simulation",
        vsync=True,
    ) as context:
        console = tcod.Console(screen_width, screen_height, order="F")
        
        # Create world and populate with humans
        world = World(width=screen_width-2, height=screen_height-2)
        world.populate(num_humans=10)

        # Create UI
        ui = UI(console, world)
        debugger = Debugger(world)
        # Main game loop
        while True:
            world.update()
            ui.draw()
            
            context.present(console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()
                elif event.type == "KEYDOWN":
                    if event.sym == tcod.event.K_q:
                        raise SystemExit()
                    if event.sym == tcod.event.K_d:
                        debugger.debugPrint()

if __name__ == "__main__":
    main()