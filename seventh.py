n=int(input("输入数字:"))
n=n%2
if n==0:
    print("欢迎使用"*3)
    from turtle import pensize,right,color,screensize,setup,forward,penup,goto,pendown,left,done
    from math import pi
    pensize(4)
    goto(-200,200)
    screensize(800,800)
    setup(800,800,100,100)
    for _ in range(4):
        if _<2:
            color("blue")
        else:
            color("green")
        forward(400)      
        right(90)
    penup
    goto(-200,0)
    pendown
    left(90)
    pensize(4)
    color("red")
    r=200
    step=(2*pi*r/360)
    for _ in range(360):
        forward(step)
        right(1)

    done()
elif n!=0:
    print("输你老冯呢孩子")
