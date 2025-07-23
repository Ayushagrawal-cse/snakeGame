from turtle import Turtle



STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]



    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)


    def add_segment(self,position):
        new_element = Turtle(shape="square")
        new_element.color("red")
        new_element.penup()
        new_element.goto(position)
        self.segment.append(new_element)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            num_x = self.segment[seg_num - 1].xcor()
            num_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(num_x, num_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segment[0].heading()!=DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading()!=UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading()!=RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading()!=LEFT:
            self.segment[0].setheading(RIGHT)





