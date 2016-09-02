import turtle

def pythagorasRules(choice):
    newStr=""
    if choice == '0':
        newStr = '1[0]0'
    elif choice == '1':
        newStr = '11'
    else:
        newStr=choice
            
    return newStr 

def pythagoraSystem(Iters,axiom): 
    startStr=axiom
    endStr = "" 
    for i in range(Iters): 
        endStr = pythagoraProcess(startStr) 
        startStr = endStr

    return endStr

def pythagoraProcess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + pythagorasRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def pythagorasdraw(orders,angles, distance, min_len): #here the turtle is assigned  basic instructions on how to move using its library of commands. Here we are using 4 parameters
    stack = []
    for cmd in orders:
        if cmd == '0':
                    turtle.forward(distance)
        elif cmd == '1':
                    turtle.forward(distance)
        elif cmd=='[':
            turtle.left(angles/2)
        elif cmd==']':
            turtle.right(angles/2)        

def main():

    instance = pythagoraSystem(7, "0")   
    print(instance)
    wn = turtle.Screen()    
    turtle.up()
    turtle.back(200)
    turtle.down()
    turtle.speed(9)
    pythagorasdraw(instance, 45, 5) 
    wn.exitonclick() 

main()

def tree(f_length, spray=45., branches=1, f_scale=0.5, f_scale_friction=1.4, min_length=10):
    step = float(spray / (branches - 1))
    f_scale /= f_scale_friction
    turtle.forward(f_length)
    if f_length > min_length:
        turtle.left(spray / 2)
        tree(f_scale * f_length, spray, branches, f_scale, f_scale_friction, min_length)
        for counter in range(branches - 1):
            turtle.right(step)
            tree(f_scale * f_length, spray, branches, f_scale, f_scale_friction, min_length)
        turtle.left(spray / 2)
    turtle.back(f_length)

turtle.left(90)
tree(80, spray=120, branches=4)
turtle.exitonclick()