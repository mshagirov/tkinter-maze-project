"""
Cell : grid cell (box) with maximum 4 walls
"""
from point import Point
from line import Line   

class Cell:
    def __init__(self, window=None):
        self.visited = False

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # location on canvas
        # top-left
        self._x1 = None
        self._y1 = None
        # bottom-right
        self._x2 = None
        self._y2 = None

        # host Window object
        self._win = window

    def get_loc(self):
        if (self._x1 is None) or (self._x2 is None) or (self._y1 is None) or (self._y2 is None):
            return
        return (self._x1 + self._x2) // 2,  (self._y1 + self._y2) // 2


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        color = "gray" if undo else "red"
        loc1 = self.get_loc()
        loc2 = to_cell.get_loc()
        if loc1 is None or loc2 is None:
            return
        x1, y1 = loc1
        x2, y2 = loc2
        self._win.draw_line(
            Line( Point(x1, y1), Point(x2, y2) ),
            fill_color=color
        )

    def draw(self, x1, y1, x2, y2, fill_color="black", no_wall_color="white"):
        if self._win is None:
            return
        # top-left
        self._x1, self._y1 = x1, y1
        # bottom-right
        self._x2, self._y2 = x2, y2
        if self.has_left_wall:
            self._win.draw_line( Line( Point(x1, y1), Point(x1, y2) ),
                                fill_color=fill_color
                                )
        else:
            self._win.draw_line( Line( Point(x1, y1), Point(x1, y2) ),
                                fill_color=no_wall_color
                                )

        if self.has_right_wall:
            self._win.draw_line( Line( Point(x2, y1), Point(x2, y2) ),
                                fill_color=fill_color
                                )
        else:
            self._win.draw_line( Line( Point(x2, y1), Point(x2, y2) ),
                                fill_color=no_wall_color
                                )
        if self.has_top_wall:
            self._win.draw_line( Line( Point(x1, y1), Point(x2, y1) ),
                                fill_color=fill_color
                                )
        else:
            self._win.draw_line( Line( Point(x1, y1), Point(x2, y1) ),
                                fill_color=no_wall_color
                                )
        if self.has_bottom_wall:
            self._win.draw_line( Line( Point(x1, y2), Point(x2, y2) ),
                                fill_color=fill_color
                                )
        else:
            self._win.draw_line( Line( Point(x1, y2), Point(x2, y2) ),
                                fill_color=no_wall_color
            )


