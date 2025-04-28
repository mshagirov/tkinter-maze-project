from point import Point
from tkinter import Canvas

class Line:
    def __init__(self, start:Point, end:Point)->None:
        self.start = start
        self.end = end

    def draw(self, canvas:Canvas, fill_color="black", width=2)->None:
        canvas.create_line(self.start.x, self.start.y,
                           self.end.x, self.end.y,
                           fill=fill_color,
                           width=width
                           )

