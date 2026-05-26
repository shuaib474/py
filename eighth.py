import random
secret=random.randint(1,100)
print("输入1到100的数字")
while True:
    try:
        guess=int(input("请输入数字:"))
        if guess==secret:
            print("猜对了!")
            break
        elif guess>secret:
            print("猜大了")
        elif guess<secret:
            print("猜小了")
    except  ValueError:
        print("你输你m呢")
        

