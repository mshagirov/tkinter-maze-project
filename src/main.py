from window import Window
from maze import Maze

def main():
    rng_seed = 2 # random.seed(rng_seed) for debugging; else set to None
    num_rows = 12
    num_cols = 16
    padding = 50
    screen_width = 800
    screen_height = 600
    cell_size_x = (screen_width - 2 * padding) / num_cols
    cell_size_y = (screen_height - 2 * padding) / num_rows

    win = Window(screen_width, screen_height)
    
    maze = Maze(padding,
                padding,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win=win,
                seed=rng_seed,verbose=True)

    print("Solving the maze ...")
    result = maze.solve()
    print(f'Maze is solved : {result}')

    win.wait_for_close()


if __name__ == '__main__':
    main()
