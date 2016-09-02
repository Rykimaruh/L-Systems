import turtle

def pythagorasSystem(Iters,axiom): 
    startStr = axiom 
    endStr = "" 
    for i in range(Iters): 
        endStr = Pythagorasprocess(startStr) 
        startStr = endStr 

    return endStr      

def Pythagorasprocess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + pythagorasRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

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
            

def source():
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

source()