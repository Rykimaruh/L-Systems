#Jonathan Nunez
#Lindermayer System show cases iteration by following particular set of instructions and observing it's own "growth" just like in biological systems such as tree
#this was made as a simple observational concept to help understand better the L-System

import turtle #here we import the turtle library
import sys

def MakeLSystem(Iters,axiom): #numIters is number of iterations while the axiom is the starting string of the algorithm
    startStr = axiom #the axiom variable is assigned as startString
    endStr = "" #endString initialized to null
    for i in range(Iters): #for loop iterating thru the range of iterations given in the main as argument
        endStr = process(startStr) #processstring is where the conversion happend and result assigned to endString variable
        startStr = endStr #therefore the endString becomes the new one

    return endStr        #APPARENTLY TOO MUCH INDENT CAN GIVE A LOGIC ERROR! WTF PYTHON!?! DOUBLE TABBING CAN CAUSE THIS SHIT OMFG!!

def AlgaeSystem(Iters,axiom): 
    startStr=axiom
    endStr = "" 
    for i in range(Iters): 
        print (startStr) #prints the process within range based on the iterations
        endStr = algaeProcess(startStr) 
        startStr = endStr      

    return endStr       

def kochcurveSystem(Iters,axiom): 
    startStr = axiom #the axiom variable is assigned as startString
    endStr = "" #endString initialized to null
    for i in range(Iters): #for loop iterating thru the range of iterations given in the main as argument
        endStr = kochcurveprocess(startStr) #processstring is where the conversion happend and result assigned to endString variable
        startStr = endStr #therefore the endString becomes the new one

    return endStr 

def sierpinskySystem(Iters,axiom): 
    startStr = axiom #the axiom variable is assigned as startString
    endStr = "" #endString initialized to null
    for i in range(Iters): #for loop iterating thru the range of iterations given in the main as argument
        endStr = sierpinskyprocess(startStr) #processstring is where the conversion happend and result assigned to endString variable
        startStr = endStr #therefore the endString becomes the new one

    return endStr  

def dragonSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = dragonprocess(startStr) 
        startStr = endStr 

    return endStr 

def FractalSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = Fractalprocess(startStr) 
        startStr = endStr 

    return endStr

def pythagorasSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = Pythagorasprocess(startStr) 
        startStr = endStr 

    return endStr 

def process(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + conditionsRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def algaeProcess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + algaeRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def kochcurveprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + kochcurveRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def sierpinskyprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + sierpinskyRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def dragonprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + dragonRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def Fractalprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + FractalRules(choice) 

    return newstr

def Pythagorasprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + pythagorasRules(choice) 

    return newstr

def conditionsRules(choice):
    newstr = ""
    if choice == 'F': #A->B | B -> AB | AB -> BAB...etc
        newstr = 'F-F++F-F'   # Rule 1
        #newstr = 'F+F--F+F+F'
        #newstr = 'F-[[X+X]+F[+FX]-X'
        #newstr = 'F++F-F'
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def kochcurveRules(choice):
    newstr = ""
    if choice == 'F':         
        newstr = 'F+F-F-F+F'       
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def algaeRules(choice):
    newStr=""
    if choice == 'A':
        newStr = 'AB'
    elif choice == 'B':
        newStr = 'A'
    else:
        newStr=choice
            
    return newStr 

def sierpinskyRules(choice):
    newstr = ""
    if choice == 'A':         
        newstr = '+B-A-B+'
    elif choice == 'B':
        newstr= '-A+B+A-'       
    else:
        newstr = choice    #keep character if above condition is not sated

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

def FractalRules(choice):
    newstr = ""
    if choice == 'X': 
        newstr = 'F?[[X]+X]+F[+FX]?X'   
    elif choice == 'F':
        newstr = 'FF'
    else:
        newstr = choice    

    return newstr

def pythagorasRules(choice):
    newstr = ""
    if choice == '1':         
        newstr = '11'
    elif choice == '0':
        newstr= '1[0]0'           
    else:
        newstr = choice    #keep character if above condition is not sated

    return newstr

def Sixthchoice():
    turtle.hideturtle()
    instance = pythagorasSystem(7, "0")   
    print(instance)
    wn = turtle.Screen()    
    turtle.setheading(90)
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    Pythagorasdraw(instance, 90, 5) 
    wn.exitonclick()
    return Sixthchoice()
    return source() 


def Fifthchoice():
    instance = dragonSystem(10, "FX")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    dragondraw( instance, 90, 5) 
    wn.exitonclick() 
    return source() 


def Fourthchoice():
    instance = sierpinskySystem(8, "A")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(100)
    sierpinskydraw( instance, 60, 5) 
    wn.exitonclick() 
    return source()
    return Fourthchoice
     


def Thirdchoice():

    instance = kochcurveSystem(4, "F")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    kochcurvedraw( instance, 90, 5) 
    wn.exitonclick() 
    return Thirdchoice
    return source()
    

def Secondchoice():
    Algaeinstance = AlgaeSystem(7, "A")
    return source() 
    return Secondchoice
    
    

def Firstchoice():

    instance = MakeLSystem(4, "F")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
   # turtle.back(200)
    turtle.goto(-200,-200)
    turtle.down()
    turtle.speed(9)
    draw(instance, 60, 5) 
    wn.exitonclick()
    
    return source()   

def draw(orders,angles, distance): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders:
        if cmd == 'F':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.backward(distance)
        elif cmd == '+':
                    turtle.right(angles)
        elif cmd == '-':
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
      
def sierpinskydraw(orders,angles, distance): 
    stack = []
    for cmd in orders:
        if cmd == 'A':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.forward(distance)
        elif cmd == '-':
                    turtle.right(angles)
        elif cmd == '+':
                    turtle.left(angles)

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

def Fractaldraw(orders,angles, distance): 
    stack = []
    for cmd in orders:
        if cmd == 'F':
                    turtle.forward(distance)
        elif cmd == 'B':
                    turtle.backward(distance)
        elif cmd == '+':
                    turtle.right(angles)
        elif cmd == '-':
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

def Pythagorasdraw(orders,angles, distance): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders:
        if cmd == '1':
                    turtle.forward(distance)
        elif cmd == '0':
                    turtle.backward(distance)
        elif cmd=='[':
            stack.append((turtle.position(), turtle.heading()))
            turtle.left(45)
        elif cmd==']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.right(45)
            turtle.pendown()
                          
def switchcase(x):
   switcher = {
        1: Firstchoice,
        2: Secondchoice,
        3: Thirdchoice,
        4: Fourthchoice,
        5: Fifthchoice,
        6: Sixthchoice,
           
    }
   
   func = switcher.get(x, 0)
   func()

def source():

    
    user_input= int(input("Choice: \n 1. Lindenmayer System Draw \n 2. Algae Growth \n 3. Koch Curve \n 4. Sierpinsky Triangle \n 5. Dragon Curve \n 6. Pythagoras Plant \n ")) #you gotta convert your string input to int
    switchcase(user_input)

source()

