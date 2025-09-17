from turtle import *
speed(5)
pencolor('red')
side = 6
for i in range (side):
    for i in range (side):
        for i in range(side):
            fd(25)
            lt(360/side)
            
            dot(5)
            circle(10,4)
        fd(50)
        lt(360/side)        
    fd(100)
    lt(360/side)

hideturtle()
mainloop