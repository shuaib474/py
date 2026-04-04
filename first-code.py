def x():
    count=int(input("输入数字"))
    while count>=1:
        if count<=15 and count>=10:
            print(count)
            count=count-1
        elif  count>5 and count<10:
            print(count)
            count=count-1
        else:
            return"sb"
    return count
result=x()
print(result)