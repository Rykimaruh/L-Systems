import turtle  
import math  


def fractal(aturt, depth, maxdepth, riangle = 90, angle = 45): 
     
   if depth > maxdepth:  
     return  
   distance = 180*((math.sqrt(2)/2)**depth)  # ** = exponential power operator. distance of 127

   anotherturt = aturt.clone()  
   aturt.forward(distance)  
   aturt.left(angle)  #angle
   fractal(aturt, depth+1, maxdepth)  
   anotherturt.right(riangle) #angle  
   anotherturt.forward(distance)  
   anotherturt.left(riangle) #angle 
   anotherturt.forward(distance)  
   if depth != maxdepth:  
     turt3 = anotherturt.clone()  
     turt3.left(angle)  
     turt3.forward(180*((math.sqrt(2)/2)**(1+depth)))  
     turt3.right(riangle)  
     fractal(turt3, depth+1, maxdepth)  
   anotherturt.left(riangle)  
   anotherturt.forward(distance)  


def draw_fractal():  

   window = turtle.Screen()  
   turt = turtle.Turtle()  
   turt.hideturtle()  
   turt.penup()  
   turt.goto(-75, -225)  
   turt.pendown()  
   turt.speed(0)  
   turt.left(90)  
   fractal(turt, 1, 12)  
   window.exitonclick()  


draw_fractal() 