import pgzrun
import random

WIDTH = 2000
HEIGHT = 1300

size = 20

speed = 50

max_source_id = -1

cells = []

source_id_counter = []

current_sources = 0


def draw():
    count = 0
    while len(cells) > 0 and count < speed * current_sources:
        pos, color, s_id = cells.pop(0)
        x, y = pos
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            decrease_source_count(s_id)
            continue

        if screen.surface.get_at((x, y)) != (255, 255, 255, 255):
            decrease_source_count(s_id)
            continue

        screen.surface.set_at((x, y), color)
        count += 1

        source_id_counter[s_id] += 4
        cells.append(((x + 1, y), color, s_id))
        cells.append(((x - 1, y), color, s_id))
        cells.append(((x, y + 1), color, s_id))
        cells.append(((x, y - 1), color, s_id))
        decrease_source_count(s_id)


def update():
    pass


def on_key_down(key):
    global speed

    if key == keys.R:
        draw_maze()

    if key == keys.UP:
        speed += 5

    if key == keys.DOWN:
        speed -= 5
        speed = max(speed, 5)


def draw_maze():
    screen.fill("white")
    for x in range(0, WIDTH, size):
        for y in range(0, HEIGHT, size):
            if random.random() < 0.5:
                screen.draw.line((x, y), (x + size, y + size), (0, 0, 0))
            else:
                screen.draw.line((x, y + size), (x + size, y), (0, 0, 0))


def on_mouse_down(pos):
    cells.append((pos, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), add_source()))


def add_source():
    global max_source_id, current_sources
    source_id_counter.append(1)
    max_source_id += 1
    current_sources += 1
    return max_source_id


def decrease_source_count(s_id):
    global current_sources
    source_id_counter[s_id] -= 1
    if source_id_counter[s_id] == 0:
        current_sources -= 1


pgzrun.go()
