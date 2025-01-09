from graphics.maze import Maze
import unittest
import random

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )

        # testing if start and exit cells are missing appropriate walls
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_rows - 1][num_cols -1].has_bottom_wall)

        # picking any of the cells at random to test
        random_cell = (
            m1._cells[random.randint(0, num_rows -1)][random.randint(0, num_cols - 1)]
        )

        # test if cell has been visited by _break_walls_r()
        m1._break_walls_r(0, 0)
        self.assertTrue(random_cell.visited)

        # test if cell's visited data member has been reset properly
        m1._reset_cells_visited()
        self.assertFalse(random_cell.visited)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )

        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_rows - 1][num_cols -1].has_bottom_wall)

        random_cell = (
            m1._cells[random.randint(0, num_rows -1)][random.randint(0, num_cols - 1)]
        )
        m1._break_walls_r(0, 0)
        self.assertTrue(random_cell.visited)
        m1._reset_cells_visited()
        self.assertFalse(random_cell.visited)

if __name__ == "__main__":
    unittest.main()
