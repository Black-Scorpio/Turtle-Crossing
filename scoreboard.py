from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.current_level = 1
        self.goto(-280, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def level_increase(self):
        self.current_level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
