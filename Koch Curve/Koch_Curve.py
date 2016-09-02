#Jonathan Nunez
#Lindermayer System show cases iteration by following particular set of instructions and observing it's own "growth" just like in biological systems such as tree
#this was made as a simple observational concept to help understand better the L-System

import turtle #here we import the turtle library
import sys

def kochcurveSystem(Iters,axiom): #numIters is number of iterations while the axiom is the starting string of the algorithm
    startStr = axiom #the axiom variable is assigned as startString
    endStr = "" #endString initialized to null
    for i in range(Iters): #for loop iterating thru the range of iterations given in the main as argument
        endStr = kochcurveprocess(startStr) #processstring is where the conversion happend and result assigned to endString variable
        startStr = endStr #therefore the endString becomes the new one

    return endStr       #APPARENTLY TOO MUCH INDENT CAN GIVE A LOGIC ERROR! WTF PYTHON!?! DOUBLE TABBING CAN CAUSE THIS SHIT OMFG!!

def kochcurveprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + kochcurveRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def kochcurveRules(choice):
    newstr = ""
    if choice == 'F':         
        newstr = 'F+F-F-F+F'       
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def kochcurvedraw(orders,angles, distance): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders:
        if cmd == 'F':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.backward(distance)
        elif cmd == '-':
                    turtle.right(angles)
        elif cmd == '+':
                    turtle.left(angles)
        elif cmd=='[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd==']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()
        elif cmd=='X':
            pass

def source():

    instance = kochcurveSystem(4, "F")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    kochcurvedraw( instance, 90, 5) 
    wn.exitonclick() 

source()

