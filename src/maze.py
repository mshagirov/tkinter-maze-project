import time
import random

from cell import Cell
from window import Window

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows:int,
                 num_cols:int,
                 cell_size_x,
                 cell_size_y,
                 win: Window | None = None,
                 seed: int | float | str | bytes | bytearray | None =None,
                 verbose: bool = False,
                 ):
        if seed != None:
            random.seed(seed)

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win

        if verbose:
            print("Constructing cells ...")
        self._create_cells()
        if verbose:
            print("Breaking some walls ...")
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        if verbose:
            print("Resetting cells' visited parameter to False ...")
        self._reset_cells_visited()
        if verbose:
            print('Maze is ready. Please enjoy all paths equally!')

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if (i,j) == (len(self._cells) - 1, len(self._cells[0]) - 1):
            return True
        next_dirs = self._get_neighbours(i,j) 
        for next_dir in next_dirs:
            next_i, next_j = next_dirs[next_dir]
            current =  self._cells[i][j]
            to_cell = self._cells[next_i][next_j]
            if to_cell.visited:
                continue
            match next_dir:
                case "left":
                    if current.has_left_wall or to_cell.has_right_wall:
                        continue
                case "right":
                    if current.has_right_wall or to_cell.has_left_wall:
                        continue
                case "up":
                    if current.has_top_wall or to_cell.has_bottom_wall:
                        continue
                case "down":
                    if current.has_bottom_wall or to_cell.has_top_wall:
                        continue
            current.draw_move(to_cell)
            if self._solve_r(next_i, next_j):
                return True
            current.draw_move(to_cell, undo=True)
        return False

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False
                # self._draw_cell(i,j, animate=False)

    def _get_neighbours(self, i, j):
        return {
            "left": (        max( 0, i - 1)             ,                     j                ),
            "right":( min( len( self._cells) - 1, i + 1),                     j                ),
            "up"  : (                i                  ,             max( 0, j - 1 )          ),
            "down": (                i                  , min( len(self._cells[0]) - 1, j + 1) ),
        }

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        neighbours  = self._get_neighbours(i,j) 
        not_visited = [
            k 
            for k in neighbours
            if not self._cells[neighbours[k][0]][neighbours[k][1]].visited
        ]
        if len(not_visited) < 1:
            self._draw_cell(i,j)
            return
        next_dir = random.choice(not_visited)
        next_i, next_j = neighbours[next_dir]
        match next_dir:
            case "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
                self._break_walls_r(next_i, next_j)
            case "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
                self._break_walls_r(next_i, next_j)
            case "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
                self._break_walls_r(next_i, next_j)
            case "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
                self._break_walls_r(next_i, next_j)
        self._break_walls_r(next_i, next_j)
        self._draw_cell(i,j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1 , self._num_rows - 1)

    def _create_cells(self):
        self._cells = [
            [
                Cell(self._win) for _ in range(self._num_rows)
            ] for _ in range(self._num_cols)
        ]

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j, animate=True):
        x1 = self._x1 + i*self._cell_size_x
        y1 = self._y1 + j*self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        if animate:
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        delay = 3/(len(self._cells) * len(self._cells[0]))
        delay = min(delay, 0.05)
        time.sleep(delay)
