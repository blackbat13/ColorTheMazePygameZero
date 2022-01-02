import pgzrun
import random

WIDTH = 2000
HEIGHT = 1300

size = 20

speed = 50

cells = []

def draw():
    count = 0
    while len(cells) > 0 and count < speed:
        pos, color = cells.pop(0)
        x, y = pos
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            continue

        if screen.surface.get_at((x, y)) != (255, 255, 255, 255):
            continue

        screen.surface.set_at((x, y), color)
        count += 1

        cells.append(((x + 1, y), color))
        cells.append(((x - 1, y), color))
        cells.append(((x, y + 1), color))
        cells.append(((x, y - 1), color))


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
    cells.append((pos, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))


def flood_fill(x, y):
    cells = [(x, y)]
    while len(cells) > 0:
        x, y = cells.pop()
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            continue

        if screen.surface.get_at((x, y)) != (255, 255, 255, 255):
            continue

        screen.surface.set_at((x, y), (255, 0, 0))

        cells.append((x + 1, y))
        cells.append((x - 1, y))
        cells.append((x, y + 1))
        cells.append((x, y - 1))


pgzrun.go()
