import re
from cmath import sqrt as csqrt
A=float(input("请输入x³系数:"))
B=float(input("请输入x²系数:"))
C=float(input("请输入x系数:"))
D=float(input("请输入常数:"))
Equation1=f"{A}*x**3+{B}*x**2+{C}*x+{D}=0"
def gx(k):
    if k in ("","+"):
        return 1
    elif k in ("-"):#或者写elif k==-
        return -1
    else:
        return float(k)
s1=re.search(r"(-?\d*\.?\d*)*?x\*\*3",Equation1)
s2=re.search(r"(-?\d*\.?\d*)*?x\*\*2",Equation1)
s3=re.search(r"(-?\d*\.?\d*)*?x\*",Equation1)
s4=re.search(r"([+-]?\d+\.?\d*)=\s*(.+)",Equation1)
m1=s1.group(1) if s1 and s1.group(1) else "1"  #把match拆开
m2=s2.group(1) if s2 and s2.group(1) else "1"
m3=s3.group(1) if s3 and s3.group(1) else "1"
m4=s4.group(1) if s4 and s4.group(1) else "1"
coeff_1=gx(m1)
coeff_2=gx(m2)
coeff_3=gx(m3)
coeff_4=gx(m4)
dat=(coeff_1,coeff_2,coeff_3,coeff_4)
a=dat[0]
b=dat[1]
c=dat[2]
d=dat[3]
p=(3*a*c-b**2)/(3*a**2)
q=(2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)
#计算p,q的相应参数
def clear_im(z):
        if abs(z.imag)<1e-7:
            return z.real
        else:
            return z
#清理虚部误差
x1=x2=x3=None
if (q/2)**2+(p/3)**3>=0:
    print("1个实根+2个共轭复根")
    Equation2=f"t**3+{p}t+{q}=0"
    P=(q/2)**2+(p/3)**3
#定义判别式u=(q/2)**2+(p/3)**3
#A=M=(-q/2)+u开根号
    M=-q/2+csqrt(P)
    N=-q/2-csqrt(P)
    u=M**(1/3)#N,M可能为负数,cmath复数模块,无立方复数
    (w1:=-1/2+1/2*3**(1/2)*1j)
    #海象运算符加括号,全部括上
    (w2:=-1/2-csqrt(3)/2*1j)
    def valute(t,a,b):
        return t-b/(3*a)
    v=(-p/3)/u
    #if abs(u*v+p/3)<1e-9:#计算机存小数存在误差,1e-9精度为10的负9次方
    t1=u+v
    t2=w1*u+w2*v
    t3=w2*u+w1*v
    x1,x2,x3=valute(t1,a,b),valute(t2,a,b),valute(t3,a,b)
    x1=clear_im(x1)
    x2=clear_im(x2)
    x3=clear_im(x3)
elif (q/2)**2+(p/3)**3<=0:
    print("三个实数根")
    from sympy import symbols,sin,cos,solve,pi,Eq
    theta1=symbols('theta1')#alt+小键盘952 
    Eq(cos(3*theta1),(-q/2)/(-p/3)**(3/2))
    result=solve(Eq,theta1)
    o=1/3*result
    y1,y2,y3=o,o+(2/3)*pi,o+(4/3)*pi
    h=2*(-p/3)**(1/2)
    x1,x2,x3=h*cos(y1),h*cos(y2),h*cos(y3)
    x1=clear_im(x1)
    x2=clear_im(x2)
    x3=clear_im(x3)
print(x1,"\n",x2,"\n",x3,"\n")




    


