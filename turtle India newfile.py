a=50
b=100
import turtle

t=turtle.Turtle()
#t.speed(100000)

wn=turtle.Screen()

t.color("orange")

t.color("black")

t.penup()


t.goto(-250+a,350+b)
t.pendown()
t.color('black',"orange")
t.begin_fill()
t.goto(250+a,350+b)
t.goto(250+a,275+b)
t.goto(-250+a,275+b)
t.goto(-250+a,350+b)
t.end_fill()


t.penup()
t.goto(-250+a,275+b)
t.pendown()
t.color('black',"white")
t.begin_fill()
t.goto(250+a,275+b)
t.goto(250+a,200+b)
t.goto(-250+a,200+b)
t.goto(-250+a,275+b)
t.end_fill()

t.penup()
t.goto(-250+a,200+b)
t.pendown()
t.color('black',"green")
t.begin_fill()
t.goto(250+a,200+b)
t.goto(250+a,125+b)
t.goto(-250+a,125+b)
t.goto(-250+a,200+b)
t.end_fill()

t.color("black")
t.penup()
t.goto(-250+a,275+b)
t.pendown()
t.goto(250+a,275+b)
t.penup()
t.goto(-250+a,200+b)
t.pendown()
t.goto(250+a,200+b)



t.penup()
t.goto(0+a,200+b)
t.pendown()
t.color('blue')
t.width(3)
t.circle(38)


for i in range(24):
	t.penup()
	t.goto(0+a,237+b)
	t.pendown()
	
	t.forward(36)
	t.right(15)
	
wn.bgcolor("white")
	


t.penup()
t.goto(-250+a,350+b)
t.pendown()
t.begin_fill()
t.width(1)
t.color("black","gold")
t.goto(-250+a,380+b)
t.goto(-250+a,-600+b)
t.goto(-270+a,-600+b)
t.goto(-270+a,380+b)
t.goto(-250+a,380+b)
t.goto(-260+a,380+b)
t.circle(20)
t.end_fill()



#steps


t.penup()
t.goto(-270+a,-600+b)
t.pendown()
t.color("black","orange")
t.begin_fill()
t.goto(-300+a,-600+b)
t.goto(-220+a,-600+b)
t.goto(-220+a,-630+b)
t.goto(-300+a,-630+b)
t.goto(-300+a,-600+b)
t.end_fill()

t.color("black")
t.penup()
t.goto(-300+a,-630+b)
t.color("black","white")
t.begin_fill()
t.pendown()
t.goto(-330+a,-630+b)
t.goto(-190+a,-630+b)
t.goto(-190+a,-660+b)
t.goto(-330+a,-660+b)
t.goto(-330+a,-630+b)
t.end_fill()



t.penup()
t.goto(-330+a, -660+b)
t.pendown()
t.color("black","green")
t.begin_fill()
t.goto(-360+a,-660+b)
t.goto(-160+a,-660+b)
t.goto(-160+a,-690+b)
t.goto(-360+a,-690+b)
t.goto(-360+a,-660+b)
t.end_fill()
wn.bgcolor("black")

#t.penup()
#t.goto(-150,0)

#t.color("blue")
#t.write("HAPPY")
#t.goto(-20,0)
#t.write("INDEPENDENCE")
#t.goto(230,0)
#t.write("DAY")
#t.penup()

#for i in range(10000):
#	t.goto(a,b)
#	a,b=b,a+b
#	wn.bgcolor("orange")
#	t.goto(a,b)
#	a,b=b,a-b
#	wn.bgcolor("white")
#	t.goto(a,b)
#	a,b=b,a+b
#	wn.bgcolor("green")
#	t.goto(a,b)
#	a,b=b,a-b
#	t.speed(1)

for i in range(10000):
	t.speed(1)
	t.color('orange')
	t.color("white")
	t.color("green")
	
	

