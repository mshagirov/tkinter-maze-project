from tkinter import BOTH, Canvas, Tk

from line import Line
# from point import Point

class Window:
    def __init__(self, width:int, height:int):
        self.__root = Tk()
        self.__root.title('Maze Puzzle Solver')
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('window closed...')

    def close(self):
        self.__running = False

    def draw_line(self, line:Line, fill_color="red"):
        line.draw(self.__canvas, fill_color=fill_color)


