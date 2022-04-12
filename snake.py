from random import randint
from colorama import Fore, init
from pytimedinput import timedInput


# settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
SPEED = 0.3
DIRECTIONS = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}

#ansi
CLS = "2J"
GOTO00 = "H"
CURSOR_ON = "?25h"
CURSOR_OFF = "?25l"


def ansi(*code: str):
    """ See: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 """
    for c in code:
        print(f"\033[{c}", end="")


def is_border(x, y):
    return ((x % FIELD_WIDTH) * (y % FIELD_HEIGHT)) == 0


def print_field():
    ansi(GOTO00)
    row = 0
    while row <= FIELD_HEIGHT:
        col = 0
        while col <= FIELD_WIDTH:
            cell = col, row
            if is_border(col, row):
                print(Fore.CYAN + '#', end='')
            elif cell in snake_body:
                print(Fore.GREEN + 'X', end='')
            elif cell == apple_pos:
                print(Fore.RED + 'a', end='')
            else:
                print(' ', end='')
            col += 1
        row += 1
        print()


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

init(autoreset=True)
ansi(CLS, CURSOR_OFF)
while True:
    # draw field
    print_field()

    # get input
    txt, _ = timedInput("   \r", SPEED)
    if txt and (txt in 'wasd'):
        direction = DIRECTIONS[txt]
    elif txt == 'q':
        break

    # update game
    apple_pos = update_snake(apple_pos)

    # check death
    if is_border(*snake_body[0]) or snake_body[0] in snake_body[1:]:
        break

ansi(CLS, CURSOR_ON)
