import random
secret=random.randint(0,20)
attempts=0
max_attempts=5
try:
    while attempts<5:
        guess=int(input("请输入数字:"))
        print("输入1到20的数字")
        attempts+=1
        if guess==secret:
            print(f"猜对了,仅用{attempts}次")
            break
        elif guess>=secret:
            print(f"猜大了,还有{max_attempts-attempts}次机会")
        elif guess<=secret:
            print(f"猜小了,还有{max_attempts-attempts}次机会")
    else:
        print("sb,没次数了")
except ValueError:
    print("老冯升天了不会输数字吗 ")
print("菜就多练")

        