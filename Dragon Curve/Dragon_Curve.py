#Jonathan Nunez
#Lindermayer System show cases iteration by following particular set of instructions and observing it's own "growth" just like in biological systems such as tree
#this was made as a simple observational concept to help understand better the L-System

import turtle #here we import the turtle library
import sys

def dragonSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = dragonprocess(startStr) 
        startStr = endStr 

    return endStr       

def dragonprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + dragonRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def dragonRules(choice):
    newstr = ""
    if choice == 'X':         
        newstr = 'X+YF+'
    elif choice == 'Y':
        newstr= '-FX-Y'       
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def dragondraw(orders,angles, distance): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders:
        if cmd == 'F':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.forward(distance)
        elif cmd == '+':
                    turtle.right(angles)
        elif cmd == '-':
                    turtle.left(angles)
       
def source():

    instance = dragonSystem(10, "FX")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    dragondraw( instance, 90, 5) 
    wn.exitonclick() 

source()

