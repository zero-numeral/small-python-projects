import copy
import random
import time


class Cell:
    DEAD = ' '
    ALIVE = '0'


def generate_field(w, h):
    return [[random.choice([Cell.DEAD, Cell.ALIVE]) for _ in range(w)] for _ in range(h)]


# Посчитать живых соседей у клетки
def cells_alive(field, i, j):
    num = 0
    rows = len(field)
    cols = len(field[0])
    for offset in range(9):
        if offset != 4:  # Пропускаем центровую клетку
            idx_r = i - 1 + offset % 3
            idx_c = j - 1 + offset // 3

            if 0 <= idx_r < rows and 0 <= idx_c < cols:
                num += field[idx_r][idx_c] == Cell.ALIVE
    return num


def process_field(field):
    rows = len(field)
    cols = len(field[0])

    new_field = copy.deepcopy(field)

    for i in range(rows):
        for j in range(cols):
            still_alive = cells_alive(field, i, j)
            if field[i][j] == Cell.ALIVE and 2 <= still_alive <= 3:
                new_field[i][j] = Cell.ALIVE
            elif field[i][j] == Cell.DEAD and still_alive == 3:
                new_field[i][j] = Cell.ALIVE
            else:
                new_field[i][j] = Cell.DEAD

    return new_field


def is_a_least_one_alive(field):
    rows = len(field)
    cols = len(field[0])
    return any([any([field[i][j] == Cell.ALIVE for j in range(cols)]) for i in range(rows)])


def main():
    WIDTH = 20
    HEIGHT = 10

    main_field = generate_field(WIDTH, HEIGHT)
    while is_a_least_one_alive(main_field):
        print(*["".join(row) for row in main_field], sep='\n', end='\n\n\n')
        main_field = process_field(main_field)
        time.sleep(1)


if __name__ == "__main__":
    main()
