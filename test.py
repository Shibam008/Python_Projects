import turtle

def draw_heart():
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def draw_text():
    turtle.penup()
    turtle.goto(0, 180)
    turtle.pendown()
    turtle.color("black")
    turtle.write("I Love You Mam", align="center", font=("Arial", 24, "normal"))

def draw_love_pattern():
    turtle.speed(2)
    turtle.bgcolor("white")

    draw_heart()
    draw_text()

    turtle.hideturtle()
    turtle.done()

# Main function
def main():
    draw_love_pattern()

if __name__ == "__main__":
    main()

