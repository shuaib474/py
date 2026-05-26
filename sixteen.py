m="fhcuuhrf"
n="6754"
for a in m:
    b=ord(a)
    print(b,end="")
for i in n:
    cc=int(i)
    c=chr(cc)
    print(c,end="")
d1={"name":"张三","age":20}
print(d1,end="")
print(d1.get("nam"))
keys=['1','2','3']
values=['ji','ba','shi']
d2=dict(zip(keys,values))
print(d2)
d3={x:x**3 for x in range(5)}
print(d3,"\n")
print("字典d3长度为{}".format(len(d3)))
#jihe
s1={0,7,5}
print(s1,end="")
list1=[56,78,91,64,64,64]
s2=set(list1)
print(s2,end="")
print(f"集合s2长度为{len(s2)}","\n")
print("删除{}个重复元素".format(len(list1)-len(s2))) 