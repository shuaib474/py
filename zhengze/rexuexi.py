s="hfkuhiu678678--3330526125@qq.com;名字:浩南"
import re
t_t=re.search(r"--(.+?);",s)
t=t_t.group(1) if t_t else  None
print(t)
v_v=re.findall(r"(6[3-9]\d{1})--",s)
v=v_v[0] if v_v else None
print(v)
k="user:zhangsan123@163.com;age:20"
print(re.search(r":(.*?\.\w+);",k).group(1))
m="phone:13800138000;name:李四"
print(re.search(r":(\w+);",m).group(1))
n="info:小明-2024001;class:计算机1班"
print(re.search(r":(.*?)-",n).group(1))
print(re.search(r"-(2[0-9]\d{5});",n).group(1))
u="ids:1001,1002,1003,1004;end"
print(re.findall(r"(\d+)",u)[0:5])
sz=re.findall(r"(\d+)",u)
print(sz[0])
h="data:abc678def--999@qq.com;test"
print(re.search(r"(6[3-9]\d{1})def",h).group(1))
print(re.search(r"--(9[3-9]\d{1})@(.*?);",h).group(1)+re.search(r"--(9[3-9]\d{1})@(.*?);",h).group(2))


