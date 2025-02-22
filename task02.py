import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    start_pos = t.pos()
    start_heading = t.heading()

    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()

    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()

def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_pythagoras_tree(t, 100, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()