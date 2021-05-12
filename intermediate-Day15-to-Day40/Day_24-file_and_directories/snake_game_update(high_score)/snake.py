
import turtle

# Following are constants.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    """ Holds all the functionality of the snake. Create, Move, Control"""
    def __init__(self):
        self.segments = []
        self.create_snake()  # Create snake body and append it to segments list
        self.head = self.segments[0]  # Holds the head of the snake

    def create_snake(self):
        """ Creates the initial snake body. """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset_snake(self):
        """ Reset snake and make it disappear on the screen """
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()  # Clears the segment list
        self.create_snake()  # Creates snake again
        self.head = self.segments[0]  # Holds the head of the snake

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")  # Creates a single part for snake
        new_segment.color("white")  # Gives snake the color white
        new_segment.penup()  # Internal turtle func. Make snake to not draw line on screen
        new_segment.goto(position)  # Each snake body segment goto new position from STARTING_POSITIONS list
        self.segments.append(new_segment)  # Append each part of the snake body to the segments list

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Make snake move forward by {MOVE_DISTANCE}"""
        # This for loop move the last part of the snake to the 2nd last part position
        # until all the parts of the snake are moved
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Holds the x co-ordinate of the it's previous snake segment
            new_x = self.segments[seg_num - 1].xcor()
            # Holds the y co-ordinate of the it's previous snake segment
            new_y = self.segments[seg_num - 1].ycor()
            # Moves each snake segment to it's previous snake segment by using
            # new_x and new_y co-ordinates
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Moves snake head forward

    def up(self):
        """ Move Snake head Up """
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        """ Move Snake head Left """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """ Move Snake head Down """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """ Move Snake head Right """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

