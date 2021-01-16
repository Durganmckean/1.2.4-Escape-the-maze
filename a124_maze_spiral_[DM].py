import turtle
import random as rand

wall_width = 10
num_of_sides = 25
length = wall_width

myturtle = turtle.Turtle()
wn = turtle.Screen()

for i in  range(num_of_sides):
    myturtle.pendown()
    if i >= 1:
        door = rand.randint(wall_width*2, (length))
        myturtle.forward(wall_width)
        myturtle.penup()
        myturtle.forward(door)
        myturtle.pendown()
        myturtle.forward(length - wall_width*2)

        barrier = rand.randint(wall_width*2, (length))
        '''myturtle.forward(10)
        myturtle.left(90)
        myturtle.forward(wall_width)
        myturtle.back(wall_width)
        myturtle.right(90)'''

        if door is True:
            myturtle.forward(door)
            myturtle.forward(barrier - door)
            
        else:
            myturtle.forward(barrier)
            myturtle.forward(door - barrier)
            
        
    else:
        myturtle.forward(length)
    myturtle.right(90)
    if i%2 == 0:
        length += wall_width

    





wn.mainloop()


