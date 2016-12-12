'''
This module is used for drawing the van Koch snowflake fractal by using
recursive functions.
'''

import turtle

def vonKochSegment(level, startingPoint, heading, length, turtle):
    '''
    Draws segments of the van Koch fractal by making recursive calls to itself. 
    For each recursive call, the level is decreased by 1 and the base case is when level
    equals zero, the point at which the drawing of the fractal will be complete.
    Returns the endpoint, i.e. finishing position of the turtle, in the end.
    '''
    if level == 0:   #base case: draw a simple equilateral triangle
        turtle.down()
        turtle.setheading(heading)
        turtle.setpos(startingPoint)
        turtle.forward(length)
        return turtle.position()
    else:   
        vonKochSegment(level - 1, startingPoint, heading, length / 3, turtle)
            #for each segment there are four recursive calls because as the level one
            #fractal diagram in the assignment shows, drawing a triangle on a 
            #straight line separates the straight line into four segments.
        turtle.up()   #prevent overlapping with parts of segments that are already
                      #draw by later recursive calls
        turtle.setpos(startingPoint)
        turtle.setheading(heading)
        turtle.forward(length / 3)
        endPoint1 = turtle.position()   #saves the position of the turtle to be
                                        #passed onto the next recursive call
        vonKochSegment(level - 1, endPoint1, heading - 60, length / 3, turtle)
        turtle.up()
        turtle.setpos(endPoint1)
        turtle.setheading(heading - 60)
        turtle.forward(length / 3)
        endPoint2 = turtle.position()
        vonKochSegment(level - 1, endPoint2, heading + 60, length / 3, turtle)
        turtle.up()
        turtle.setpos(endPoint2)
        turtle.setheading(heading + 60)
        turtle.forward(length / 3)
        endPoint3 = turtle.position()
        vonKochSegment(level - 1, endPoint3, heading, length / 3, turtle)
        turtle.up()
        turtle.setpos(endPoint3)
        turtle.setheading(heading)
        turtle.forward(length / 3)
        endPoint4 = turtle.position()
        return endPoint4

def vonKoch(level, length):
    '''
    Creates a turtle and draws three von Koch segments of level 'level' arranged
    in an equilateral triangle.
    '''
    myTurtle = turtle.Turtle()
    startingPoint = myTurtle.pos()
    heading = myTurtle.heading()
    endPoint = vonKochSegment(level, startingPoint, heading, length, myTurtle)
    endPoint = vonKochSegment(level, endPoint, heading + 120, length, myTurtle)
    endPoint = vonKochSegment(level, endPoint, heading - 120, length, myTurtle)
        #there are three calls as the fractal is based on an equilateral triangle,
        #hence each call corresponds to one side of the triangle.
    turtle.exitonclick()

    