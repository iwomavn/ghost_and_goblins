from actor import Actor, Arena, Point
from actors.arthur import Arthur
from actors.zombie import Zombie
from actors.gravestone import Gravestone
from actors.platform import Platform
from random import randint

BG_WIDTH, BG_HEIGHT = 3588, 250

def tick():
    global x_view, y_view
    g2d.clear_canvas()
    g2d.draw_image("./imgs/background.png", (0, 0), (x_view, y_view), (w_view, h_view))

    keys = arena.current_keys()
    if "up" in keys and y_view > 0:
        y_view = max(0, y_view - 5)
    elif "down" in keys and y_view < BG_HEIGHT - h_view:
        y_view = min(BG_HEIGHT - h_view, y_view + 5)
    if "left" in keys and x_view > 0:
        x_view = max(0, x_view - 5)
    elif "right" in keys and x_view < BG_WIDTH - w_view:
        x_view = min(BG_WIDTH - w_view, x_view + 5)

    for a in arena.actors():
        if isinstance(a, Arthur):
            ax, ay = a.pos()

            # Spawn a zombie only if arthur is alive
            if randint(0, 500) == 5:
                direction = randint(0, 10) % 2
                diff = randint(50, 200)
                zx = ax + diff * (1 if direction == 0 else -1)
                arena.spawn(Zombie((max(0, zx), 170), direction))

            if a.sprite != None:
                g2d.draw_image(
                    "./imgs/sprites.png",
                    (ax - x_view, ay - y_view),
                    a.sprite(),
                    a.size(),
                )

            margin = 50
            if ax - x_view < margin:
                x_view = max(0, ax - margin)
            elif ax - x_view > w_view - margin:
                x_view = min(BG_WIDTH - w_view, ax - (w_view - margin))
        else:
            if a.sprite() is not None:
                g2d.draw_image(
                    "./imgs/sprites.png",
                    (a.pos()[0] - x_view, a.pos()[1] - y_view),
                    a.sprite(),
                    a.size(),
                )
    arena.tick(g2d.current_keys())

x_view, y_view = 0, 0
w_view, h_view = 400, 220

def main():
    global g2d, arena
    import g2d
    arena = Arena((w_view, h_view), (BG_WIDTH, BG_HEIGHT))
    arena.spawn(Arthur((0, 170)))
    arena.spawn(Gravestone((50, 185), (15, 15)))
    arena.spawn(Gravestone((242, 185), (15, 15)))
    arena.spawn(Gravestone((530, 185), (15, 15)))
    arena.spawn(Gravestone((754, 185), (15, 15)))
    arena.spawn(Gravestone((962, 185), (15, 15)))
    arena.spawn(Gravestone((1106, 185), (15, 15)))
    # mancano altre tombe che aggiungerò piu avanti + tagliero meglio gli sprites di arturo in modo che non li hitti prima hai capito dai ma mi son rotta...

    g2d.init_canvas(arena.view_size(), 2)
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
