from re import L
import unittest

from maze import Maze

class Tests(unittest.TestCase):
    seed = 42
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10,10, seed=Tests.seed)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    
    def test_maze_x1_y1(self):
        x1 = 123
        y1 = 456
        m1 = Maze(x1, y1, 10, 10, 10, 10, seed=Tests.seed)
        self.assertEqual(m1._x1, x1)
        self.assertEqual(m1._y1, y1)

    def test_maze_cell_size(self):
        size_x = 11
        size_y = 12
        m1 = Maze(0, 0, 10, 10, size_x, size_y, seed=Tests.seed)
        self.assertEqual(m1._cell_size_x, size_x)
        self.assertEqual(m1._cell_size_y, size_y)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 15
        num_rows = 8
        m1 = Maze(0,0,num_rows, num_cols, 10, 10, seed=Tests.seed)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_maze_break_walls_and_reset(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0,0,num_rows, num_cols, 10, 10, seed=Tests.seed)
        visited = []
        for col in m1._cells:
            for c_ij in col:
                if c_ij.visited:
                    visited.append(c_ij)
        self.assertEqual(len(visited), 0)
        if m1._cells[0][0].has_right_wall:
            self.assertFalse(m1._cells[0][0].has_bottom_wall)
            self.assertFalse(m1._cells[0][1].has_top_wall)
            self.assertFalse(m1._cells[0][1].has_right_wall)
            self.assertFalse(m1._cells[1][1].has_left_wall)
        else:
            self.assertFalse(m1._cells[1][0].has_left_wall)
            self.assertFalse(m1._cells[1][0].has_bottom_wall)
            self.assertFalse(m1._cells[1][1].has_top_wall)



if __name__ == "__main__":
    unittest.main()
