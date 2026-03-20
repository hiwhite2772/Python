import turtle
# Tạo màn hình vẽ
wn = turtle.Screen()
wn.title("Cờ Tổ Quốc Việt Nam")
wn.bgcolor("white")
pen = turtle.Turtle()
pen.speed(3)
# Hàm vẽ hình chữ nhật
def draw_rectangle(color, width, height):
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()
# Vẽ nền đỏ
pen.penup()
pen.goto(-150, 100)
pen.pendown()
draw_rectangle("red", 300, 200)
# Hàm vẽ sao vàng
def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)  # Hướng lên trên
    pen.forward(size / 2)
    pen.right(162)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()
# Vẽ sao vàng đúng giữa lá cờ
draw_star(0, 0, 50)
pen.hideturtle()
wn.mainloop()
