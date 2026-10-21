from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # constant, starting position of snake body
MOVE_FORWARD = 20    #constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []   #initializing the segment list which stores all segments of the snake as we now initially snake is mad up of 3 turtles
        self.createsnake()   # call create snake method
        self.head = self.segments[0]    # head variable constains head of snake

    def createsnake(self):     # to create the initial snake with 3 turtles
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):           # to create the snake
        segment = Turtle(shape="square")    # shape of snake is square
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extra_segment(self):         # called when snake hits the food to increase the length of the snake
        self.add_segment(self.segments[-1].position())


    def move(self):                # to move the snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()     # 3rd segement is moved is first moved to 2 segment and 2nd to 1st segment
                                                            # (**note - here in range end 0, so 1st segment is not moved in for loop
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)    # 1st segment is moved forward

    def up(self):             # when arrow up key is pressed this method is called and it set snake head to 90 degrees
        if self.head.heading() != DOWN:    #when snake head is down it cant go up, it can only go left and right
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1001)
        self.segments.clear()
        self.createsnake()
        self.head=self.segments[0]
