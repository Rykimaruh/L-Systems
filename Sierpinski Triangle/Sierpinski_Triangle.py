#Jonathan Nunez
#Lindermayer System show cases iteration by following particular set of instructions and observing it's own "growth" just like in biological systems such as tree
#this was made as a simple observational concept to help understand better the L-System

import turtle #here we import the turtle library
import sys

def sierpinskySystem(Iters,axiom): #numIters is number of iterations while the axiom is the starting string of the algorithm
    startStr = axiom #the axiom variable is assigned as startString
    endStr = "" #endString initialized to null
    for i in range(Iters): #for loop iterating thru the range of iterations given in the main as argument
        endStr = sierpinskyprocess(startStr) #processstring is where the conversion happend and result assigned to endString variable
        startStr = endStr #therefore the endString becomes the new one

    return endStr       #APPARENTLY TOO MUCH INDENT CAN GIVE A LOGIC ERROR! WTF PYTHON!?! DOUBLE TABBING CAN CAUSE THIS SHIT OMFG!!

def sierpinskyprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + sierpinskyRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def sierpinskyRules(choice):
    newstr = ""
    if choice == 'A':         
        newstr = '+B-A-B+'
    elif choice == 'B':
        newstr= '-A+B+A-'       
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def sierpinskydraw(orders,angles, distance): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders: #orders refers to the string
        if cmd == 'A':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.forward(distance)
        elif cmd == '-':
                    turtle.right(angles)
        elif cmd == '+':
                    turtle.left(angles)
       
def source():

    instance = sierpinskySystem(8, "A")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    sierpinskydraw( instance, 60, 5) 
    wn.exitonclick() 

source()

