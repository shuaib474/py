i=int(1)
sum=int(input("输入数字:")) 
while sum>i:
    print(sum)
    remainder=sum%7
    if remainder==0:
        print(int(7))
        print("约数7")
        break
    else:
        sum=remainder
        if sum==1:
            print("互质")
            break
        elif sum>=1 and sum<7:
            print("互质")
            break

        