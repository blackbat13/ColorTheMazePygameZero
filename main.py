import pgzrun
import random


""" CONFIGURATION """

WIDTH = 2000
HEIGHT = 1300

TITLE = "Color The Maze Pygame Zero"

SIZE = 20

WALL_COLOR = (0, 0, 0, 0)

BG_COLOR = (255, 255, 255, 255)

""" VARIABLES """

speed = 50

max_source_id = -1

cells_list = []

source_id_counters_list = []

current_sources = 0

""" DRAW """


def draw():
    """ On draw handler 
    """
    count = 0
    while len(cells_list) > 0 and count < speed * current_sources:
        pos, color, s_id = cells_list.pop(0)
        x, y = pos
        if not inside_screen(pos) or screen.surface.get_at(pos) != BG_COLOR:
            decrease_source_count(s_id)
            continue

        screen.surface.set_at(pos, color)
        count += 1

        source_id_counters_list[s_id] += 4
        cells_list.append(((x + 1, y), color, s_id))
        cells_list.append(((x - 1, y), color, s_id))
        cells_list.append(((x, y + 1), color, s_id))
        cells_list.append(((x, y - 1), color, s_id))
        decrease_source_count(s_id)


def draw_maze():
    """Generates and draws new random maze on the screen
    """
    screen.fill(BG_COLOR)
    for x in range(0, WIDTH, SIZE):
        for y in range(0, HEIGHT, SIZE):
            if random.random() < 0.5:
                screen.draw.line((x, y), (x + SIZE, y + SIZE), WALL_COLOR)
            else:
                screen.draw.line((x, y + SIZE), (x + SIZE, y), WALL_COLOR)


""" UPDATE """


def update():
    """On update handler.
    """
    pass


""" EVENTS """


def on_key_down(key):
    """ Gives you a chance to control your maze generation
        according to the key pressed.

    Args:
        key: pressed key
    """
    global speed

    if key == keys.R:
        draw_maze()

    if key == keys.UP:
        speed += 5

    if key == keys.DOWN:
        speed -= 5
        speed = max(speed, 5)


def on_mouse_down(pos):
    """ Drops source at mouse position

    Args:
        pos (int, int): mouse position
    """
    cells_list.append((pos, random_color(), add_source()))


""" HELPERS """


def add_source():
    """Adds new source for the flood fill algorithm

    Returns:
        int: identifier of the new source
    """
    global max_source_id, current_sources

    source_id_counters_list.append(1)
    max_source_id += 1
    current_sources += 1

    return max_source_id


def decrease_source_count(s_id):
    """Decreases source counter for the given source

    Args:
        s_id (int): source identifier
    """
    global current_sources

    source_id_counters_list[s_id] -= 1
    if source_id_counters_list[s_id] == 0:
        current_sources -= 1


def random_color():
    """'Returns a random color for the drawing of the cells

    Returns:
        (int, int, int, int): r, g, b, a tuple with values from 0 to 255
    """
    return (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255), 255)


def inside_screen(pos):
    """Checks if given coordinate is inside the screen

    Args:
        pos (int, int): a tuple with x and y coordinates

    Returns:
        bool: True if inside the screen, False otherwise
    """
    x, y = pos
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


""" INITIALIZATION """

pgzrun.go()
