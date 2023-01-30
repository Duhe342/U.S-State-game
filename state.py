from turtle import Turtle


class State(Turtle):
    def __init__(self, name):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.name = name

    def move_state(self, x, y):
        self.goto(x, y)
        self.write(self.name)


