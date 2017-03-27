import turtle
def Flower(s):
    for i in range(1,3):
        s.forward(100)
        s.left(45)
        s.forward(100)
        s.left(135)
    #s.forward(100)
def line(s):
    for i in range(1,2):
        s.right(90)
        s.forward(300)
def art():
    window=turtle.Screen()
    window.bgcolor("green")
    s=turtle.Turtle()
    s.shape("turtle")
    s.color("blue")
    s.speed(10)
    for i in range(1,37):
            Flower(s)
            s.right(10)
    for i in range(1,2):
        line(s)
    window.exitonclick()       
    
art()
