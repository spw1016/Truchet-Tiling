__author__='Sergei Wallace'

from turtle import *
import random
import sys


def tiling(wall_width, wall_height, tile_type, tile_size):
    """
    This function produces a truchet tile pattern using turtle graphics.
    :param wall_width: width of the patterned area
    :param wall_height: height of the patterned area
    :param tile_type: type of tile design. values range from 1-3
    :param tile_size: height and width of the tile. It must be a divisor of the wall height and width such that the
    remainder is zero.
    :return: none
    """

    class MyTurtle(Turtle):
        """
        Define a class named MyTurtle that is a subclass of Turtle
        to provide an interface for graphics similar to those in
        other languages such as Java and C#.
        """

        def __init__(self):
            """ Constructor
            """

            # Call the constructor of the parent class
            Turtle.__init__(self)
            # Hide the turtle
            Turtle.hideturtle(self)
            s = Screen()
            s.setup(width=wall_width+0.05*wall_width, height=wall_height+0.05*wall_height)
            self.speed(100)

        def draw_line(self, x1, y1, x2, y2):
            """ Draw a line from (x1, y1) to (x2, y2).
            """

            self.penup()
            self.goto(x1, y1)
            self.pendown()
            self.goto(x2, y2)


        def draw_rect(self, x, y, width, height):
            """ Draw the outline of the specified rectangle.
               (x, y) is the coordinates for the top-left corner.
            """

            self.penup()
            self.goto(x, y)
            self.pendown()
            self.goto(x + width, y)
            self.goto(x + width, y + height)
            self.goto(x, y + height)
            self.goto(x, y)

        def draw_arc(self, x, y, radius, start_angle, arc_angle):
            """ Draw a circular arc.
           (x, y): the center of the circle.
           startAngle: angle in degrees measured counterclockwise from the x-axis
           to the starting point of the arc.
           arcAngle: angle in degrees measured counterclockwise from the startAngle
           parameter to ending point of the arc.
           """

            self.penup()
            self.setheading(90)
            self.goto(x + radius, y)
            self.circle(radius, start_angle)
            self.pendown()
            self.circle(radius, arc_angle)

        def draw_tile(self, x, y, orientation):
            """
            draw_tile provides the drawing instructions for three different types of tiles.
            :param x: x coordinate (bottom left)
            :param y: y coordinate (bottom left)
            :param orientation: determines which direction the tile will be oriented (tiles have two fold rotational
            symmetry)
            """
            if tile_type == 1:
                if orientation == 0:
                    self.draw_arc(x, y, tile_size/2, 0, 90)
                    self.draw_arc(x + tile_size, y + tile_size, tile_size/2, 180, 90)
                else:
                    self.draw_arc(x + tile_size, y, tile_size/2, 90, 90)
                    self.draw_arc(x, y + tile_size, tile_size/2, 270, 90)
            elif tile_type == 2:
                if orientation == 0:
                    self.draw_line(x, y, x + 0.2*tile_size, y + tile_size/2)
                    self.draw_line(x + tile_size, y, x + tile_size - 0.2*tile_size, y + tile_size/2)
                    self.draw_line(x + 0.2*tile_size, y + tile_size/2, x + tile_size - 0.2*tile_size, y + tile_size/2)
                    self.draw_line(x, y + tile_size, x + 0.2*tile_size, y + tile_size/2)
                    self.draw_line(x + tile_size, y + tile_size, x + tile_size - 0.2*tile_size, y + tile_size/2)
                else:
                    self.draw_line(x, y, x + tile_size/2, y + 0.2*tile_size)
                    self.draw_line(x + tile_size, y, x + tile_size/2, y + 0.2*tile_size)
                    self.draw_line(x + tile_size/2, y + 0.2*tile_size, x + tile_size/2, y + tile_size - 0.2*tile_size)
                    self.draw_line(x, y + tile_size, x + tile_size/2, y + tile_size - 0.2*tile_size)
                    self.draw_line(x + tile_size, y + tile_size, x + tile_size/2, y + tile_size - 0.2*tile_size)
            elif tile_type == 3:
                if orientation == 0:
                    self.draw_line(x, y, x + tile_size, y + tile_size)
                else:
                    self.draw_line(x + tile_size, y, x, y + tile_size)
            else:
                print("\nincorrect input parameter for tile type. Tile types range from integers 1-3.\n")
                sys.exit()

        def draw_tiles(self):
            """
            draws randomly oriented tiles to form a patterned area.
            """
            self.draw_rect(-wall_width/2, -wall_height/2, wall_width, wall_height)
            for x in range(int(-wall_width/2), int(wall_width/2), tile_size):
                for y in range(int(-wall_height/2), int(wall_height/2), tile_size):
                    self.draw_tile(x, y, random.randint(0, 1))

    if (wall_width or wall_width) % tile_size != 0:
        print("\nThe wall width and height parameters are not divisible by the tile size parameter. Please try again.\n")
        sys.exit()
    else:
        truchet = MyTurtle()
        truchet.draw_tiles()
        mainloop()

tiling(500, 500, 3, 50)