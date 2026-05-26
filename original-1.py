import turtle
from sympy import symbols,sin,cos,Eq,solve
import math
a,b,c=100,300,100+300*math.sqrt(2)
theta=symbols("theta")
equation=Eq(cos(theta),(a**2+c**2-b**2)/(2*a*c))#cos返回无穷个点,取第一个
#Eq=(cos(theta),(a**2+c**2-b**2)/(2*a*c))#2ac没有加括号
result=solve(equation,theta)
theta_rad=float(result[0].as_real_imag()[0])#cos返回无穷个点,取第一个
theta_deg=math.degrees(theta_rad)#弧度转度数
k=math.sqrt((100+300*math.sqrt(2)))/400
n=0
n+=1
t=turtle.Turtle()
w=1200
h=1200
turtle.setup(width=w,height=h,startx=0,starty=0)
turtle.setworldcoordinates(0,0,w,h)
turtle.bgcolor("black")
t.pencolor("white")
t.pensize(5)
t.penup()
t.goto(200,1000)
t.pendown()
t.left(22.5)#从水平右转正确方向
u=400
for i in range(8):
    t.fd(400)
    t.right(45)
t.fd(300)#300最初是第一个长,不能加入循环计算
t.right(theta_deg)#theta_deg=22.5
p=1
while True:#while m<2(m未定义):#第二圈开始循环
    #p=1
    m=u*(k**p)
    for i in range(8):
        t.fd(m)
        t.right(45)
    t.fd((3/4)*m)
    t.right(theta_deg)
    p+=1
    if m<30:
        break
turtle.done()


        

