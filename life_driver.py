import os
import random
from model import Grid
x = 100
y = 50

cell_count = 500

live_cells = [[random.randint(0,x), random.randint(0,y)] for _ in range(cell_count)]

grid = Grid(x+1, y+1)
grid.set_alive(live_cells)

while True:
    tmp = os.system('clear')
    grid.play()




