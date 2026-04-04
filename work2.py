a,b=input("请输入名字与年龄:").split(" ")
list_1=[{"name":a,"age":b}]
for item in list_1:
    print(item["name"])
    print(item["age"])
career=input("输入职业:")
list_1[0]["career"]=career
list_1[0]["age"]=input("重新输入年龄:")
for i in list_1:
    print(i["name"],i["age"],i["career"])
#print(list_1)
text="hello python"
counts={}
for char in text:
    if char!=" ":
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1
print(counts)
