import turtle

def FractalSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = Fractalprocess(startStr) 
        startStr = endStr 

    return endStr

def Fractalprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + FractalRules(choice) 

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

def Fractaldraw(orders,angles, distance): 
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

    instance = FractalSystem(6, "X")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    Fractaldraw(instance, 25, 5) 
    wn.exitonclick() 

source()

