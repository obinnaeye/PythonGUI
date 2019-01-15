import turtle

wn = turtle.Screen()
wn.bgcolor("white") 
wn.title("Perplexing Patterns")
turtle.setup(800, 800)
# turtle.speed(1)
turtle.pen(pensize=3)

tess = turtle.Turtle()
tess.penup()
tess.color('grey')

turtle.color('grey')
turtle.penup()
turtle.goto(0, 0)

# turtle.right(50)
for n in range(3,10):
    turtle.penup()
    turtle.fd(135)
    turtle.pendown()
    angle = 360 / n
    for count in range(n):
        turtle.fd(30)
        turtle.right(angle)  # Draw a square in the current colour.   
    if n == 3:
        turtle.rt(180 - 360/7)
    else:
        turtle.rt(360/7)     

turtle.ht()
wn.mainloop()