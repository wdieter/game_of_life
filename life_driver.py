import os
import random
from model import Grid
import time
import click


@click.command()
@click.option('--width', default=10, help='width of grid')
@click.option('--height', default=10, help='height of grid')
@click.option('--cells', default=20, help='number of cells to set alive at random locations in the grid')
def main(width, height, cells):
    live_cells = [[random.randint(0, width - 1), random.randint(0, height - 1)] for _ in range(cells)]

    grid = Grid(width, height)
    grid.set_alive(live_cells)

    while not grid.stale:
        tmp = os.system('clear')
        grid.play()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
