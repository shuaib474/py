import turtle
from sympy import symbols,sin,cos,Eq,solve
import math
u=400
a=400*((math.sqrt(5)-1)/(math.sqrt(5)+1))#黄金分割
b=400*(2/(math.sqrt(5)+1))
cos145=math.cos(math.radians(145))
sin45=math.sin(math.radians(45))
c=symbols('c')#定义c为未知数
x=symbols('x')
equation_c=Eq(cos145,(a**2+b**2-c**2)/(2*a*b))
res1=solve(equation_c,c)
C=float([s for s in res1 if s>0][0].evalf())
equation_jiao=Eq((C/sin45),(b/x))
snx=solve(equation_jiao,x)#sympy的solve解出来的东西不能直接用( Expr)
sinx=float([v for v in snx if v>0][0].evalf())
sn=math.asin(sinx)
degg=math.degrees(sn)
k=C/u#边长比例系数
n=0
n+=1
t=turtle.Turtle()
turtle.tracer(0,0)
t.hideturtle()
w=1300
h=1300
turtle.setup(width=w,height=h,startx=0,starty=0)
turtle.setworldcoordinates(0,0,w,h)
turtle.bgcolor("black")
t.pencolor("white")
t.pensize(5)
t.penup()
t.goto(200,1150)
t.pendown()
t.left(22.5)#从水平右转正确方向
for i in range(8):
    t.fd(400)
    t.right(45)
t.fd(a)#a是最初
t.right(degg)
p=1
while True:
    m=400*(k**p)
    for i in range(7):
        t.fd(m)
        t.right(45)
    t.fd(((math.sqrt(5)-1)/(math.sqrt(5)+1))*m)
    t.right(degg)
    p+=1
    if m<70:
        break
t.pencolor("red")
t.pensize(15)
t.penup()
t.goto(0,1100)
t.pendown()
t.write("20250608216 工程2 曾仁烨",font=("微软雅黑",20,"normal"))
turtle.done()


        

