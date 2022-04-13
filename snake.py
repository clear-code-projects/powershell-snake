import colorama
from random import randint
from pytimedinput import timedInput


# settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
SPEED = 0.3
DIRECTIONS = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}


def p(*args, end=""):
    print(*args, end=end)


def is_border(x, y):
    return ((x % FIELD_WIDTH) * (y % FIELD_HEIGHT)) == 0


def print_field():
    p(colorama.Cursor.POS())
    p(f"\n  SCORE: {colorama.Fore.RED}{len(snake_body) - 3}", end="\n  ")
    row = 0
    while row <= FIELD_HEIGHT:
        col = 0
        while col <= FIELD_WIDTH:
            cell = col, row
            if is_border(col, row):
                p(colorama.Fore.CYAN + '▓')
            elif cell in snake_body:
                p(colorama.Fore.GREEN + '░')
            elif cell == apple_pos:
                p(colorama.Fore.RED + 'a')
            else:
                p(' ')
            col += 1
        row += 1
        p('\n  ')


def place_apple():
    while True:
        col = randint(1, FIELD_WIDTH - 2)
        row = randint(1, FIELD_HEIGHT - 2)
        if (col, row) not in snake_body:
            return col, row


def update_snake(apple_xy):
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if apple_xy != new_head:
        snake_body.pop(-1)
    else:
        apple_xy = place_apple()
    return apple_xy


# init snek
snake_body = [(5 - x, FIELD_HEIGHT // 2) for x in range(3)]
direction = DIRECTIONS['d']
apple_pos = place_apple()

colorama.init(autoreset=True)
p(colorama.ansi.clear_screen())
while True:
    # draw field
    print_field()

    # get input
    txt, _ = timedInput("   \r", SPEED)
    if len(txt) and (txt[0] in 'wasd'):
        direction = DIRECTIONS[txt[0]]
    elif txt == 'q':
        break

    # update game
    apple_pos = update_snake(apple_pos)

    # check death
    if is_border(*snake_body[0]) or snake_body[0] in snake_body[1:]:
        break

p(colorama.ansi.clear_screen())
