from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.X_move = 10
        self.Y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.X_move
        new_y = self.ycor() + self.Y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.Y_move *= -1

    def bounce_x(self):
        self.X_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
